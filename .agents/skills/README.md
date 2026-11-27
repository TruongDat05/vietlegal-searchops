# VietLegal shared skills

Start with [AGENTS.md](../../AGENTS.md), which contains the common rules. All
skill entrypoints and references are in English. Original project planning
documents remain local under the Git-ignored `docs/` directory.

| Skill | Use it for |
| --- | --- |
| [vietlegal-dev](vietlegal-dev/SKILL.md) | Focused implementation, refactoring and optimization with appropriate checks |
| [vietlegal-handoff](vietlegal-handoff/SKILL.md) | Ownership, shared contracts and H01-H09 acceptance |
| [vietlegal-debug](vietlegal-debug/SKILL.md) | Reproducing a bug, testing its cause and verifying the fix |
| [vietlegal-review](vietlegal-review/SKILL.md) | Reviewing requirements, code quality and evidence |
| [vietlegal-git](vietlegal-git/SKILL.md) | Coherent commits, accurate messages and optional Lazygit staging |

## Use on either contributor's machine

Keep these files in the repository so both contributors use the same version.
Each skill includes `SKILL.md` and Codex UI metadata in `agents/openai.yaml`.
Automatic selection is left enabled; discovery does not authorize commits,
publication or live experiments.

Use this set inside its project checkout: the relative references require
`AGENTS.md`, `ARCHITECTURE.md` and the bundled skill references, not local `docs/`.
Copying only one skill folder into a global catalog loses that shared project
context. For tools without discovery, provide this prompt, replacing the task:

```text
Read AGENTS.md and .agents/skills/README.md in this checkout. Read the SKILL.md
for this task and only the references relevant to it. Use the repository's
project documents and actual code as context. Complete this task: <task>.
```

Explicit invocation examples:

```text
Use $vietlegal-dev to implement RT-04 with offline context fixtures.
Use $vietlegal-handoff to prepare the H05 search/context handoff.
Use $vietlegal-debug to diagnose this snapshot/profile mismatch.
Use $vietlegal-review to review the uncommitted changes for IX-03.
Use $vietlegal-git to commit the authorized changes as coherent commits.
```

If `$skill-name` is unsupported, give its file path. No other globally installed
skill, plugin, issue tracker or sub-agent is required. See
[attribution and licenses](THIRD_PARTY_NOTICES.md) for adapted coding guidance.

Choose the requested operation first. Debugging and review consult the development
references without automatically implementing features. A review-only task stays
read-only; an explicit request to improve the reviewed files authorizes scoped
fixes. Read shared instructions once per task and load only affected contract
sections; do not reload every skill or reference on each edit.

## Maintain the instructions

Keep shared contracts, task ownership and handoffs in `ARCHITECTURE.md`, with
focused scope/protocol rules in the skill references. Reflect authorized decisions
from local planning documents in these shared sources when needed. Update affected
references when decisions change. Keep descriptions specific. Ordinary
skill edits need frontmatter/reference checks; behavioral skill evaluation is
optional. Structural validation establishes file quality, not guaranteed agent
behavior. Report only the evidence actually collected.
