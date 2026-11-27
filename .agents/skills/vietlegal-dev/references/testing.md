# Appropriate verification

Use the actual project environment and configured commands. At skill creation,
`pyproject.toml` and the test files were plans, not an installable application or
an implemented suite. Inspect the current checkout again; do not preserve that
state as a permanent assumption or invent passing checks.

## Choose the check by the change

- For code behavior, test its public interface with small independent expected
  results. For bugs, keep a reproduction that detects the user's actual symptom.
- Verify a failing regression reaches the intended behavior rather than failing
  from a syntax error, unavailable dependency or broken setup. Run the same
  scenario after the fix; a newly added test that only passes once is weaker
  evidence than an observed reproduction and verified correction.
- For documentation/skills, check frontmatter, links, examples and consistency
  with project sources. Do not add application tests merely to test wording.
  Agent-based evaluation of the skills is optional, not required by this set.
- For performance, measure a comparable before/after baseline and preserve
  correctness/parity. A workload estimate alone cannot establish speedup.
- Reuse configured lint/format/type/build commands where applicable. Select the
  packaging/runtime in an environment task before prescribing installation.

Use focused checks while editing, then the implemented offline suite once before
completing application code changes. Rerun when new changes, failures or an
unresolved concern justify it. Report pre-existing failures accurately; avoid
unrelated fixes just to obtain a green suite.

Run against the final relevant code/configuration and record the command,
interpreter/environment and observed result. An earlier pass is reusable only
while its inputs and covered behavior remain unchanged. State whether a failure
is known to predate the patch; if no baseline was observed, say it is unclassified.

## Map changes to planned coverage

All paths below are under `tests/`. These are coverage targets, not assertions
that test functions already exist.

| Changed area | Test file | Meaningful coverage |
| --- | --- | --- |
| Crawl, corpus, datasets | `test_sources_and_splits.py` | Original bytes, hashes, Unicode spans, revision/source identity, accepted exports, split inheritance and gold-free public cases |
| Chunking, E5, cache, training | `test_encoder_and_training.py` | Prefix/budget, vector/profile validation, breadcrumb/weights misses, metadata hits, sampler collisions and dev-only selection |
| Update and snapshots | `test_updates_and_snapshots.py` | Independent parity, idempotency, shared vectors, partial work, crash/resume, publication failure and concurrent historical pins |
| Search and context | `test_retrieval_and_context.py` | FTS order/escaping, RRF/ties, complementary spans, serialized budgets and shared CLI/API/collector behavior |
| Predictions and metrics | `test_predictions_and_evaluation.py` | Save-before-dispatch/scoring, alternative evidence sets, eligible/failure counts, grouped pairs and uncertain attempts |
| HTTP, Qwen and judge | `test_api_and_judge.py` | Contract/source revisions, citation errors, exact actual context, fake provider identity/errors, budgets and blind calibration |

Once runnable tests and packaging exist, commands may look like:

```bash
python -m pytest -q tests/test_updates_and_snapshots.py
python -m pytest -q
```

Use the project's selected interpreter and configuration; these are examples,
not a claim of a currently working setup. A zero-test or all-skipped run does not
verify application behavior. Read collection, failures, skips and exit status.
Expected optional skips may be legitimate; explain them if they leave changed
behavior unverified. Do not turn failures into skips or ignore a nonzero exit
status to manufacture a passing result.

## Keep offline checks independent and useful

Use checked-in tiny reviewed source fixtures, fixed ranks/vectors, tokenizer
fixtures, fake HTTP transports and temporary isolated artifact roots. Offline CI
must not need downloads, credentials, provider calls or restricted real test gold.
Exercise real internal behavior; fake only external/expensive boundaries.
Keep test databases/caches separate from retained real artifacts. Do not read
live restricted test gold or production cache state to construct CI expectations.
Make accidental live calls/model downloads fail in offline checks instead of
silently treating them as extra verification.

Expected results must come from known examples/specifications, not the production
function under test or a second copy of its algorithm. Relevant examples:

- Relevant sources `{a,b}` and ranks `[a,z,b]` give Recall@3 = 1 and nDCG@3 about
  0.91972 under the specified binary policy.
- Evidence alternatives `[{a,b},{c}]` require both a+b or c; only a fails. Check
  actual retained text/spans as well as the IDs.
- A metadata-only change can reuse vectors and must still update metadata.
- Corrupt candidate membership must be detected by independent full reconstruction.
- An activation failure must leave the old snapshot usable by pinned requests.

These are constructed expectations, not measured project results. Do not mirror
implementation with tautological assertions, weaken tests to match bugs or add
`assert True` to hide missing coverage.

## Keep evidence levels explicit

| Evidence | Supports | Does not establish |
| --- | --- | --- |
| Structural/frontmatter/link checks | Files are well formed and referenced resources exist | Agents always follow instructions or the application works |
| Offline fixture/fixed-vector tests | Software behavior for tested cases | Real encoder/provider availability, accuracy or throughput |
| Actual model reload/inference/provider smoke | The observed path works in that environment | A quality improvement or a reproducible final comparison |
| Locked comparable benchmark | Measured results under that protocol | Broader legal correctness or untested domains/workloads |

Live inference, crawling, training or benchmarks need the user's corresponding
task scope and budgets; they are not default consequences of running checks.
