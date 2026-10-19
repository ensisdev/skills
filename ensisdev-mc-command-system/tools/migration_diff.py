#!/usr/bin/env python3
"""Migration diff: compare old vs new command ASTs, list path changes with dispositions (Phase 14, refs 43/44).

Usage: python tools/migration_diff.py <old_ast.json> <new_ast.json>

Outputs a YAML-ish migration record skeleton: removed paths (need disposition),
added paths, and preserved paths.
"""
import json
import sys
from pathlib import Path


def leaves(node, trail, out):
    path = ' '.join(trail + [node.get('name', '?')])
    children = node.get('children', []) or []
    if not children:
        out.add(path)
    for ch in children:
        leaves(ch, trail + [node.get('name', '?')], out)


def main():
    if len(sys.argv) < 3:
        print('usage: migration_diff.py <old_ast.json> <new_ast.json>')
        sys.exit(2)
    old = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    new = json.loads(Path(sys.argv[2]).read_text(encoding='utf-8'))
    old_paths, new_paths = set(), set()
    leaves(old['root'], [], old_paths)
    leaves(new['root'], [], new_paths)
    removed = sorted(old_paths - new_paths)
    added = sorted(new_paths - old_paths)
    kept = sorted(old_paths & new_paths)
    print(f'Migration diff: {len(removed)} removed, {len(added)} added, {len(kept)} preserved')
    if removed:
        print('migration:')
        for r in removed:
            print(f'  - old_path: {r}')
            print('    disposition: TODO # preserve | alias | deprecate | migrate | remove (43/44)')
    if added:
        print('added:')
        for a in added:
            print(f'  - {a}')


if __name__ == '__main__':
    main()
