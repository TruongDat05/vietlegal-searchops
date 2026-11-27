# VietLegal SearchOps — proposed workflow

The overview and five detail panels were derived from the original proposal, ownership/handoff plan and paper sections 01–12 plus appendices. The planning documents remain local under ignored `docs/`; the original paper package remains external. [ARCHITECTURE.md](ARCHITECTURE.md) records the shared contracts, scaffold, module mapping and design decisions without requiring those local sources in a clone. This is a design proposal, with no implementation or measured-result claims. C1/C2/T1/E1/S1/P1/G1 identify shared artifacts, independently of experiment IDs D1/D2/H0/H1.

Built with the [diagram-design skill](https://github.com/cathrynlavery/diagram-design/blob/main/skills/diagram-design/SKILL.md), using its architecture, semantic-pattern, style, layout, connector, output and export references. No specialized semantic pattern applies to the whole topology.

## Design and editing

The light palette comes from `project.html`: paper `#F8FAFC`, ink `#0F172A`, muted `#475569`, artifact surface `#F1F5F9`, rules `#CBD5E1`, accent `#2563EB`, tint `#EFF6FF`, API link `#1D4ED8`. These explicitly replace the skill defaults. Each panel has at most nine nodes, twelve orthogonal connectors and one focal node.

`workflow.html` contains the editable native SVG and is the source of truth; `workflow.svg` is exported from it. Edit XML text/geometry or use a vector editor; there is no drag-and-drop browser editor. Both files work without scripts, external assets or network fonts. Instrument Serif/Geist/Geist Mono stacks fall back to installed fonts here, so appearance can vary across machines. HTML uses a local horizontal scroller and print CSS.

## Proposed module mapping [A1]

Paths are relative to proposed `src/vietlegal_searchops/`. This table preserves the original workflow proposal; the current docstring-only modules and consolidated paths are reconciled in [ARCHITECTURE.md](ARCHITECTURE.md#workflow-reconciliation-and-responsibility-ownership). Artifact filenames/layout remain proposals [A2].

| Boundary | Proposed modules | Input → output | Owner / tasks |
| --- | --- | --- | --- |
| Sources | `ingest/discovery.py`, `fetch.py` | Allowlisted pages/attachments → original bytes, hashes, URLs, manifest and crawl checkpoints | Dat / SR-01–08 |
| Corpus | `corpus/normalize.py`, `structure.py`, `release.py` | Raw files → **C1** revisions, normalized text, source units/spans, dates/status and source mapping | Dat / DT-01–08 |
| Chunks | `chunking/structure.py`, `serialize.py` | C1 + chunk profile → **C2** occurrences, breadcrumbs, spans and complete encoder inputs | Dat / IX-01 |
| Datasets | `datasets/groups.py`, `splits.py`, `authoring.py`, `audit.py` | C1 → group splits, **T1** train/dev pairs/qrels and separate **G1** held-out gold/cases | Lich / DS-01–11 |
| Training | `training/train_e5.py`, `negatives.py`, `select.py` | T1 + pretrained E5 → D1/D2 candidates; dev evaluation → **E1** weights/tokenizer/profile manifest | Dat / TR-01–08 |
| Embeddings | `embedding/profile.py`, `e5.py`, `cache.py` | Full input + E1/inference profile → validated vectors and durable SQLite cache | Dat / IX-02–03 |
| Update/checks | `indexing/update.py`, `journal.py`, `full_build.py`; `verification/update.py` | Target sources/profile + events → resumable candidate; independent reference → parity report | Dat / IX-04–10 |
| Snapshots | `snapshots/build.py`, `validate.py`, `loader.py`, `registry.py` | Metadata/membership/vectors → **S1** bundle; validate/load → atomic publication and request pin | Dat / IX-08, RT-06 |
| Retrieval | `retrieval/lexical.py`, `dense.py`, `fusion.py`, `context.py` | Query + pinned S1 → BM25/dense ranks → RRF → actual serialized context | Dat / RT-01–07 |
| Agent/application | `agent/qwen.py`, `answer.py`, `validate.py`; `api/search.py`, `answer.py`, `sources.py`; `ui/` | Shared search/context → answer/action/citations and historical source viewer | Lich / QW-01–05, AP-01–06 |
| Evaluation/Judge | `evaluation/runner.py`, `ledger.py`, `run_store.py`, `retrieval.py`, `metrics.py`, `reports.py`; `judge/calibrate.py`, `deepseek.py`, `schema.py`, `rubrics/` | Save **P1** first; P1 + G1 → metrics, calibrated **J1** profile, judge JSON and reports | Lich / EV-01–08, JG-01–07; both label calibration |

## Proposed interfaces [A1]

CLI, API and evaluator use the same search core. These concrete field/method proposals need agreement in PL-03–PL-06.

| Interface | Inputs | Outputs |
| --- | --- | --- |
| `POST /search` | `query`, optional `snapshot_id`/`as_of`, retrieval profile/top-k | Request/snapshot/checkpoint/profile identity, ranked occurrence/source references, timing |
| `POST /answer` | Question, snapshot/time, `mode`; options only for MCQ | Search identity/ranks, answer/action/citations, actual context, provider/model identity, usage/errors |
| `GET /source` | Snapshot/revision/unit IDs; optional `[start,end)` | Hash-locked text/span, locator, original-file/source references |
| `verify-update` | Target, candidate, independent reference, query suite | Revision/metadata/membership/vector/FTS/rank differences under locked tolerance/tie-break |

P1 persists run/case IDs, original request, ranks, exact ordered context **after** serialization/truncation, response, profile hashes, usage/latency and failures. Judge replays that context rather than reconstructing it from the current corpus. Source lookup never silently substitutes a newer revision.

## Architecture invariants

- C1 retains originals and hash-locked normalized text. Gold/citations use source spans with Unicode code-point offsets `[start,end)`. Missing validity metadata stays `unverified`; snapshots do not establish legal validity.
- Freeze source groups before authoring; variants/MCQ/QA inherit them. Use train-only supervision/mining and dev-only selection. Corpus text may cover every split: query generalization on a known corpus. Held-out gold stays outside query/context/generation.
- D1/D2 match steps/loss/batch and fixed checkpoint schedules; three seeds/arm are planned. Dev selects deployment checkpoint/seed; changed weights require corpus re-encoding. E5: query/passage prefixes, ≤512 tokens, masked mean pooling, 384-dimensional L2 vectors. FTS5: `unicode61 remove_diacritics 0`.
- Reuse requires full-input and canonical-profile hashes, verified completion, and matching checkpoint/tokenizer/preprocessing/pooling/normalization/inference settings. Occurrence membership stays separate from shared vectors.
- S1 contains manifest, immutable metadata/membership/source mapping, snapshot-local FTS, matrix/row map and profiles. Stage/load outside long write transactions, validate, then switch the service reference. Failures preserve the active snapshot; resume uses verified journal/cache entries. Retain sources for old pins/citations.
- Humans label calibration outputs before machine verdicts; compare/tune, lock J1, then audit separate outputs. Test never tunes models/prompts/rubrics. Report five QA dimensions, complete evidence-set coverage in actual context, completion/scored coverage, source-group uncertainty, seed variation, costs and failures. Fixed-vector checks do not establish model accuracy/speed.

## Dependencies and assumptions

H01 corpus → H02 pilot data + **H03 deterministic evaluator before checkpoint selection** → H04 training release → H06 checkpoint/index. H05 integrates D0 search before fine-tuning; H07 precedes update experiments. H08 supports blind calibration; H09 supplies final saved outputs. These are dependencies, not completed handoffs.

- **A1:** Package paths, API methods/fields, source-route spelling and action enum are proposed.
- **A2:** Bundle filenames/serialization and atomic-reference primitive are open; publication is not a transaction spanning SQLite, files and model APIs.
- **A3:** Choose NumPy exact search or FAISS Flat after the pilot; no additional ANN stage is implied.
- **A4:** Verify/pin Qwen and DeepSeek provider, requested/response model and available backend revision before runs. Alias names do not establish weights identity. Provider/rubric changes require a new calibrated Judge profile. No live model test was performed.
- **A5:** Full-rebuild parity is proposed as a release/benchmark audit gate. Production audit frequency and history retention remain open. Full/document/exact-reuse comparisons must match target, chunker, weights, dedup and starting cache policy.

## Validation

Upstream `self_check.py --offline` passes on HTML; `verify_geometry.py` passes on HTML and SVG; `export_svg.py --system-fonts` produced the XML-valid export. Panel budgets and unique IDs were checked. Native 1× librsvg/Cairo renders of every panel and legend were visually inspected; overflowing copy and isolated artifact-ID title wraps were fixed.

Chromium startup is blocked by sandbox process/socket restrictions, so this is an SVG render review, not a browser interaction test. All 142 pre-existing workspace files were verified unchanged. Only the three requested deliverables were added here; preview/checker files remain temporary.
