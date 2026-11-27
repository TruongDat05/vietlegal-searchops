# VietLegal SearchOps architecture scaffold

Status: architecture only, 26 November 2026. Every Python file is a single English
module docstring. Configuration, prompts, deployment and web files are comment-only
placeholders. Nothing here implements search, tests, model loading or deployment.
Task IDs below assign future work; none are marked complete by this scaffold.

## Sources and design decisions

Design sources and shared references:

- Original proposal (local planning material under ignored `docs/project/`): scope, sources,
  models, schemas and experimental protocol.
- Original ownership and handoff plan (local, not versioned here): all 107 core tasks, H01–H09,
  and the rule that ownership includes implementation, tests and artifacts.
- Original paper sections (`vietlegal_paper/sections/`, not included): 01 problem; 02 corpus; 03 retrieval;
  04 training; 05 hybrid/context; 06 benchmark; 07 updates; 08 agent; 09 evaluation;
  10 protocol; 11 integration; 12 limits; appendices with evidence/prediction contracts.
- [Workflow HTML](workflow.html), [SVG](workflow.svg) and [notes](workflow_notes.md):
  panels 00–05, artifact aliases and assumptions A1–A5. The HTML owns the drawing;
  the SVG is its export. Their 48 node identities and semantic text agree.
- The installed codebase-design and ponytail skills informed small interfaces,
  direct dependencies and responsibility consolidation.
- The [Spec Kit plan template](https://github.com/github/spec-kit/blob/main/templates/plan-template.md)
  was consulted only for organizing technical assumptions, project structure and
  validation gates. Spec Kit was neither initialized nor added as a dependency.

Current user constraints govern this scaffold. This document records the shared
behavior contracts and ownership derived from the original proposal, paper and
handoff plan. Those local/external sources are not required to use a clone;
the task and handoff tables below preserve the shared implementation contracts.
Workflow filenames, routes and bundle names were explicitly proposed, so this
document records their disposition rather than treating them as implementations.
Surface substantive conflicts instead of silently changing the agreed behavior.

The initial target is one Python application/library with CLI and HTTP callers,
SQLite/FTS5, local exact vectors, CPU E5 serving and remote fixed-weight Qwen/DeepSeek.
The Python version, dependency versions and container base remain unselected.
Sentence Transformers/PyTorch, NumPy, httpx and FastAPI are planned dependencies,
not installed requirements. Source readers depend on the formats actually used.

Callers supply resolved profiles, loaded snapshot/encoder handles and native HTTP
clients/transports or tokenizer/vector fixtures where needed. This makes the same
interfaces usable in offline tests without a custom provider hierarchy or factory.

The six labour-contract topics, three official source systems, mandatory E5
fine-tuning and fixed generator/judge roles remain the scope. The proposed
20–50 documents, 1,000–2,000 base training queries, 300 benchmark cases, three
seeds/arm and other sizes are planning targets. No data, checkpoint or metric
is implied by directory names. Optional OP-01–05 (quantization, accentless lexical,
extra paraphrases, expansion, OCR) receive no speculative modules.

## Exact current tree

This tree records the original application scaffold. The later shared agent
instructions are documented in [AGENTS.md](AGENTS.md) and the
[skill catalog](.agents/skills/README.md); they add no application runtime.

This tree lists the original scaffold files, including the three preserved workflow files.
It contains 41 source Python files, seven test-package Python files and no
generated runtime artifacts. Directory names inside the later artifact tables
are future paths, not additional files in this inventory.

```text
vietlegal_searchops/
├── artifacts/
│   └── README.md
├── config/
│   ├── corpus.toml
│   ├── evaluation.toml
│   ├── models.toml
│   ├── retrieval.toml
│   ├── training.toml
│   └── updates.toml
├── deploy/
│   ├── ci.yaml
│   ├── compose.yaml
│   └── Dockerfile
├── prompts/
│   ├── dataset_authoring.jinja
│   ├── deepseek_judge.jinja
│   ├── qwen_mcq.jinja
│   └── qwen_qa.jinja
├── rubrics/
│   └── qa.toml
├── src/
│   └── vietlegal_searchops/
│       ├── agent/
│       │   ├── __init__.py
│       │   ├── answer.py
│       │   └── qwen.py
│       ├── chunking/
│       │   ├── __init__.py
│       │   └── structure.py
│       ├── corpus/
│       │   ├── __init__.py
│       │   ├── normalize.py
│       │   └── release.py
│       ├── datasets/
│       │   ├── __init__.py
│       │   ├── authoring.py
│       │   ├── release.py
│       │   └── splits.py
│       ├── embedding/
│       │   ├── __init__.py
│       │   ├── cache.py
│       │   └── e5.py
│       ├── evaluation/
│       │   ├── __init__.py
│       │   ├── metrics.py
│       │   ├── runner.py
│       │   └── score.py
│       ├── indexing/
│       │   ├── __init__.py
│       │   ├── build.py
│       │   ├── snapshots.py
│       │   ├── update.py
│       │   └── verify.py
│       ├── ingest/
│       │   ├── __init__.py
│       │   └── crawl.py
│       ├── judge/
│       │   ├── __init__.py
│       │   ├── calibrate.py
│       │   └── deepseek.py
│       ├── retrieval/
│       │   ├── __init__.py
│       │   ├── context.py
│       │   └── search.py
│       ├── training/
│       │   ├── __init__.py
│       │   ├── select.py
│       │   └── train_e5.py
│       ├── __init__.py
│       ├── api.py
│       ├── cli.py
│       ├── config.py
│       ├── contracts.py
│       └── predictions.py
├── tests/
│   ├── fixtures/
│   │   └── README.md
│   ├── __init__.py
│   ├── test_api_and_judge.py
│   ├── test_encoder_and_training.py
│   ├── test_predictions_and_evaluation.py
│   ├── test_retrieval_and_context.py
│   ├── test_sources_and_splits.py
│   └── test_updates_and_snapshots.py
├── web/
│   └── index.html
├── .env.example
├── ARCHITECTURE.md
├── pyproject.toml
├── workflow_notes.md
├── workflow.html
└── workflow.svg
```

Every package has `__init__.py`; every initializer stays inert and has no
re-exports. The `src/` directory itself is a source-layout container, not a package.
The tests are specifications in docstrings, so running a test runner now would
not exercise the proposed behavior.

## Workflow reconciliation and responsibility ownership

Paths in this table are relative to `src/vietlegal_searchops/` unless stated
otherwise. Bare filenames in the workflow notes, such as `fetch.py`, are
interpreted within the package named in their row, never as new root modules.

| Workflow proposal | Scaffold disposition | Reason / single owner |
| --- | --- | --- |
| `ingest/discovery.py`, `ingest/fetch.py` | `ingest/crawl.py` | Discovery, traced attachments, fetch metadata and crawl resume form one ingestion job. |
| `corpus/normalize.py`, `corpus/structure.py`, `corpus/release.py` | Keep `normalize.py`; merge structure/identity/versioning/validation into `release.py`. | Extraction changes locally; one release owner locks text/spans and revision relations. |
| `chunking/structure.py`, `chunking/serialize.py` | `chunking/structure.py` | Passage serialization and chunk/source mapping must change together. |
| `datasets/groups.py`, `splits.py`, `authoring.py`, `audit.py` | `datasets/splits.py`, `authoring.py`, `release.py` | Split freeze, evidence authoring and accepted/exported releases have distinct access rules; audit belongs to release. |
| `training/train_e5.py`, `negatives.py`, `select.py` | `training/train_e5.py`, `select.py` | Mine negatives with the train-only sampler; selection is a separate dev-only interface. |
| `embedding/profile.py`, `e5.py`, `cache.py` | Profiles in `contracts.py`/`config.py`; retain `embedding/e5.py` and `cache.py`. | One profile contract; encoder and durable cache have different artifacts. |
| `indexing/update.py`, `journal.py`, `full_build.py`; `verification/update.py` | `indexing/update.py`, `build.py`, `verify.py` | Update recovery stays with update; full reference and comparison remain independent. |
| `snapshots/build.py`, `validate.py`, `loader.py`, `registry.py` | `indexing/snapshots.py` | One bundle/load/publish/pin interface owns snapshot lifecycle. `build.py` owns full target construction, not publication. |
| `snapshots/staging/` in panel 03 | Future `artifacts/staging/<job_id>/` | Runtime output is outside source packages. It is absent today. |
| `retrieval/lexical.py`, `dense.py`, `fusion.py`, `context.py` | `retrieval/search.py` plus `context.py` | BM25/dense/RRF are one search implementation; source-preserving context has a separate interface. |
| `agent/qwen.py`, `answer.py`, `validate.py` | `agent/qwen.py`, `answer.py` | Low-level provider/cache is reusable for drafting; answer flow owns output/citation checks. |
| `api/search.py`, `answer.py`, `sources.py`, `ui/` | Root `api.py`; `web/index.html` at scaffold root | One small HTTP module and one demo asset; no second search implementation. |
| `evaluation/runner.py`, `ledger.py`, `run_store.py`, `retrieval.py`, `metrics.py`, `reports.py` | `evaluation/runner.py`, `metrics.py`, `score.py`; root `predictions.py` | Collection, pure metrics and gold-enabled scoring separate; shared persistence must not depend on evaluation. |
| `judge/calibrate.py`, `deepseek.py`, `schema.py`, `rubrics/` | `judge/calibrate.py`, `deepseek.py`; `rubrics/qa.toml` at scaffold root | Judge schema/parser/cache stay with its provider; calibration owns human comparisons and J1. |

Semantic discrepancies and decisions:

1. Panel 04 says `/search` stops after RRF, while H05/RT-04 and retrieval evaluation
   need deterministic context without an LLM. The chosen interface returns ranks
   **and selected serialized context**. It never generates an answer. Retrieval
   metrics can use that fixed-budget context without Qwen/DeepSeek.
2. The notes associate retrieval context with “actual context”. These are two
   records: selected context from shared retrieval, then exact context/messages
   after the generator tokenizer/limit check. Only the latter supports judgments
   about what Qwen saw. Retrieval-only runs explicitly have no sent context.
3. Source-unit dedup for ranking metrics does not justify dropping all chunks of
   that unit from generation. The context owner deduplicates overlapping spans
   and keeps complementary rule/exception spans (paper 05).
4. Workflow arrows for dev selection are artifact dependencies, not an import from
   the serving module into an evaluator. `training/select.py` orchestrates dev
   collection/metrics and independent checkpoint-specific builds; serving imports
   neither training nor scoring.
5. C1/C2/T1/E1/S1/P1/G1/J1 identify artifacts; D1/D2/H0/H1 identify experiments.
   They are never interchangeable IDs. T1 includes train and dev qrels; held-out
   calibration/test labels stay in G1. Dev gold may also exist in G1 for QA scoring,
   but only explicit dev qrels go into the training handoff.
6. `GET /source`, the action enum and file layouts are scaffold choices under A1/A2,
   pending PL-03–06 review. No HTTP specification or schema has been implemented.
7. Release/benchmark parity is a required gate here, consistent with panel 03/A5.
   Continuous production audit cadence is still open; structural validation is
   mandatory on every publication.
8. “Gold only enters scoring” applies to inference. Evidence-first authoring and
   calibration have split-authorized label access. The shared low-level Qwen
   adapter can draft datasets, but the answer interface accepts no gold fields.

Single ownership prevents duplicate implementations: `corpus/release.py` owns
source identity; `chunking/structure.py` owns encoder passage serialization;
`embedding/e5.py` owns token counts/vector validation; `cache.py` owns vector hits;
`indexing/snapshots.py` owns snapshot projections/publication; `retrieval/search.py`
owns ranks; `context.py` owns retained source spans/serialization; `agent/answer.py`
owns answer/citation checks; `predictions.py` owns durable P1/attempts;
`evaluation/metrics.py` owns deterministic scores; `judge/calibrate.py` owns judge
agreement scores. A publisher consumes a parity report; it never invokes the verifier.

## Planned module dependency directions

An arrow means “may depend on”, not a data-flow arrow. Names below resolve to
exact files in the source tree. These are allowlists, not instructions to import
every listed module. Unlisted project dependencies are disallowed. External
libraries are identified in each module docstring. Namespace initializers have
no dependencies.

| Module | Allowed project dependencies |
| --- | --- |
| `agent.answer` | `contracts`, `config`, `predictions`, `retrieval.search`, `retrieval.context`, `indexing.snapshots`, `agent.qwen` |
| `agent.qwen` | `contracts`, `config` |
| `api` | `contracts`, `config`, `predictions`, `indexing.snapshots`, `retrieval.search`, `agent.answer` |
| `chunking.structure` | `contracts`, `config`, `embedding.e5` |
| `cli` | `config`, `ingest.crawl`, `corpus.release`, `datasets.release`, `training.train_e5`, `training.select`, `indexing.build`, `indexing.update`, `indexing.verify`, `retrieval.search`, `agent.answer`, `evaluation.runner`, `evaluation.score`, `judge.calibrate` |
| `config` | `contracts` |
| `contracts` | `none` |
| `corpus.normalize` | `contracts`, `config` |
| `corpus.release` | `contracts`, `config`, `corpus.normalize` |
| `datasets.authoring` | `contracts`, `config`, `corpus.release`, `datasets.splits`, `agent.qwen` |
| `datasets.release` | `contracts`, `config`, `corpus.release`, `datasets.splits` |
| `datasets.splits` | `contracts`, `config` |
| `embedding.cache` | `contracts` |
| `embedding.e5` | `contracts`, `config` |
| `evaluation.metrics` | `contracts` |
| `evaluation.runner` | `contracts`, `config`, `predictions`, `indexing.snapshots`, `indexing.update`, `indexing.verify`, `retrieval.search`, `agent.answer` |
| `evaluation.score` | `contracts`, `config`, `predictions`, `datasets.release`, `evaluation.metrics`, `judge.deepseek` |
| `indexing.build` | `contracts`, `config`, `corpus.release`, `chunking.structure`, `embedding.e5`, `indexing.snapshots` |
| `indexing.snapshots` | `contracts`, `config`, `embedding.e5` |
| `indexing.update` | `contracts`, `config`, `corpus.release`, `chunking.structure`, `embedding.e5`, `embedding.cache`, `indexing.snapshots` |
| `indexing.verify` | `contracts`, `config`, `indexing.build`, `indexing.snapshots`, `retrieval.search` |
| `ingest.crawl` | `contracts`, `config` |
| `judge.calibrate` | `contracts`, `config`, `predictions`, `judge.deepseek` |
| `judge.deepseek` | `contracts`, `config` |
| `predictions` | `contracts` |
| `retrieval.context` | `contracts`, `config`, `embedding.e5` |
| `retrieval.search` | `contracts`, `config`, `embedding.e5`, `embedding.cache`, `indexing.snapshots`, `retrieval.context` |
| `training.select` | `contracts`, `config`, `embedding.e5`, `indexing.build`, `evaluation.runner`, `evaluation.metrics` |
| `training.train_e5` | `contracts`, `config`, `datasets.release`, `datasets.splits`, `embedding.e5`, `retrieval.search` |

Tests may depend on the modules named in their own docstrings; production modules
never depend on tests. Configuration/contracts and inert package initializers
sit at the bottom. `cli.py` is a composition caller; it is never imported by core
modules. The evaluator's optional HTTP mode uses wire contracts and does not
import `api.py`. Judge modules do not import evaluation modules.

Important paths through this directed graph:

- `api` / `evaluation.runner` / `cli` → `retrieval.search` →
  `retrieval.context`, `indexing.snapshots`, `embedding.e5/cache` →
  `config/contracts`.
- `agent.answer` → the same retrieval flow + `agent.qwen` + `predictions`.
  No inference module depends on `datasets`, `evaluation.score` or `judge`.
- `training.select` → `evaluation.runner/metrics` + `indexing.build`.
  No evaluator imports training. Retrieval-only collection must dispatch without
  requiring generator credentials or initializing a model client.
- `indexing.verify` → `indexing.build` + `retrieval.search`;
  neither full builder, snapshot loader nor search calls the verifier/update planner.
- `evaluation.score` → `datasets.release` + `judge.deepseek` +
  `evaluation.metrics` + saved P1. It never imports collection, retrieval or generation.
- `datasets.authoring` → `agent.qwen` only for provider invocation, never
  `agent.answer`. No provider adapter reads dataset files.
- `judge.calibrate` → `judge.deepseek` + P1; no reciprocal import.

There are no planned module dependency cycles. The update→parity→publication
sequence is orchestrated by CLI/experiment callers, avoiding a
snapshots→verify→retrieval→snapshots cycle. The human handoff sequence is different
from the import graph and must be evaluated separately.

## Interface and record contracts

All names describe future interfaces. There are no classes/functions or schemas
implemented by these docstrings. `contracts.py` contains planned inference/source
record contracts; `datasets/release.py` owns TrainingSample/GoldRecord contracts
so label custody is explicit.

| Record / interface | Required inputs and resulting outputs | Invariants / failure behavior |
| --- | --- | --- |
| SourceSpan | `document_id, revision_id, unit_id, text_hash, start, end, locator` | Absolute Unicode code points in locked normalized revision text; `[start,end)`; bounds/slices must match. No byte or silently unit-relative offsets. |
| CorpusManifest / C1 | Raw manifest, extraction/normalization profile, documents/revisions/units/relations, dates/status and coverage → locked corpus release | Preserve original bytes/URLs/hashes; duplicate sources link to one document; amendments have separate identity; date uncertainty remains `unverified`. Changed normalization requires new text/hash and affected-label review. |
| Chunk occurrence / C2 | C1 + chunk/tokenizer profile → `occurrence_id`, ordered source spans, breadcrumb/body, complete input and hash | Chunk may cover multiple spans; full prefix/breadcrumb/body/special-token input is ≤512 tokens. Gold never depends on occurrence IDs. |
| EmbeddingProfile / E1 | Weights and tokenizer identities; preprocessing/prefix/serialization, pooling/L2, dimension, backend/dtype/quantization/inference settings → canonical hash | Query/passage role is explicit; mean pooling uses attention mask; output is finite, 384-dimensional, near-unit norm under declared tolerance. No implicit weights/backend substitution. |
| Embedding cache | SHA-256 of full UTF-8 input + SHA-256 of canonical profile → completed validated vector or miss | Store input/hash/shape/dtype/completion; body equality or semantic similarity is insufficient. Metadata outside input need not miss; breadcrumb/weights changes do. No occurrence membership in vector keys. |
| SplitManifest / T1 / G1 | Reviewed source-group equivalences + pre-authoring split policy → group/parent links, train/dev release, public cases and restricted labels | Train/dev/calibration/test groups freeze before generation; train prompts/mining exclude held-out target evidence. Variants, MCQ/QA and equivalent revisions inherit split. Search corpus may contain all source text. |
| GoldRecord | Case/version, alternative `evidence_sets`, reference answer, required facts/conditions, acceptable actions/options, reviewer/status/reason | Each alternative set needs all source atoms; empty evidence is not automatic success. Accept only reviewed cases; post-freeze edits create a new benchmark version. |
| `full_build` | Target C1, chunk/encoder profiles, explicit workload or fixed-vector mode → fresh staged S1 and workload log | Reference reconstructs every target membership from source releases; no old/candidate index, updater plan or candidate vector cache is an input. |
| `update_index/resume_update` | Base S1, target release, event labels, mode/cache policy and job/profile hashes → candidate S1 + journal/workload | Distinguish full/document/exact modes; resume only verified complete work for the same target/profile; reruns are idempotent; retain shared vectors and historical sources. |
| `verify_update` | Target, candidate, independent full rebuild, query suite and tolerance/tie-break profile → hash-bound diff/report | Compare source revisions, metadata, occurrences, complete inputs/profiles/vector mapping/values, FTS content/statistics and ranks. No mutation/publication. Fixed-vector checks establish software parity only. |
| SnapshotManifest / S1 | C1/C2/E1 references, immutable metadata/membership, FTS, vector matrix/row map and profile hashes → validated loaded handle | Validate completeness, exact membership, source availability, all file hashes and checkpoint consistency before publication; projections cannot mix revisions. |
| `publish/pin/resolve_source` | Validated loaded S1 + target/candidate-bound release audit → active reference; explicit/current snapshot → pinned handle; source IDs/span → historical text/raw references | One pin covers BM25, dense, context, Qwen and citations. Keep in-flight old handles/history. Reject missing/invalid snapshots, spans and profiles rather than silently selecting newer sources. |
| `search` | Gold-free query, optional verified applicability time, explicit/pinned S1 and retrieval/context profiles → raw branch/fused ranks, source maps, original/processed query, selected context and timing | B0 is lexical; D0/D1/D2 dense; H0/H1 RRF. Question-only retrieval also applies to MCQ. Lexical statistics belong only to S1. Stable tie-break uses locked identity ordering. |
| `select_context/fit_context` | Ranked spans + frozen serialization, rank/dedup/budget policy → ordered labels/text, retained-span maps and payload hash | Keep complementary spans. Count labels/breadcrumb/metadata under the reference E5 budget; additionally check actual Qwen tokenizer/input limits. Any reduction records exact remaining spans and profile. Gold cannot influence selection. |
| `answer_question` | Query/time, optional MCQ options, pinned S1 + locked profiles → Vietnamese answer, action, citations, raw response/errors and P1 | One retrieval pass; no gold/reference/acceptable-action fields. Save context/messages before dispatch. Validate citations against sent source spans and S1; preserve malformed outputs/errors instead of repairing after seeing labels. |
| `collect_predictions` | Gold-free case manifest, track, frozen run config and budgets → durable P1 + attempt ledger | Retrieval never calls either LLM. HTTP/direct collection reaches the same search/context code. Save a terminal prediction or explicit error for each requested item before scoring it. |
| `score_predictions` | Saved P1 + authorized labels, rubric/J1 and accounting config → metric/judge/report artifacts | Verify hashes and replay saved context, never rebuild it from today's corpus. Judge errors stay unscored. Gold cannot change predictions. |
| `judge_saved` / calibration | P1 actual context + gold/rubric → five JSON verdicts/reasons; blind human labels + calibration outputs → comparison, locked J1 and separate audit | Correctness, completeness, groundedness, citation support and appropriate action remain separate. Humans label before verdict reveal; no test tuning. Provider/model/rubric changes create new calibrated profiles. |

A planned SearchRequest admits only query, optional time/snapshot, explicit profiles
and top-k; an AnswerRequest adds mode/options. Benchmark case/group identifiers may
be carried for logging, but source groups, correct options, reference answers,
gold evidence and rubric labels are not query/context features. Unknown
label-bearing request fields must be rejected. Whether time is verified is part
of recorded source metadata; `as_of` cannot certify law-in-force automatically.

The provisional HTTP routes are `POST /search`, `POST /answer`, `GET /source`
and read-only `GET /status`. The first two return request/snapshot/checkpoint/profile
identities, ranked source mappings, relevant context, timing and explicit errors.
Source lookup requires snapshot/revision/unit IDs and an optional validated span;
it returns locked text/hash, locator and source/original-file references.
The status route reads persisted update/reuse/miss/workload/error records.
The provisional action enum is `answer`, `clarify`, `insufficient_evidence`,
`correct_premise`; conditional explanations use `answer`. PL-06 must finalize it.

## Persistent artifacts and access

These are precise **future** paths relative to `vietlegal_searchops/`, with
angle-bracket IDs substituted at runtime. Existing files are only the exact tree
above. Manifests are versioned and enumerate file hashes and parent manifests;
a content hash proves identity, not source/legal/label correctness.

| Alias / future artifact path | Writer → readers | Required contents / lifetime |
| --- | --- | --- |
| Raw: `artifacts/raw/<batch_id>/manifest.json`; `artifacts/raw/objects/<file_hash>` | `ingest/crawl.py` → corpus | Original bytes, page/file/origin URLs, fetched time, status/metadata, raw hashes, retry/extraction references; archive originals for cited history. |
| C1: `artifacts/corpus/<corpus_id>/manifest.json`, `revisions.jsonl`, `units.jsonl`, `coverage.json`, `text/<revision_id>.txt` | `corpus/release.py` → chunks, datasets, builders, source lookup | Document/revision/unit relations and source mapping, locked normalized texts/hashes, dates/status, normalization version, coverage/limits and raw refs. |
| C2: `artifacts/chunks/<chunk_profile_hash>/<corpus_id>/manifest.json`, `occurrences.jsonl` | `chunking/structure.py` → builds | Complete inputs/input hashes and occurrence→source-span maps, not vector ownership. |
| Groups: `artifacts/datasets/<dataset_id>/groups.jsonl`, `splits.json` | `datasets/splits.py` → authoring, training, evaluation | Equivalence decisions, split seed/version, parent/group inheritance and leakage audit references. |
| T1: `artifacts/datasets/<dataset_id>/train_dev/manifest.json`, `train.jsonl`, `dev_cases.jsonl`, `dev_qrels.jsonl`, `audit.jsonl` | `datasets/release.py` → training/dev evaluator | Pilot and main releases have different dataset IDs; query/positive/negative spans, review/provenance/variant links and dev qrels. No calibration/test gold. |
| Public cases: `artifacts/datasets/<dataset_id>/cases/manifest.json`, `dev.jsonl`, `calibration.jsonl`, `test.jsonl` | `datasets/release.py` → collector | Case/parent/variant/group/split, question/mode/options, snapshot/time and tags; label fields removed. |
| G1: `artifacts/restricted/gold/<benchmark_id>/manifest.json`, `dev.jsonl`, `calibration.jsonl`, `test.jsonl` | Dataset custodian → authorized scorer/calibrator | Source-anchored evidence sets, answers/facts/conditions/actions/options, reviews/status/version; no serving or collector mount/access. |
| Drafts: `artifacts/authoring/<job_id>/manifest.json`, `drafts.jsonl`, `reviews.jsonl` | `datasets/authoring.py` → reviewer/release | Source authorization, prompt/model/provider/sampling identity, raw outputs/usage and acceptance history; separate from inference P1. |
| Training: `artifacts/training/<run_id>/manifest.json`, `checkpoints/`, `training.jsonl`, `negatives.jsonl`, `dev_metrics.json` | Train/select → encoder release/reports | Initial identity, schedule/seeds/loss/sampling, tokens/loss/resources/errors, reviewed negatives and dev-only selection evidence. |
| E1: `artifacts/encoders/<encoder_release_id>/manifest.json`, `model/`, `inference.json` | Train/select + E5 exporter → builders/serving | Complete exported weights, tokenizer and loader/config files enumerated by hash; checkpoint hash, canonical inference-profile hash and independent reload evidence. Release identity covers the complete profile, so different backends cannot overwrite a release sharing the same weights. Exact upstream export file inventory is a loader decision. |
| Cache/state: `artifacts/state/embeddings.sqlite`, `qwen.sqlite`, `judge.sqlite` | Respective cache owner → its callers | Completed vectors or full-payload provider records, identities/usage/status; query vectors have query-role inputs. No mutable membership lives in the embedding cache. |
| Update: `artifacts/updates/<job_id>/target.json`, `events.jsonl`, `journal.jsonl`, `workload.json`, `verification.json` | Update/verifier → publisher/status/experiment report | Target/base/profile/cache policy hashes; real/controlled labels; planned/completed operations; parity references and staged/published recovery state. |
| Staging: `artifacts/staging/<job_id>/` | Builders/snapshot owner → verifier/loader | Unpublished complete bundle under construction; it cannot be served as active. |
| S1: `artifacts/snapshots/<snapshot_id>/manifest.json`, `metadata.sqlite`, `fts.sqlite`, `vectors.npy`, `rows.jsonl`, `profiles.json` | Snapshot owner → pinned serving/evaluator/source viewer | Immutable revision/unit/occurrence membership/source maps and snapshot-local FTS; row→input/profile/vector map, all hashes and retained C1/E1 refs. “Complete” includes reachable original/text/model artifacts, not just vectors. |
| Active: `artifacts/state/active.json` | Single publisher → serving/startup recovery | Snapshot ID, manifest hash and activation generation. Must reference a validated fully available bundle; old request handles remain retained. |
| P1: `artifacts/runs/<run_id>/manifest.json`, `predictions.jsonl`, `attempts.jsonl`, `contexts/<payload_hash>.json` | Shared prediction store, driven by serving/collector → scorer/calibrator | Exact request/ranks/selected/sent contexts, profiles, answers/actions/citations, response identities, latency/usage/cache/retry/error state and code/dependency/hardware identity. Gold is excluded. |
| J1: `artifacts/judge/<judge_profile_hash>/manifest.json`, `human_labels.jsonl`, `disagreements.jsonl`, `calibration.json`, `audit.json` | Calibrator → judge/scorer | Blind-label provenance, rubric/prompt/profile hashes, actual provider identities, natural/controlled origin, per-dimension confusion and uncertainty, frozen/audit separation. |
| Reports: `artifacts/runs/<run_id>/judge_outputs.jsonl`; `reports/metrics.json`, `groups.json`, `costs.json`, `errors.jsonl` | Scorer → H09/packaging | Scores and all denominators/failures, paired group comparisons, separate seed variation, measured timing/usage and disclosed price assumptions. |

For P1 the item key is `(run_id, case_id, variant_id, track)`, with profile/seed
locked in its run manifest. Persist exact ordered outbound messages and a
source-span map before the request; preserve the original response and parser
errors afterwards. Cases with no generator record `actual_context = null`
and retain `selected_context`. Their evidence metric is explicitly over selected
context, while QA evidence/groundedness uses the sent context. Both are compared
under the locked reference budget, with generator reductions disclosed.

Interrupted provider calls are not automatically complete or free: distinguish
pending/in-flight/completed/failed/uncertain attempts. A crash after dispatch can
leave unknown provider usage or a duplicated request risk; the predeclared retry
policy must retain that uncertainty and count every observed attempt. API/direct
collection may retain separate copies of the same identified prediction, but
resume/dedup uses the immutable item/payload identity, never silent overwrite.

All cache layers require explicit identity:
embedding = full input + E5 profile; any future retrieval cache also adds S1 and
retrieval/context profiles; Qwen = ordered query/time/messages/context/source
metadata + provider/model/prompt/parser/settings; judge additionally includes
gold/rubric/prediction/sent-context hashes. Identical H0/H1 Qwen payloads may share
an output only if the frozen protocol permits it. Cache/replay latency never
stands in for a real API measurement.

## Build, release and request order

1. Ingest retains originals and durable crawl checkpoints. Corpus release locks
   normalized text, structure, hashes, source IDs and coverage before bulk data
   construction. A normalization fix creates a new release and affected-label review.
2. Freeze source groups, author only authorized source units, audit/accept cases
   and export public payloads separately from T1/G1. A controlled missing-evidence
   challenge specifies a full target and review of alternative sources;
   `indexing/build.py` materializes it rather than adding a separate snapshot writer.
3. H02 pilot data and H03 deterministic retrieval metrics enable the E5 pilot.
   H04 precedes main training. D1/D2 share initial weights, optimizer/loss/batch/
   steps/final checkpoint schedule; choose base queries uniformly for D2 and
   lock clean/variant/missing-type sampling. Three seeds per arm are planned.
   Mine only train queries and exclude known/held-out equivalent positives.
4. Each candidate weights hash re-encodes the whole corpus and receives its own
   cache/profile/index identity. Dev alone chooses the deployment checkpoint/seed
   under the predeclared clean/noisy rule. Fusion/metric sweeps may reuse vectors
   only when input and encoder profile are unchanged. Package E1 and verify reload.
5. Full/document/exact-reuse builds match target, chunker, weights and input dedup.
   Full encodes every unique target input with an explicitly cold workload;
   document mode reprocesses changed documents; exact mode encodes only verified
   misses from the declared initial cache scope. Encode/token/time accounting
   includes all three strategies, not only hits.
6. Build isolated metadata/membership/vectors and snapshot-local FTS/matrix
   projections. Keep encode/provider waits outside long SQLite write transactions.
   Resume matches job, target and profile hashes; partial cache entries are misses.
7. Independently rebuild the target from C1, then compare complete state, vectors,
   FTS and locked query ranks. Reference construction never consumes candidate/
   previous membership or updater plans. A shared fixed input→vector fixture may
   isolate software correctness, but cannot validate E5 inference or real speed.
8. Validate bundle completeness/hash/profile/source/model availability and load it.
   Release/benchmark activation also requires a matching parity report. Only then
   switch the active service reference. A prepublication failure leaves the old
   active handle unchanged. Publication is not a transaction across SQLite, files
   and model APIs.
9. For the initial single-process Linux target, same-filesystem staging/final
   rename plus a loaded-handle reference swap and durable active-record replacement
   are proposed. A single publisher prevents competing activation. Startup must
   validate active identity and reconcile journal state after a crash around the
   switch; never mark an invalid/incomplete bundle active. Exact fsync/recovery
   ordering must be settled before implementation.
10. Each request pins one loaded S1 handle, then shared search produces ranks and
    context. MCQ options do not affect retrieval. Answering checks Qwen limits via
    shared context code, saves the exact messages/context and invokes the fixed
    Qwen profile once (with bounded accounted retries). Citation/source lookup uses
    the pinned historical IDs, including after newer snapshots publish.
11. Save prediction/error before reading labels. Scoring joins authorized gold
    only to durable outputs; DeepSeek receives the actual saved context, blinded
    system names and locked rubric. Save unscored/errors and a review queue for
    suspect gold; do not let the judge “correct” source labels.
12. Humans label calibration outputs independently before machine verdicts;
    disclose initial agreement and adjudication. Tune only calibration, lock J1,
    then audit separate unused outputs. Model/provider/rubric changes require a
    new J1. Test cannot tune checkpoint, seed, agent prompt or rubric.

Old S1/C1/raw/E1 artifacts remain available while referenced by requests,
citations, benchmark manifests or recovery jobs. Deletion/GC is not implemented
or automatically authorized. Snapshot membership proves which content was used;
it does not prove every provision was legally in force.

## Task-to-file mapping

All paths in this table are relative to this scaffold root, not the source root.
Ranges include every task in the stated group exactly once. Cross-file entries
identify collaborators in the same task, not additional owners. Đạt retains
49 primary tasks, Lịch 45 and both 13; shared tasks still need an agreed implementer
and reviewer when real implementation begins. Plans/checklists are not progress evidence.

| Task IDs | Owner | Current scaffold files responsible for future work | Deliverable / constraint |
| --- | --- | --- | --- |
| PL-01, PL-02 | Đạt + Lịch | `config/corpus.toml`; `src/vietlegal_searchops/config.py` | Six-topic scope, seed/coverage and source policy; no legal-validity assumption. |
| PL-03 | Đạt + Lịch | `src/vietlegal_searchops/contracts.py`; `src/vietlegal_searchops/corpus/release.py` | Document/revision/unit/span and verification contract. |
| PL-04 | Đạt + Lịch | `src/vietlegal_searchops/datasets/release.py`; `src/vietlegal_searchops/datasets/splits.py` | Training, source-group, case and restricted-gold contracts. |
| PL-05 | Đạt + Lịch | `src/vietlegal_searchops/contracts.py`; `src/vietlegal_searchops/indexing/snapshots.py` | Canonical profile/hash and S1/E1 manifests. |
| PL-06 | Đạt + Lịch | `src/vietlegal_searchops/contracts.py`; `src/vietlegal_searchops/predictions.py`; `src/vietlegal_searchops/api.py` | Request/action/citation/context/error and prediction schemas. |
| PL-07 | Đạt + Lịch | `config/training.toml`; `config/retrieval.toml`; `config/evaluation.toml` | Freeze comparison, split, seed, selection, metric and budget policies. |
| PL-08 | Đạt + Lịch | `tests/fixtures/README.md`; `src/vietlegal_searchops/indexing/build.py` | Tiny fixture bundle and independent reference-builder plan. |
| EN-01 | Đạt + Lịch | `pyproject.toml`; `src/vietlegal_searchops/cli.py`; `artifacts/README.md` | Source layout, future entry point and artifact roots. |
| EN-02 | Đạt + Lịch | `pyproject.toml`; `src/vietlegal_searchops/embedding/e5.py` | Future dependency lock and measured runtime/hardware/reload checks. |
| EN-03 | Đạt + Lịch | `config/models.toml`; `.env.example`; `src/vietlegal_searchops/config.py` | Separate E5/Qwen/DeepSeek identities and role-specific validation. |
| EN-04 | Đạt + Lịch | `src/vietlegal_searchops/contracts.py`; `src/vietlegal_searchops/predictions.py` | Common event identity; crawl/update own job journals under that record convention. |
| EN-05 | Đạt + Lịch | `config/models.toml`; `config/evaluation.toml`; `src/vietlegal_searchops/agent/qwen.py`; `src/vietlegal_searchops/judge/deepseek.py` | Per-purpose API budgets, attempts and payload caches. |
| SR-01–08 | Đạt | `src/vietlegal_searchops/ingest/crawl.py`; `config/corpus.toml` | Discovery, download, metadata/raw archive, recovery, pilot/main coverage and error records. |
| DT-01, DT-02 | Đạt | `src/vietlegal_searchops/corpus/normalize.py` | Format extraction and versioned normalization. |
| DT-03–06 | Đạt | `src/vietlegal_searchops/corpus/release.py`; `src/vietlegal_searchops/contracts.py` | Structure/spans, duplicate mapping, dates/relations and validation. |
| DT-07 | Đạt | `src/vietlegal_searchops/corpus/normalize.py`; `src/vietlegal_searchops/corpus/release.py` | Pilot extraction review and corrected source/coverage release. |
| DT-08 | Đạt | `src/vietlegal_searchops/corpus/release.py` | Locked C1 manifest, coverage, statistics and limits. |
| DS-01, DS-02 | Lịch | `src/vietlegal_searchops/datasets/splits.py` | Equivalent-rule grouping, split freeze and overlap checks. |
| DS-03–05 | Lịch | `src/vietlegal_searchops/datasets/authoring.py`; `prompts/dataset_authoring.jinja` | Evidence-first Qwen drafts, training pairs and five benchmark groups. |
| DS-06 | Lịch | `src/vietlegal_searchops/datasets/authoring.py`; `src/vietlegal_searchops/indexing/build.py` | Reviewed challenge target specification; ordinary full builder materializes controlled snapshot. |
| DS-07 | Lịch | `src/vietlegal_searchops/datasets/release.py`; `src/vietlegal_searchops/datasets/authoring.py` | Human acceptance, conditions/exceptions/actions and source-written subset. |
| DS-08, DS-09 | Lịch | `src/vietlegal_searchops/datasets/authoring.py`; `src/vietlegal_searchops/datasets/splits.py` | Meaning-preserving variants and audited MCQ with inherited parent/group. |
| DS-10, DS-11 | Lịch | `src/vietlegal_searchops/datasets/release.py` | Stratified training/negative audit; separate T1, public cases, G1 and datasheets. |
| IX-01 | Đạt | `src/vietlegal_searchops/chunking/structure.py` | Legal chunking, full input serialization and source mapping. |
| IX-02 | Đạt | `src/vietlegal_searchops/embedding/e5.py` | E5 prefixes, tokens, pooling, normalization and vector checks. |
| IX-03 | Đạt | `src/vietlegal_searchops/embedding/cache.py` | Complete exact-input/profile embedding cache. |
| IX-04 | Đạt | `src/vietlegal_searchops/indexing/build.py` | Independent full target rebuild with explicit workload policy. |
| IX-05–07 | Đạt | `src/vietlegal_searchops/indexing/update.py`; `src/vietlegal_searchops/embedding/cache.py` | Document/exact modes, occurrence deltas, journal and resume. |
| IX-08 | Đạt | `src/vietlegal_searchops/indexing/snapshots.py` | Immutable staged bundle, validation, load and publication. |
| IX-09 | Đạt | `src/vietlegal_searchops/indexing/verify.py`; `src/vietlegal_searchops/cli.py` | Independent verify-update report and command. |
| IX-10 | Đạt | `tests/test_updates_and_snapshots.py`; `tests/test_encoder_and_training.py` | Update/cache edge cases and injected-failure recovery coverage. |
| RT-01–03 | Đạt | `src/vietlegal_searchops/retrieval/search.py` | Snapshot-local FTS, exact dense/query cache and RRF/ranking policy. |
| RT-04 | Đạt | `src/vietlegal_searchops/retrieval/context.py` | Rank-aware span selection, labels, budget and exact context. |
| RT-05 | Đạt | `src/vietlegal_searchops/retrieval/search.py`; `config/retrieval.toml` | Train/dev query rules with original query and protected identifiers. |
| RT-06 | Đạt | `src/vietlegal_searchops/indexing/snapshots.py` | Load, publish, pin and historical references. |
| RT-07 | Đạt | `src/vietlegal_searchops/cli.py`; `src/vietlegal_searchops/retrieval/search.py` | One shared B0/D0/D1/D2/H0/H1 search interface. |
| TR-01, TR-02 | Đạt | `src/vietlegal_searchops/training/train_e5.py`; `src/vietlegal_searchops/datasets/release.py` | Sampler/loss/collision control and train-only reviewed negatives. |
| TR-03–05 | Đạt | `src/vietlegal_searchops/training/train_e5.py`; `config/training.toml` | Pilot, locked schedules, main seeds and measured training artifacts. |
| TR-06 | Đạt | `src/vietlegal_searchops/training/select.py`; `src/vietlegal_searchops/indexing/build.py` | Fresh corpus encoding/index for every candidate weights hash. |
| TR-07 | Đạt | `src/vietlegal_searchops/training/select.py`; `src/vietlegal_searchops/evaluation/metrics.py` | Predeclared dev-only H1 checkpoint/seed selection. |
| TR-08 | Đạt | `src/vietlegal_searchops/embedding/e5.py`; `src/vietlegal_searchops/training/select.py` | E1 packaging and independent reload evidence. |
| QW-01, QW-04 | Lịch | `src/vietlegal_searchops/agent/qwen.py`; `config/models.toml` | Bounded provider calls, identity and complete-payload generation cache. |
| QW-02 | Lịch | `src/vietlegal_searchops/agent/answer.py`; `prompts/qwen_qa.jinja`; `prompts/qwen_mcq.jinja` | QA/MCQ action and citation behavior. |
| QW-03, QW-05 | Lịch | `src/vietlegal_searchops/agent/answer.py`; `src/vietlegal_searchops/predictions.py` | Shared search/context flow, exact payload log and visible output/citation errors. |
| EV-01 | Lịch | `src/vietlegal_searchops/evaluation/metrics.py` | Source-level Recall/nDCG and complete alternative evidence sets. |
| EV-02 | Lịch | `src/vietlegal_searchops/evaluation/runner.py`; `src/vietlegal_searchops/cli.py` | Locked gold-free retrieval collection through shared local/HTTP contract. |
| EV-03 | Lịch | `src/vietlegal_searchops/predictions.py`; `src/vietlegal_searchops/evaluation/runner.py` | Durable P1, run ledger, budgets and resume. |
| EV-04, EV-05 | Lịch | `src/vietlegal_searchops/evaluation/metrics.py`; `src/vietlegal_searchops/evaluation/score.py` | MCQ/citations/coverage, source-group pairing/bootstrap and seed reports. |
| EV-06 | Lịch | `tests/test_predictions_and_evaluation.py`; `tests/test_retrieval_and_context.py` | Known-rank/evidence/error fixtures before training selection. |
| EV-07, EV-08 | Lịch | `src/vietlegal_searchops/evaluation/runner.py`; `src/vietlegal_searchops/evaluation/score.py` | Separate collection/scoring tracks and layered usage/cost/failure reports. |
| JG-01 | Lịch | `rubrics/qa.toml`; `prompts/deepseek_judge.jinja` | Five case-aware dimensions with explicit scoring/review rules. |
| JG-02, JG-03 | Lịch | `src/vietlegal_searchops/judge/deepseek.py`; `config/models.toml` | Verified provider identity, schema/parser/retry and cache. |
| JG-04–07 | Lịch; both label | `src/vietlegal_searchops/judge/calibrate.py`; `rubrics/qa.toml` | Blind packets, independent labels, disagreement, locked J1 and separate audit. |
| AP-01, AP-02 | Lịch | `src/vietlegal_searchops/api.py`; `src/vietlegal_searchops/agent/answer.py` | Shared /search, /answer and historical /source routes. |
| AP-03, AP-04 | Lịch | `web/index.html`; `src/vietlegal_searchops/api.py` | Query/source viewer and persisted update status/workload/errors. |
| AP-05, AP-06 | Lịch | `src/vietlegal_searchops/api.py`; `tests/test_api_and_judge.py` | Request/artifact/profile validation; offline smoke now planned, later authorized live smoke separate. |
| EX-01 | Lịch | `src/vietlegal_searchops/evaluation/runner.py`; `config/evaluation.toml` | Pilot case/run budget and measured effort/resource records. |
| EX-02 | Lịch | `src/vietlegal_searchops/config.py`; `config/evaluation.toml` | Freeze manifests, profiles, subset, budgets and failure policy. |
| EX-03, EX-04 | Lịch | `src/vietlegal_searchops/evaluation/runner.py`; `src/vietlegal_searchops/evaluation/metrics.py` | Locked per-seed retrieval test and eligible MCQ collection/scoring. |
| EX-05 | Lịch | `src/vietlegal_searchops/evaluation/runner.py`; `src/vietlegal_searchops/evaluation/score.py` | Preselected H0/H1 QA subset, fixed Qwen/J1 and budgeted attempts. |
| EX-06 | Lịch | `src/vietlegal_searchops/evaluation/runner.py`; `src/vietlegal_searchops/evaluation/score.py` | Warm-up/concurrency, p50/p95, cold load, resources and live/replay separation. |
| EX-07 | Lịch | `src/vietlegal_searchops/evaluation/runner.py`; `src/vietlegal_searchops/indexing/verify.py` | Matched full/document/exact workload, at least three planned repetitions, failures/resume/concurrent switch. |
| EX-08 | Lịch | `src/vietlegal_searchops/evaluation/metrics.py`; `src/vietlegal_searchops/evaluation/score.py` | Grouped uncertainty and source/gold/retrieval/context/generation/judge errors, including negative findings. |
| PK-01 | Đạt | `deploy/Dockerfile`; `deploy/compose.yaml` | CPU E5 API/demo image and explicit immutable artifact mounts. |
| PK-02 | Đạt | `deploy/ci.yaml`; `tests/__init__.py`; `tests/fixtures/README.md` | Offline CI integration and future runnable test assets. |
| PK-03 | Đạt | `deploy/compose.yaml`; `src/vietlegal_searchops/embedding/e5.py`; `src/vietlegal_searchops/api.py` | Later real CPU reload/search/RAM/latency/missing-artifact acceptance. |
| PK-04 | Đạt | `ARCHITECTURE.md`; `pyproject.toml`; `src/vietlegal_searchops/cli.py` | Required future implementation README, environment lock and reproducible commands documented below. |
| PK-05–08 | Đạt; Lịch supplies H09 | `ARCHITECTURE.md`; `src/vietlegal_searchops/evaluation/score.py`; `artifacts/README.md` | Future technical report/cards/share manifest/demo and task-to-evidence acceptance register; no results created now. |

PK-04–08 include later runnable instructions, reports/cards/video and evidence.
This scaffold records where those outputs belong; it does not claim to deliver
them now. All optional OP-01–05 remain deferred and unassigned.

## Handoff-to-file mapping and scheduling

All paths in this table are relative to this scaffold root. Acceptance artifacts
are the future versioned records defined above, not files delivered by this task.

| Handoff | Producer → consumer | Owning files and acceptance artifact | Scheduling condition |
| --- | --- | --- | --- |
| H01 | Đạt → Lịch | `src/vietlegal_searchops/ingest/crawl.py`, `src/vietlegal_searchops/corpus/release.py` → C1 with raw/text hashes, units/spans, stable schema and source mapping | Seed release precedes bulk authoring; do not wait for 20–50 documents. |
| H02 | Lịch → Đạt | `src/vietlegal_searchops/datasets/splits.py`, `src/vietlegal_searchops/datasets/release.py` → separate pilot T1, approximately 300–500 reviewed train queries plus grouped dev qrels | Before TR-03; distinct identity from H04. |
| H03 | Lịch → Đạt | `src/vietlegal_searchops/evaluation/runner.py`, `src/vietlegal_searchops/evaluation/metrics.py`, `tests/test_predictions_and_evaluation.py`, `src/vietlegal_searchops/cli.py` → deterministic ranks/metric fixtures and shared D0 collection | Implement EV-01/02/06 before selecting training configurations; no Qwen/judge prerequisite. |
| H04 | Lịch → Đạt | `src/vietlegal_searchops/datasets/release.py` → main T1 with groups/variants/manifests/dev qrels and accepted audit records | Before TR-04/05; held-out calibration/test gold stays with Lịch. |
| H05 | Đạt → Lịch | `src/vietlegal_searchops/retrieval/search.py`, `src/vietlegal_searchops/retrieval/context.py`, `src/vietlegal_searchops/indexing/snapshots.py` → D0-capable shared ranks/context/source/snapshot/profile interface | Agent/API integration starts before fine-tuning finishes. |
| H06 | Đạt → Lịch | `src/vietlegal_searchops/training/select.py`, `src/vietlegal_searchops/embedding/e5.py`, `src/vietlegal_searchops/indexing/build.py`, `src/vietlegal_searchops/indexing/snapshots.py` → E1 + matching S1 + independent reload record | Before H0/H1 benchmark; every evaluated checkpoint has its own corpus encoding. |
| H07 | Đạt → Lịch | `src/vietlegal_searchops/indexing/update.py`, `src/vietlegal_searchops/indexing/verify.py`, `src/vietlegal_searchops/indexing/build.py`, `src/vietlegal_searchops/cli.py` → job/event/cache-policy bundle, parity report and failure/resume fixtures | Before EX-07; distinguish real and controlled changes. |
| H08 | Lịch → Đạt | `src/vietlegal_searchops/judge/calibrate.py`, `src/vietlegal_searchops/predictions.py`, `rubrics/qa.toml` → source/rubric/output blind packet and independent human labels | Prepare before verdict reveal; both label, then compare/calibrate and separately audit. |
| H09 | Lịch → Đạt | `src/vietlegal_searchops/evaluation/score.py`, `src/vietlegal_searchops/evaluation/metrics.py`, `src/vietlegal_searchops/predictions.py`, `src/vietlegal_searchops/judge/deepseek.py` → P1, ranks/judge JSON/usage/failures/config hashes, uncertainty and limits | Before PK-05/07/08; packaging consumes recorded evidence. |

The artifact schedule is H01 → H02 + H03 → pilot → H04 → main training → H06.
H05 uses pretrained D0 early. H07 depends on stable source/profile contracts, not
on H09. H08 can use dev/calibration saved outputs before the final test freeze.
H09 follows locked prediction/scoring runs. These choices remove data/evaluator/
training circular waits without changing who owns each task.

## Workflow node coverage

IDs below omit the shared `workflow-node-` prefix. Paths are relative to the
source root. Repeated files deliberately own multiple stages/artifact nodes;
they do not indicate parallel implementations.

| Panel | Node ID | Owning source file |
| --- | --- | --- |
| 00 | `overview-corpus` | `corpus/release.py` |
| 00 | `overview-build` | `indexing/snapshots.py` |
| 00 | `overview-serving` | `api.py` |
| 00 | `overview-training` | `training/select.py` |
| 00 | `overview-predictions` | `predictions.py` |
| 00 | `overview-viewer` | `api.py` |
| 00 | `overview-gold` | `datasets/release.py` |
| 00 | `overview-evaluation` | `evaluation/score.py` |
| 01 | `sources` | `ingest/crawl.py` |
| 01 | `ingestion` | `ingest/crawl.py` |
| 01 | `normalization` | `corpus/normalize.py` |
| 01 | `corpus-release` | `corpus/release.py` |
| 01 | `raw-artifacts` | `ingest/crawl.py` |
| 01 | `chunker` | `chunking/structure.py` |
| 01 | `chunk-set` | `chunking/structure.py` |
| 02 | `training-source` | `corpus/release.py` |
| 02 | `splitter` | `datasets/splits.py` |
| 02 | `authoring` | `datasets/authoring.py` |
| 02 | `split-release` | `datasets/release.py` |
| 02 | `fine-tuning` | `training/train_e5.py` |
| 02 | `dev-selector` | `training/select.py` |
| 02 | `encoder-release` | `embedding/e5.py` |
| 03 | `build-input` | `indexing/update.py` |
| 03 | `reuse` | `embedding/cache.py` |
| 03 | `encode-misses` | `embedding/e5.py` |
| 03 | `staged-bundle` | `indexing/snapshots.py` |
| 03 | `full-reference` | `indexing/build.py` |
| 03 | `verify-update` | `indexing/verify.py` |
| 03 | `validation` | `indexing/snapshots.py` |
| 03 | `publish` | `indexing/snapshots.py` |
| 03 | `published-snapshot` | `indexing/snapshots.py` |
| 04 | `query` | `api.py` |
| 04 | `pin` | `indexing/snapshots.py` |
| 04 | `bm25` | `retrieval/search.py` |
| 04 | `dense` | `retrieval/search.py` |
| 04 | `rrf` | `retrieval/search.py` |
| 04 | `context` | `retrieval/context.py` |
| 04 | `qwen` | `agent/qwen.py` |
| 04 | `response` | `agent/answer.py` |
| 04 | `viewer` | `api.py` |
| 05 | `eval-runner` | `evaluation/runner.py` |
| 05 | `eval-api` | `api.py` |
| 05 | `prediction-store` | `predictions.py` |
| 05 | `metrics` | `evaluation/metrics.py` |
| 05 | `gold-store` | `datasets/release.py` |
| 05 | `human-calibration` | `judge/calibrate.py` |
| 05 | `deepseek` | `judge/deepseek.py` |
| 05 | `reports` | `evaluation/score.py` |

The overview reuses the detailed owners. Artifact nodes retain the aliases and
access rules defined above. External source/provider nodes point to their
concrete ingestion/provider adapter. All 48 nodes across six panels are mapped.

## Configuration, tests and deployment assets

The comment-only files name required inputs; they are not usable configurations.
No credentials, provider endpoints, model weights or dependency lock are supplied.

| Existing asset | Required future content / gate |
| --- | --- |
| `pyproject.toml` | Agreed Python version, src packaging, CLI entry point, package data (prompts/rubric/web), actual dependencies and a pinned lockfile. Select the lock format before EN-02, then record code/dependency/runtime identity. |
| `.env.example` | Names for separate Qwen/DeepSeek base URL/model/key and artifact root; document role-scoped environment requirements. Keys must remain environment-only. Local retrieval needs no API key. |
| `config/corpus.toml` | Topic/coverage, allowed origins/attachments, fetch/recovery, parser/normalization/span/chunk profiles, equivalence/split/review policy. |
| `config/models.toml` | E5 weights/tokenizer/backend/device/batch/dtype; Qwen and DeepSeek requested/response/backend IDs, prompts/parsers, thinking/sampling/output, timeouts/budgets/cache. |
| `config/training.toml` | Explicit new pilot/main T1 paths/hashes, train-only mining, equal D1/D2 steps/loss/batch, seed/sampler policy, fixed checkpoint schedule, dev selection and corpus re-encoding. |
| `config/retrieval.toml` | Snapshot/profile identities, branch/query/MATCH/rank/tie-break rules, RRF/top-k, span/context serialization and both tokenizer limits; dev defaults are proposals. |
| `config/updates.toml` | Matched targets/cache starting state, full/document/exact modes, job recovery, vector/tolerance/query suite, validation/parity gate and publication/retention policy. |
| `config/evaluation.toml` | Separate collector/scorer/calibrator roles, public versus restricted paths, eligible/completed/scored/failure rules, QA subset, budgets, source-group bootstrap, warm-up/concurrency/repetitions and latency/cost accounting. |
| Four `prompts/*.jinja` and `rubrics/qa.toml` | Real versioned templates and five-dimension group-aware rubric; freeze/hashes with actual model profile after authorized pilot/calibration. |
| `tests/fixtures/README.md` and six `tests/test_*.py` | Reviewed small originals, source maps/groups/cases/gold, vector/rank/event fixtures, fake tokenizer/provider data and expected results; then implement genuine offline tests. |
| `deploy/Dockerfile` | Pin runtime/base/lock, copy installed package and assets, CPU E5 path, non-downloading startup and HTTP entry point. No GPU Qwen/DeepSeek serving is planned. |
| `deploy/compose.yaml` | Initial one-process API/demo/single publisher, explicit read-only raw/C1/E1/S1 mounts, distinct writable request/cache journals, provider environment and readiness/resource settings. Never mount G1 into serving. |
| `deploy/ci.yaml` | Future CI job using implemented offline tests and fixture vectors/clients, with no network/model/key prerequisite. This file is not an active root workflow; repository CI integration is later work. |
| `web/index.html` | Simple accessible query/results/action/citation/historical-source viewer and persisted update status. Display actual snapshot/checkpoint, honest loading/errors and recorded workload. |

PK-04–08 additionally require an implementation README with tested commands,
dependency lock and environment/hardware notes; dataset/model cards, provenance/
sharing inventory; training/dev/checkpoint reload evidence; locked benchmark
runs; calibration/update reports; a quality/cost report; a demo video; and a
task→code/config→run/report→person acceptance register. Proposed future output
names are `artifacts/delivery/<release_id>/README.md`, `dataset_card.md`,
`model_card.md`, `provenance.json`, `technical_report.md`, `demo.mp4` and
`acceptance.json`. They are not created by this task. Existing proposal, paper
and workflow documents remain intact.

## Planned validation coverage

Each listed Python test file contains only its plan; there are no collected
test functions, fabricated assertions or claimed passing runtime tests.

| Test file under `tests/` | Critical checks and expected evidence |
| --- | --- |
| `test_sources_and_splits.py` | Allowlisted origin/attachment tracing, fetch idempotency/resume and preserved bytes; actual-used-format extraction; NFC/code-point round trips; tree/hash/date/duplicate/amendment checks; reviewed coverage; pre-authoring group freeze/near-duplicate/variant/MCQ inheritance; accepted/rejected exports and no held-out labels in T1/inference payloads. |
| `test_encoder_and_training.py` | Full prefix/breadcrumb/special-token budgets; query/passage prefix once; finite shape/norm/dtype; incomplete/cache-profile/breadcrumb/weights/backend misses; metadata-only hits; duplicate/equivalent-positive batches and train-only negatives; uniform base-query/D1-D2 schedules/dev-only seed selection; full re-encoding for each new checkpoint. Offline fixtures do not load real E5. |
| `test_updates_and_snapshots.py` | Full/document/exact matched target/cache policies; no-edit, metadata-only, add/edit/delete and shared-vector removal; journal/partial-cache recovery and reruns; independent reference detects corrupted candidate membership/FTS/vectors; failure before activation preserves active handle; crash recovery around activation; old/new concurrent pins and historical source retention. |
| `test_retrieval_and_context.py` | FTS tokenizer/MATCH escaping/score direction, dense/RRF ranks/ties/limits; profile mismatch rejection; ranking-unit dedup versus complementary-span preservation; serialized label/metadata budget; actual retained-span reductions; gold/options exclusion; same search/context through CLI, HTTP and collector. |
| `test_predictions_and_evaluation.py` | Durable context before dispatch, output/error before label join, hash-bound replay and matching-run resume; uncertain attempts and budget accounting; known Recall/nDCG and alternative complete evidence sets, empty/ineligible cases, MCQ/citations/coverage; paired variants and grouped bootstrap versus separate seed variation; actual/replay/retry cost and failures retained. |
| `test_api_and_judge.py` | HTTP/answer/source/status contracts and exact cited revision/span, missing artifacts/invalid profiles, no benchmark gold in serving; mocked Qwen parsing/citation/identity errors, tokenizer-limit context logging; DeepSeek schema/retry/cache/unscored/identity changes; blind human labels, natural/controlled provenance, confusion/zero-denominator policy and separate audit. |

Known-rank fixture targets can use paper 09's example:
relevant sources `{a,b}`, ranks `[a,z,b]` give Recall@3 = 1 and
nDCG@3 ≈ 0.91972; `[{a,b},{c}]` succeeds only with both a+b or all of c.
These are constructed expectations, not results from this system. Tests must
also check sent text and revision/span coverage, not just matching source IDs.

Later evidence must stay distinct: (1) offline fixed-vector/software checks,
(2) explicitly authorized model reload/inference/provider/deployment smoke,
(3) locked comparable benchmarks. The scaffold performs only static review.
Real throughput/GPU hours/costs, provider availability and legal correctness
cannot be inferred from these placeholders.

## Remaining architectural assumptions

| Assumption / source | Decision still required and affected interface |
| --- | --- |
| A1, PL-03–06 | Review canonical ID derivation, schema versions, exact request/error fields, provisional action enum and /source spelling; absolute revision offsets are chosen here. No alternate source routes or schema variants are scaffolded. |
| A2, IX-08/RT-06 | Approve concrete S1/C1/E1 serialization, canonical hashing and export inventory. Set transaction/rename/fsync/startup-reconciliation ordering and single-process activation guarantees. A future multiworker deployment needs coordinated handle generations; it is outside this scaffold. |
| A3, RT-02 | Start with NumPy exact search for the small corpus; FAISS Flat remains a pilot-driven alternative. Freeze backend/dtype/tolerance/ties before comparable runs; no backend abstraction or ANN stage is added. |
| A4, QW-01/JG-02 | Qwen3.8-27B and DeepSeek V4 Flash are requested roles from project sources, not verified available endpoints. Configure and verify requested/response/backend identity on the actual provider; disclosed alias drift or unavailable revision may require a new profile/calibration. No live provider check was authorized here. |
| A5, IX-09/EX-07 | Full-rebuild parity gates release/benchmark audits; set continuous production cadence, audit cost policy and referenced-history retention. No automatic deletion/GC is planned. |
| DS-01/02/06/10 | Human equivalence/near-duplicate thresholds, train-only negative authorization, alternative-source review for missing-evidence cases, audit sizes and reviewer expertise remain empirical decisions. Snapshot/time metadata alone cannot certify legal validity. |
| TR-03/04/07, PL-07 | Freeze exact training steps/loss/negative policy, D2 missing-variant rule, dev clean/noisy weights/guardrail and deployment-seed tie-break after pilot. Three seeds and equal schedules are requirements of the main plan; improvement is not guaranteed. |
| RT-03/04, QW-03 | Finalize chunk→source ranking mapping, overlap merge/truncation, source labels and Qwen tokenizer/transport-limit accounting. A smaller actual QA context must be recorded with a frozen profile; there can be no hidden API/evaluator budget divergence. |
| EV-03/05/08, JG-06 | Freeze item terminal/uncertain-call policy, evidence eligibility/failure denominators, bootstrap estimand/RNG/count, ordinal/zero-denominator scoring and price snapshots. Provider idempotency/usage after a lost response is not assumed. |
| EN-02, PK-01–03 | Select Python/lock/base image, actual document readers, source fixture redistribution conditions and target CPU/RAM/disk. Container packaging must include prompt/rubric/web assets and every retained artifact needed for citations. |

Oracle gold-evidence diagnostics mentioned in paper 10 are a separately labeled
experimental condition, never a deployed retrieval option. They are deferred here
to preserve the gold-free collector/answer contract; enabling them later requires
an explicit isolated protocol and prelocked budget/subset. Multi-turn agents,
automatic legal consolidation and optional expansion work remain outside scope.

## Static scaffold review

The review checks the actual inventory against this tree and the dependency
allowlist, all Python ASTs for exactly one string-expression module docstring,
package initializers, planned interface/dependency metadata, all 107 core task IDs,
H01–H09, both workflow node inventories, renamed-path coverage and source preservation.
It checks documentation consistency rather than executable system behavior.

Static checks completed with Python's standard library, without importing the
scaffold or executing its planned interfaces:

- **48/48 Python ASTs** contain exactly one module docstring and no other source;
  all have purpose, inputs/outputs/artifacts, interfaces, dependencies, invariants
  and task/paper trace fields. All 13 package initializers are present and inert.
- **29 leaf modules / 118 planned dependency edges** resolve to real source files,
  agree between docstrings and the dependency table, and form an acyclic graph.
  Serving cannot transitively reach dataset/gold/scoring/training/judge modules.
- **71 files** match the exact tree, including directory inventory. Task and handoff
  references resolve to actual files. All **107 core tasks** are assigned once;
  all **nine handoffs** are represented without the H02/H03/H05 scheduling waits.
- Both workflow files have matching semantic text and **48 nodes / six panels**;
  every node has a concrete owner. The reconciliation table disposes of proposed
  filenames and separates artifact paths from source paths.
- All configuration/deployment/web/prompt placeholders contain only native comments;
  all TOML placeholders parse as empty documents. The six test modules are plans,
  not runnable test implementations.
- SHA-256 comparison confirms all **145 pre-existing files** unchanged, including
  the original proposal, ownership plan, every paper section and all workflows.
  All **68 new files** are inside `vietlegal_searchops/`; no files were removed.

No dependencies were installed, provider calls made, models loaded/trained, indexes
built or deployments attempted. No runtime tests or system-quality claims are made.
The assumptions above remain future design/validation work.
