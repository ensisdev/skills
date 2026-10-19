#!/usr/bin/env python3
"""Collision checker: AST roots/aliases vs reserved Vanilla/proxy/common-plugin roots (Phase 10, ref 20).

Usage: python tools/collision_check.py <ast.json> [--extra a,b,c]

Exit 1 on hard collision with reserved roots; exit 0 otherwise (warnings only).
"""
import json
import sys
from pathlib import Path

# Conservative reserved set: Vanilla + common proxy + plugin-ecosystem roots.
RESERVED = {
    # vanilla
    'help', 'op', 'deop', 'stop', 'kick', 'ban', 'ban-ip', 'pardon', 'whitelist',
    'gamemode', 'give', 'tp', 'teleport', 'time', 'weather', 'difficulty',
    'gamerule', 'tell', 'msg', 'w', 'me', 'say', 'list', 'seed', 'spawnpoint',
    'setworldspawn', 'defaultgamemode', 'advancement', 'bossbar', 'data', 'datapack',
    'effect', 'enchant', 'execute', 'fill', 'function', 'loot', 'particle',
    'playsound', 'recipe', 'reload', 'schedule', 'scoreboard', 'setblock',
    'summon', 'tag', 'team', 'title', 'trigger', 'worldborder', 'locate',
    # proxy
    'server', 'send', 'hub', 'lobby', 'glist',
    # ecosystem (common roots worth a conscious decision, not an accident)
    'essentials', 'eco', 'luckperms', 'lp', 'vault', 'plotsquared', 'plot',
    'worldedit', 'we', 'worldguard', 'wg', 'residence', 'griefdefender', 'gd',
}


def collect(node, trail, out):
    name = node.get('name', '?')
    path = trail + [name]
    out.append(('/'.join(path), node))
    for a in node.get('aliases', []) or []:
        out.append(('/'.join(trail + [a + ' (alias)']), node))
    for ch in node.get('children', []) or []:
        collect(ch, path, out)


def main():
    if len(sys.argv) < 2:
        print('usage: collision_check.py <ast.json> [--extra a,b,c]')
        sys.exit(2)
    extra = set()
    for arg in sys.argv[2:]:
        if arg.startswith('--extra'):
            extra |= set(arg.split('=', 1)[1].split(','))
    reserved = RESERVED | {e.strip().lower() for e in extra if e.strip()}
    ast = json.loads(Path(sys.argv[1]).read_text(encoding='utf-8'))
    nodes = []
    collect(ast['root'], [], nodes)
    root_name = ast['root'].get('name', '').lower()
    root_aliases = {a.lower() for a in ast['root'].get('aliases', []) or []}
    errors, warnings = [], []
    for cand, label in [(root_name, 'root')] + [(a, 'root alias') for a in root_aliases]:
        if cand in reserved:
            errors.append(f'{label} {cand!r} collides with reserved Vanilla/proxy/ecosystem root (see 20)')
    # single-letter roots are accident-prone
    if len(root_name) == 1:
        warnings.append(f"root {root_name!r} is a single letter; prefer a readable name (19)")
    print(f'Collision check: {len(errors)} errors, {len(warnings)} warnings')
    for e in errors:
        print('ERROR', e)
    for w in warnings:
        print('WARN', w)
    sys.exit(1 if errors else 0)


if __name__ == '__main__':
    main()
