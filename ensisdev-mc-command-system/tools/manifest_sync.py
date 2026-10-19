#!/usr/bin/env python3
"""Manifest sync: diff a command AST against plugin.yml/paper-plugin.yml (Phase 12, ref 52).

Usage: python tools/manifest_sync.py <ast.json> <plugin.yml>

Compares root name, aliases, root permission and description against the
manifest's commands.<name> block. Minimal YAML-subset parser (stdlib only);
handles the flat mapping shape of plugin manifests.
"""
import json
import sys
from pathlib import Path


def parse_manifest(text):
    """Parse top-level and one nested level of a simple manifest."""
    root, stack = {}, []
    for raw in text.splitlines():
        if not raw.strip() or raw.strip().startswith('#'):
            continue
        indent = len(raw) - len(raw.lstrip(' '))
        key, _, val = raw.strip().partition(':')
        key, val = key.strip(), val.strip()
        while stack and stack[-1][0] >= indent:
            stack.pop()
        node = root if not stack else stack[-1][1]
        if val == '':
            child = {}
            node[key] = child
            stack.append((indent, child))
        else:
            if val.startswith('[') and val.endswith(']'):
                node[key] = [v.strip() for v in val[1:-1].split(',') if v.strip()]
            else:
                node[key] = val.strip('"\'')
    return root


def main():
    if len(sys.argv) < 3:
        print('usage: manifest_sync.py <ast.json> <plugin.yml>')
        sys.exit(2)
    ast = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    manifest = parse_manifest(Path(sys.argv[2]).read_text(encoding='utf-8'))
    root = ast['root']
    name = root.get('name', '')
    errors, warnings = [], []

    commands = manifest.get('commands', {})
    if not isinstance(commands, dict) or name not in commands:
        errors.append(f"manifest missing commands.{name} (see 52)")
        print(f'Manifest sync: {len(errors)} errors, {len(warnings)} warnings')
        for e in errors:
            print('ERROR', e)
        sys.exit(1)
    block = commands[name]
    ast_aliases = set(root.get('aliases', []) or [])
    man_aliases = set(block.get('aliases', []) or [])
    if ast_aliases != man_aliases:
        warnings.append(f'alias drift: AST {sorted(ast_aliases)} vs manifest {sorted(man_aliases)}')
    ast_perms = set(root.get('permissions', []) or [])
    man_perm = block.get('permission')
    if man_perm and man_perm not in ast_perms:
        warnings.append(f'manifest permission {man_perm!r} not in AST root permissions {sorted(ast_perms)}')
    help_ = root.get('help') or {}
    if help_.get('summary') and block.get('description') \
            and block['description'] != help_['summary']:
        warnings.append('description differs between manifest and AST help.summary (08/52)')
    perms = manifest.get('permissions', {})
    for p in ast_perms:
        if isinstance(perms, dict) and p not in perms:
            warnings.append(f'AST permission {p!r} not declared in manifest permissions block')
    print(f'Manifest sync: {len(errors)} errors, {len(warnings)} warnings')
    for e in errors:
        print('ERROR', e)
    for w in warnings:
        print('WARN', w)
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
