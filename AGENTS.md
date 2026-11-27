# Shared agent instructions

These instructions apply to this repository. Follow the current user request and
applicable higher-priority instructions. Both contributors use the same project
contracts; personal configuration must not silently change the deliverable.

## Start with the task

- Inspect the current branch, staged changes, working changes and relevant files.
  Preserve existing work and generated/restricted research artifacts.
- Read the relevant sections of [ARCHITECTURE.md](ARCHITECTURE.md), including the
  task-to-file mapping and assumptions affecting the task. Read callers and
  existing tests before changing a shared interface.
- Shared contracts, task ownership and H01-H09 handoffs are recorded in
  [ARCHITECTURE.md](ARCHITECTURE.md); the skill references explain the relevant
  operational rules. Planning material under `docs/` is local and intentionally
  ignored by Git. Consult it when available; a clone must not require it.
- Distinguish implemented interfaces from planned docstrings/configuration
  comments. The original scaffold-only restriction is historical, not a permanent
  prohibition on implementing a task the user requests.
- Separate required behavior from provisional choices and open assumptions.
  Code shows current behavior; it does not override an agreed requirement.
  A focused task does not authorize redesigning its surrounding architecture.
- Resolve routine choices using existing contracts. Ask only when missing
  information changes correctness, ownership, public contracts or scope. Surface
  substantive conflicts instead of silently choosing one. Check whether the
  current request or an earlier recorded decision already resolves the question.

## Select the applicable skill

Read the selected `SKILL.md` and only its relevant references. Resolve links from
the containing document; use the actual repository root for shell commands.

| Work | Skill |
| --- | --- |
| Implement, refactor or optimize project code | [vietlegal-dev](.agents/skills/vietlegal-dev/SKILL.md) |
| Prepare shared work, change a contract or deliver H01-H09 | [vietlegal-handoff](.agents/skills/vietlegal-handoff/SKILL.md) |
| Diagnose a bug, failing check or performance regression | [vietlegal-debug](.agents/skills/vietlegal-debug/SKILL.md) |
| Review a diff, task or pull request | [vietlegal-review](.agents/skills/vietlegal-review/SKILL.md) |
| Commit, split commits or perform authorized Git publication | [vietlegal-git](.agents/skills/vietlegal-git/SKILL.md) |

For bugs, combine development rules with the debugging workflow. For a commit
request, apply the Git skill after the change is reviewable. The
[catalog](.agents/skills/README.md) includes examples and a bootstrap prompt for
tools without automatic discovery.

## Keep changes focused

- Reuse existing code and the standard library before adding a dependency.
  Prefer clear names, direct control flow and small public interfaces. Preserve
  essential validation and recovery behavior when simplifying code.
- Add abstractions for concrete needs. Avoid speculative frameworks, backend
  hierarchies, unrelated refactors and optional research extensions.
- CLI, API and evaluation collection use the same retrieval implementation.
  Preserve source identities/spans, exact input/profile cache keys, immutable
  snapshots, gold-free inference and saved actual generator context.
- Keep the documented owners. A necessary shared-contract change includes
  affected callers, fixtures and compatibility information; it does not silently
  reassign the other contributor's work.
- Keep credentials out of logs, examples, manifests and commit content. Read
  restricted labels only for the authorized split and scoring/review role;
  ordinary debugging does not permit exposing held-out test gold during tuning.
- Write skill instructions, identifiers and code documentation in English.
  Preserve Vietnamese source material and the product's Vietnamese answers.
  Respond to the user in their chosen language.

## Verify and report

- Test behavior through the relevant interface using independent expected results.
  Add a regression check for a substantive bug and appropriate tests for new
  logic. Avoid implementation-mirroring and cosmetic tests.
- Use configured checks. Run focused checks while iterating and the implemented
  offline suite before completing application code changes. Documentation/skill
  edits need structural and link checks, not model calls or an agent-based skill
  evaluation campaign.
- Zero collected tests, all-skipped tests, test-plan docstrings and a missing
  environment are not passing application tests. State the actual limitation.
- Separate offline checks, real model/provider smoke tests and comparable
  benchmarks. Start live runs only within the user's authorized purpose/budget.
  Do not invent quality, latency, cost or completion claims.
- Report delivered behavior, verification commands/results and material remaining
  limitations. Verification must cover the final relevant code/configuration;
  rerun affected checks after further changes. Distinguish artifact readiness
  from the receiving contributor's actual acceptance and human review.

## Keep Git history useful

When asked to commit, split independent changes into coherent commits with
descriptive English messages. Keep a change with its matching tests and necessary
documentation. One coherent change can be one commit; several unrelated changes
must not be bundled into one. Inspect the staged patch before every commit,
preserve unrelated work, and push or rewrite history only when authorized.
