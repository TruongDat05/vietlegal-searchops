---
name: vietlegal-debug
description: Diagnose VietLegal SearchOps bugs, failing tests, incorrect outputs and performance regressions with a reproducible signal and a focused fix. Use when behavior is broken or unexpectedly slow, rather than for ordinary feature implementation.
---

# VietLegal debugging

Find the cause, fix it at the appropriate shared layer and verify the original
scenario. Read [AGENTS.md](../../../AGENTS.md) and the relevant
[development references](../vietlegal-dev/SKILL.md).

## Reproduce the actual symptom

Read the error/output, relevant diffs, configuration and affected callers. Find
the exact command, fixture, CLI/API request or saved artifact that detects the
user's symptom. Minimize the input while retaining that signal. Prefer a fast
deterministic offline reproduction over repeated provider calls.

For artifact failures, verify corpus, snapshot, checkpoint, input profile and
code/run identities before interpreting results. For flaky behavior, record
timing/concurrency and a repeatable reproduction policy; a lucky pass is not a fix.
Use temporary artifact copies/roots for reproductions that mutate state. Redact
credentials and preserve the original failing input, snapshot and run identity.

## Isolate the cause

Trace the bad value/state to the earliest incorrect transformation. Inspect the
evidence needed to distinguish plausible causes. State a testable hypothesis,
change one relevant condition and rerun. Revise disproved hypotheses instead of
stacking unrelated fixes.

Useful project fault boundaries:

- Raw source -> normalization -> revision/span mapping.
- Full input/profile -> cache entry -> occurrence/vector mapping.
- Target -> updater -> independent full rebuild -> snapshot activation.
- Branch ranks -> selected context -> actual sent messages.
- Saved prediction/attempts -> gold join -> metrics/judge -> reported denominator.

For wrong answers, inspect permitted source provenance, ranks, selected/sent
context and generation/citations first. Consult labels only in the split and
role already authorized: use handed-off train/dev qrels during selection; keep
held-out test gold with the custodian. After frozen predictions exist, an
authorized scoring/audit task can inspect the corresponding gold and verdicts.
Never expose held-out labels to fix the current model, prompt or retrieval policy.
Retrieval quality and a software defect are different findings; correct code
alone does not prove better accuracy.

For slowness, capture a baseline/profile with fixed inputs and cache policy.
Separate encode, FTS/matrix, loading and provider time when relevant; fewer tokens
or replay results do not establish measured latency improvements.

## Fix and verify

- Keep a regression test at the interface exposing the failure. Observe its
  expected failure before the fix when feasible; disclose missing artifacts or
  environment limitations that prevent reproduction.
- Fix the shared cause and inspect sibling callers. Preserve explicit failures;
  avoid silent model/profile fallback, dropped records or weakened assertions
  added merely to make a check green.
- Debugging a frozen run must preserve its original outputs and profiles. A
  subsequent code/prompt/configuration change produces a separately identified
  run; do not overwrite evidence or reuse final test feedback for tuning.
- Rerun the original scenario, regressions and implemented offline suite using
  the [verification guide](../vietlegal-dev/references/testing.md).
- Remove instrumentation introduced by this task without deleting the user's
  logs or research artifacts. Preserve useful failure evidence.

Repeated failed fixes call for rechecking assumptions and the fault boundary.
Explain missing evidence when progress depends on inaccessible state; request
only the information needed to continue.

Report cause, changed behavior, checks/results and remaining uncertainty. Use
the Git skill only when committing is requested.
