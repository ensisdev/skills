#!/usr/bin/env python3
"""AST linter for EnsisDev command trees (Phase 10). Stdlib only.

Usage: python tools/ast_lint.py <ast.json> [--strict]

Checks: schema-conformance essentials, depth budget, alias/canonical
integrity, permission + risk + help + completion coverage, context
validity, deprecation record shape.
"""
import json
import sys
from pathlib import Path

VALID_KINDS = {'root', 'literal', 'argument', 'group', 'property', 'action', 'flag'}
VALID_CONTEXTS = {'player', 'console', 'admin', 'moderator', 'automation',
                  'rcon', 'gui', 'npc', 'script'}
VALID_RISK = {'read', 'mutate', 'destructive', 'bulk-destructive', 'system'}
MAX_DEPTH = 4


def lint(ast, strict=False):
    errors, warnings = [], []

    def err(m):
        errors.append(m)

    def warn(m):
        (errors if strict else warnings).append(('STRICT ' if strict else '') + m)

    if ast.get('version') != '4':
        err('version must be "4"')
    if 'root' not in ast:
        err('missing root')
        return errors, warnings

    seen_paths = {}
    seen_aliases = {}

    def walk(node, trail, depth):
        path = ' '.join(trail + [node.get('name', '?')])
        kind = node.get('name', node.get('kind', '?')) and node.get('kind')
        if not node.get('name'):
            err(f'{path}: missing name')
        if kind not in VALID_KINDS:
            err(f'{path}: bad kind {kind!r}')
        if depth > MAX_DEPTH:
            err(f'{path}: depth {depth} exceeds budget {MAX_DEPTH} (see 18)')
        for c in node.get('contexts', []) or []:
            if c not in VALID_CONTEXTS:
                err(f'{path}: bad context {c!r}')
        for a in node.get('arguments', []) or []:
            if 'name' not in a or 'type' not in a:
                err(f'{path}: argument missing name/type')
        children = node.get('children', []) or []
        if children:
            if node.get('risk'):
                warn(f'{path}: risk on branch node; risk belongs on leaves (23)')
            for ch in children:
                walk(ch, trail + [node.get('name', '?')], depth + 1)
        else:
            # leaf rules
            if not node.get('permissions'):
                warn(f'{path}: leaf without permissions')
            if not node.get('risk'):
                err(f'{path}: leaf without risk class (23)')
            elif node['risk'] not in VALID_RISK:
                err(f'{path}: bad risk {node["risk"]!r}')
            help_ = node.get('help') or {}
            if not help_.get('summary') or not help_.get('usage'):
                warn(f'{path}: leaf without help summary/usage (08)')
            if (node.get('completion') is None) and kind in ('argument', 'literal'):
                warn(f'{path}: leaf without completion metadata (11)')
            if node.get('risk') in ('destructive', 'bulk-destructive', 'system'):
                impl = node.get('implementation') or {}
                if 'audit' not in impl and 'thread_affinity' not in impl:
                    warn(f'{path}: high-risk leaf without implementation.audit note (34)')
        for alias in node.get('aliases', []) or []:
            if alias in seen_aliases:
                err(f'{path}: alias {alias!r} also on {seen_aliases[alias]}')
            seen_aliases[alias] = path
        dep = node.get('deprecation') or {}
        if dep and 'disposition' not in dep:
            err(f'{path}: deprecation without disposition (43)')
        key = path.lower()
        if key in seen_paths:
            err(f'{path}: duplicate path (also at {seen_paths[key]})')
        seen_paths[key] = path

    walk(ast['root'], [], 1)
    return errors, warnings


def main():
    if len(sys.argv) < 2:
        print('usage: ast_lint.py <ast.json> [--strict]')
        sys.exit(2)
    strict = '--strict' in sys.argv
    ast = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    errors, warnings = lint(ast, strict)
    print(f'AST lint: {len(errors)} errors, {len(warnings)} warnings')
    for e in errors:
        print('ERROR', e)
    for w in warnings:
        print('WARN', w)
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
