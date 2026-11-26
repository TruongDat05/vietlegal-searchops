"""Purpose: Plan source-provenance, corpus and dataset-release checks.
Inputs/outputs/artifacts: Archived-format/source/group fixtures will yield parser/span/hash, allowlist, leakage, review and release validation results; fixture assets are specified in fixtures/README.md.
Interfaces: Planned tests for source_roundtrip, immutable_revisions, split_inheritance and gold_free_exports.
Dependencies: ingest.crawl, corpus.normalize, corpus.release, datasets.splits, datasets.authoring, datasets.release; offline pytest and fixtures.
Invariants: Protect originals and absolute code-point slices; related revisions/variants/MCQ stay grouped and corpus visibility never authorizes held-out supervision.
Trace: SR-01–08, DT-01–08, DS-01–11, PL-08; paper 02/06.
"""
