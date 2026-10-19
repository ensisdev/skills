#!/usr/bin/env python3
"""EnsisDev v4.1 package validator. Stdlib only.

Checks: required files, SKILL routing coverage, AST schema shape,
benchmark manifest/case/golden consistency, pattern format,
template AST validity, duplicate reference titles.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
errors = []
warnings = []


def err(msg):
    errors.append(msg)


def warn(msg):
    warnings.append(msg)


# 1. Required files -----------------------------------------------------------
required = [
    'SKILL.md', 'README.md', 'SOURCES.md',
    'schemas/command-ast.schema.json',
    'benchmarks/manifest.json', 'benchmarks/SCORING.md',
    'references/17-decision-engine.md',
    'references/28-command-ast.md',
    'references/37-benchmark-methodology.md',
    'references/39-self-audit.md',
    'references/40-pattern-capture.md',
    'references/45-folia-threading.md',
    'references/46-version-matrix.md',
    'references/47-proxy-network.md',
    'references/48-messages-localization.md',
    'references/49-economy-cooldown.md',
    'references/50-integration-contracts.md',
    'references/51-command-testing.md',
    'references/52-plugin-manifest-sync.md',
    'references/53-interactive-help.md',
    'references/54-microcopy.md',
    'references/55-completion-at-scale.md',
    'showcase/warp-redesign/README.md',
    'showcase/warp-redesign/new-ast.json',
    'showcase/warp-redesign/new-ast-admin.json',
    'showcase/warp-redesign/audit.md',
    'benchmarks/golden/01-hologram-resource.ast.json',
    'benchmarks/golden/03-player-warps.ast.json',
    'tools/ast_lint.py', 'tools/collision_check.py',
    'tools/manifest_sync.py', 'tools/migration_diff.py',
]
for f in required:
    if not (ROOT / f).exists():
        err('missing: ' + f)

# 2. AST schema shape ----------------------------------------------------------
try:
    s = json.loads((ROOT / 'schemas/command-ast.schema.json').read_text())
    for k in ('$schema', 'type', 'properties', '$defs'):
        if k not in s:
            err('AST schema missing ' + k)
    node_props = s.get('$defs', {}).get('node', {}).get('properties', {})
    for k in ('name', 'kind', 'permissions', 'contexts', 'risk',
              'completion', 'help', 'deprecation', 'implementation', 'aliases'):
        if k not in node_props:
            err('AST schema node missing ' + k)
except Exception as e:
    err('AST schema invalid: ' + str(e))

# 3. SKILL routing coverage -----------------------------------------------------
try:
    skill = (ROOT / 'SKILL.md').read_text(encoding='utf-8', errors='replace')
    refs = sorted(p.name for p in (ROOT / 'references').glob('*.md'))
    for r in refs:
        stem = r[:-3]
        if stem not in skill:
            warn('SKILL.md does not reference ' + r)
    if 'Lite track' not in skill and 'lite track' not in skill:
        warn('SKILL.md missing lite track')
except Exception as e:
    err('SKILL read failed: ' + str(e))

# 4. Benchmark manifest ---------------------------------------------------------
try:
    m = json.loads((ROOT / 'benchmarks/manifest.json').read_text())
    for stem in m.get('cases', []):
        if not (ROOT / 'benchmarks/cases' / f'{stem}.md').exists():
            warn('case missing: ' + stem)
        if not (ROOT / 'benchmarks/golden' / f'{stem}.json').exists():
            warn('golden missing: ' + stem)
    for stem in m.get('cases', []):
        g = ROOT / 'benchmarks/golden' / f'{stem}.json'
        if g.exists():
            try:
                gj = json.loads(g.read_text())
                if 'requirements' not in gj:
                    err(f'golden {stem}.json missing requirements')
                if 'expected_paths' not in gj:
                    warn(f'golden {stem}.json missing expected_paths')
            except Exception as e:
                err(f'golden {stem}.json invalid: {e}')
except Exception as e:
    err('benchmark manifest invalid: ' + str(e))

# 5. Pattern format --------------------------------------------------------------
for p in sorted((ROOT / 'patterns').glob('*.yaml')):
    text = p.read_text()
    for k in ('id:', 'name:', 'intent:', 'when:', 'avoid_when:',
              'structure:', 'constraints:', 'tradeoffs:', 'evidence:', 'status:'):
        if k not in text:
            err(f'pattern {p.name} missing {k}')
    m = re.search(r'status:\s*(\S+)', text)
    if m and m.group(1) not in ('experimental', 'established'):
        err(f'pattern {p.name} bad status {m.group(1)}')

# 6. Duplicate reference titles ---------------------------------------------------
titles = {}
for p in sorted((ROOT / 'references').glob('*.md')):
    text = p.read_text(encoding='utf-8', errors='replace')
    first = text.splitlines()[0] if text else ''
    titles.setdefault(first, []).append(p.name)
for t, files in titles.items():
    if len(files) > 1:
        warn(f'duplicate title {t!r}: {files}')

# 7. Shipped ASTs parse and carry version "4" ---------------------------------------
for ast_file in ['showcase/warp-redesign/new-ast.json',
                 'showcase/warp-redesign/new-ast-admin.json',
                 'benchmarks/golden/01-hologram-resource.ast.json',
                 'benchmarks/golden/03-player-warps.ast.json']:
    p = ROOT / ast_file
    if p.exists():
        try:
            a = json.loads(p.read_text(encoding='utf-8', errors='replace'))
            if a.get('version') != '4' or 'root' not in a:
                err(f'AST {ast_file} is not a v4 AST')
        except Exception as e:
            err(f'AST {ast_file} invalid: {e}')

print(f'EnsisDev v4.2 validation: {len(errors)} errors, {len(warnings)} warnings')
for e in errors:
    print('ERROR', e)
for w in warnings:
    print('WARN', w)
sys.exit(1 if errors else 0)
