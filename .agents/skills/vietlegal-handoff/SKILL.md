---
name: vietlegal-handoff
description: Coordinate VietLegal SearchOps ownership, shared interfaces and H01-H09 artifact handoffs between Dat and Lich. Use when starting shared work, changing a cross-owner contract, preparing integration or documenting a handoff.
---

# VietLegal team handoff

Make the receiving contributor able to develop and verify their module using
explicit interfaces and small fixtures. Preserve the agreed ownership.

## Identify responsibility and compatibility

Read [AGENTS.md](../../../AGENTS.md), the relevant task rows in
[ARCHITECTURE.md](../../../ARCHITECTURE.md#task-to-file-mapping), and its
[handoff mapping](../../../ARCHITECTURE.md#handoff-to-file-mapping-and-scheduling).
[The handoff reference](references/handoffs.md) maps owners and H01-H09.
Dat and Lich here mean Đạt and Lịch in the original plan.

- The primary owner delivers implementation, appropriate tests, documentation
  and artifacts. Packaging does not inherit every integration bug.
- For shared PL/EN tasks, first use the current user's assignment or an existing
  recorded implementer/reviewer. Ask only if no assignment can be established
  and the missing owner affects the work; continue independent preparation.
  Do not silently reassign a task owned by the other contributor or ask again
  for an assignment the user has already made.
- Implement an agreed contract directly. For a compatibility change, describe
  changed fields/semantics, callers/tests, migration/version policy and the
  receiving owner's required action. Label decisions still needed as proposals.
- Inspect every known consumer of a changed contract. A fixture must model that
  contract without relying on private internals or inaccessible live artifacts.
  Necessary caller fixes may be included in the authorized task without changing
  the contributor's ongoing ownership.
- Consumers use immutable bundles or documented read interfaces. They do not
  directly edit another module's snapshot membership, vector cache or gold.

## Keep the two workstreams moving

Use tiny schema-correct fixtures, fixed ranks/vectors and fake responses at the
agreed interface. Label them as fixtures. When integrating, keep the real search
implementation shared; remove temporary duplicate paths rather than retaining
a second production implementation.

Deliver seed H01 early, distinguish pilot H02 from main-data H04, and provide H03
metrics before checkpoint selection. H05 can use pretrained D0 and must not wait
for fine-tuning. Fixtures enable independent development; final acceptance still
needs the identified real artifacts and applicable checks.

## Prepare an actionable handoff

Use the [handoff template](references/handoff-template.md) in the current response
or an existing task/PR record. Create a separate report only when requested or
required by an established repository workflow. Include:

- Task/handoff, producer, receiver and compatible code/schema/profile identities.
- Entry points, inputs/outputs, artifact paths and manifest hashes for actual
  artifacts. Distinguish artifact aliases such as S1/E1 from experiments D1/H1.
- The smallest fixture/example and exact applicable verification command.
- Observed results, known limits and the receiver's next action.

Mark a handoff ready only when its particular acceptance conditions are evidenced.
H03 can be ready from deterministic fixture checks; H06 needs the actual encoder,
matching index and reload evidence. Do not require a live provider for every
handoff or call a fixture-only model run a real-artifact acceptance.

Readiness is the producer's claim; record receiver acceptance separately only
when it exists. Do not invent human labels, a teammate's review or approval.
Missing required artifacts mean a partial handoff even if code exists. Update
status from evidence, not elapsed time. Send it outside the current task only
when requested.
