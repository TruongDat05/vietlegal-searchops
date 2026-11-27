---
name: vietlegal-dev
description: Implement, refactor or optimize VietLegal SearchOps code against its project contracts, ownership and offline checks. Use for project coding tasks; use the specialized skills for debugging, handoffs, reviews or requested commits.
---

# VietLegal development

Implement the requested behavior with the smallest clear change that preserves
the source, snapshot and evaluation contracts.

## Establish the change

1. Read [AGENTS.md](../../../AGENTS.md), the task and the relevant
   [architecture](../../../ARCHITECTURE.md) sections. Find its task-to-file row,
   owner, public interfaces and existing callers/tests. If no task ID was given,
   infer the closest scope without inventing a new assignment.
2. Inspect the actual checkout. Docstrings, diagram filenames, config comments
   and target sample sizes are plans until implemented or measured.
3. Identify the observable behavior, affected callers and appropriate checks.
   Separate required behavior from provisional implementation choices. Use the
   user's existing authorization and agreed interfaces; surface only unresolved
   decisions that materially change the result. Continue independent work.

Read only the references needed for the change:

- Ingestion, source mapping, chunking, E5, cache, updates, snapshots or retrieval:
  [source and index rules](references/source-and-index.md).
- Datasets, fine-tuning, generation, collection, metrics or judge:
  [data, training and evaluation rules](references/data-training-evaluation.md).
- New behavior or a bug fix: [verification guide](references/testing.md).
- A cross-owner interface change: [vietlegal-handoff](../vietlegal-handoff/SKILL.md).

## Implement one useful slice

- Trace the affected flow before editing. Reuse a helper, standard-library
  feature or installed dependency before creating new machinery.
- Keep interfaces small and domain terms consistent. Use ordinary functions and
  records when sufficient. Add classes, factories, registries or configuration
  knobs for concrete requirements. Pass existing handles/clients into interfaces
  that need them so tests can use fixed vectors or fake transports.
- Prefer readable control flow over compressed expressions. Preserve validation,
  explicit failures, provenance, accounting and crash recovery when simplifying.
- Add meaningful behavior checks alongside substantive logic. For a bug, first
  reproduce the failure and retain a regression check when feasible. Change
  implementation and its tests in small useful steps.
- Keep one search core for CLI/API/collector. Honor architecture dependency
  directions. A necessary interface/dependency change must stay within the
  authorized task and update the documented decision and affected callers;
  changing documentation alone does not resolve a requirement conflict.
- Use the selected package manager and lockfile. If none exists, establish the
  minimum packaging required by an environment/implementation task rather than
  inventing setup commands. Add dependencies only for the requested slice; avoid
  import-time downloads, provider initialization or job execution. Resolve
  credentials and models only for the operation that actually needs them.
- Update contracts/configuration and concise usage documentation when behavior
  changes. Version profiles/schemas when compatibility changes. Preserve
  unrelated files and original research materials.

## Optimize with evidence

For a performance claim, measure the bottleneck first and compare the same inputs,
profiles, device and cache policy before and after. Code simplification alone
needs behavior checks, not an invented speed benchmark. Separate reduced workload
from measured wall time, API cost or model quality. Retain parity checks; avoid
adding an optional backend or optimizing an unmeasured path by default.

## Complete the task

Run the checks in [testing.md](references/testing.md). Read output and exit
status; resolve failures within scope and accurately report pre-existing or
external failures. A missing dependency or zero collected tests is a limitation,
not success. Checks must cover the final relevant code/configuration, not an
earlier intermediate state.

Review the final diff for unrelated changes and contract drift. Report delivered
behavior, relevant files, checks/results and remaining limitations. For handoffs,
include the receiving interface and artifact identities. Commit only when
requested, using [vietlegal-git](../vietlegal-git/SKILL.md).
