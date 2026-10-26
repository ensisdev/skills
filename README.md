# EnsisDev Minecraft Skills

Five agent skills for building, designing and reviewing Minecraft plugins/servers with an AI coding agent, written from 3+ years of Minecraft plugin/server development experience.

| Skill | Use for |
|---|---|
| [`ensisdev-mc-design-skill`](ensisdev-mc-design-skill) | Player-facing GUIs, chat, item lore, scoreboards, tablists, holograms, dialogs, shops, onboarding — anti-generic design rules and a review workflow. |
| [`ensisdev-mc-command-system`](ensisdev-mc-command-system) | Designing, reviewing, refactoring or migrating plugin/Skript commands — Brigadier/Cloud/CommandAPI trees, permissions, tab-completion, AST modeling, journey testing. |
| [`ensisdev-mc-scoreboard-engineering`](ensisdev-mc-scoreboard-engineering) | Scoreboard sidebar and TAB player-list design, MiniMessage formatting, small caps, resource-pack sprites, with an HTML preview + scoring script. |
| [`ensisdev-mc-blockdisplays`](ensisdev-mc-blockdisplays) | Planning block-display scenes (interiors/set-pieces built from display entities) — layout conventions, anchor policy, entity budgets by scale. |
| [`ensisdev-logo-design`](ensisdev-logo-design) | Logos and brand identity end to end (brief → concepts → SVG → tests → kit), with Minecraft server/plugin, Discord and dev-platform icon exports (`server-icon.png`, pixel-grid marks). Based on [kaankiziltug/logo-design-skill](https://github.com/kaankiziltug/logo-design-skill) (MIT). |

Each skill is scoped to avoid overlap — e.g. `ensisdev-mc-design-skill` defers scoreboard/TAB layout to `ensisdev-mc-scoreboard-engineering` and command copy to `ensisdev-mc-command-system`.

## Install

Each skill is a self-contained folder (`SKILL.md` + supporting files) following the [agentskills.io specification](https://agentskills.io/specification).

**Vercel Skills CLI:**
```bash
npx skills add ensisdev/skills
```

**Manual clone:**
```bash
git clone https://github.com/ensisdev/skills.git
cp -r skills/ensisdev-mc-design-skill <your-skills-directory>
# repeat for the others, or copy all of them
```

Point any skills-CLI-compatible tool at this repo, or copy the individual skill folder you need into that tool's skills directory. Folder name and the `name:` field in each `SKILL.md` match, so either can be used as the skill id.

## License

MIT — see [LICENSE](LICENSE). Each skill folder also carries its own copy.
