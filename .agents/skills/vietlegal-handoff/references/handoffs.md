# Ownership and handoff map

[ARCHITECTURE.md](../../../../ARCHITECTURE.md#task-to-file-mapping) records the
107 tasks, primary owners, file mappings and artifact contracts. Its
[handoff mapping](../../../../ARCHITECTURE.md#handoff-to-file-mapping-and-scheduling)
and the rules below define the shared acceptance workflow. Use recorded identities
and results when accepting a handoff; the table is not a completion ledger.

## Primary owners

| Owner | Task prefixes | Responsibility |
| --- | --- | --- |
| Dat (Đạt) | SR, DT, IX, RT, TR, PK | Crawl/corpus, embeddings/index/update, retrieval, E5 training and final packaging |
| Lich (Lịch) | DS, QW, EV, JG, AP, EX | Datasets, generator, evaluator, judge/calibration, API/UI and experiment execution |
| Shared | PL, EN | Scope/schema/protocol and infrastructure; name one implementer and one reviewer per task |

Assisting an owner does not transfer the task. Reallocation needs an explicit
team decision recorded against the task and deliverable. Task counts are not
effort estimates. Keep optional OP work outside the core unless selected.

## H01-H09 acceptance

| ID | Direction | Deliverable and acceptance conditions |
| --- | --- | --- |
| H01 | Dat -> Lich | Seed corpus C1 with document/revision/unit IDs, locked text/hashes, absolute spans, source mapping and stable schema; deliver before bulk authoring |
| H02 | Lich -> Dat | Pilot train/dev release, approximately 300-500 reviewed train queries plus group-separated dev qrels; explicit identity distinct from H04 |
| H03 | Lich -> Dat | Minimal retrieval evaluator and independent known-rank/metric fixtures, EV-01/02/06; usable before training configuration selection without Qwen/judge |
| H04 | Lich -> Dat | Main train/dev release with groups, variants, qrels, manifests and review provenance; no held-out calibration/test gold for tuning |
| H05 | Dat -> Lich | D0-capable shared search/context interface, ranks/source maps, pinned snapshot/profile and deterministic selected context; fixture and applicable checks |
| H06 | Dat -> Lich | Packaged encoder E1, matching snapshot/index S1, weights/tokenizer/inference profile hashes and independent reload evidence |
| H07 | Dat -> Lich | Updater/resume/verify-update entrypoints, target/cache policy, labelled event fixtures, workload and independent parity report; distinguish real/controlled changes |
| H08 | Lich -> Dat | Blind source/output/rubric packet for independent human labels before judge reveal; preserve label provenance and calibration/audit separation |
| H09 | Lich -> Dat | Saved predictions/ranks, metrics, judge outputs, usage/retries/failures, config/profile hashes, uncertainty and limits for final packaging |

Data sizes are planning targets, not evidence that data exists. Follow the
current locked protocol if an authorized pilot changes them.

## Remove circular waits

H01 enables H02/H03 and pilot; H04 precedes main training and H06. H05 uses D0
early, before fine-tuning finishes. H07 requires stable source/profile contracts,
not completed QA evaluation. H08 can use saved dev/calibration outputs before
final test freeze. H09 follows frozen prediction/scoring runs.

H03's metric implementation and known-rank fixtures can start before H01 or H05;
only integration with the real corpus/search depends on those deliveries. The
schedule expresses real-artifact dependencies, not a ban on starting fixture work.

Dat can develop parsing/indexing with archived sources and fixed vectors; Lich
can develop metrics with known ranks and API/agent code with agreed fixtures.
Integration replaces fixtures through the same interface with identified real
artifacts, rather than bypassing acceptance conditions.
