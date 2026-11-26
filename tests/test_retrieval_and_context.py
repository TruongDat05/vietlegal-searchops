"""Purpose: Plan shared retrieval, source-level ranking and source-preserving context validation.
Inputs/outputs/artifacts: Known FTS/dense ranks, equivalent spans and budget profiles will yield deterministic branch/RRF/context and CLI/HTTP/collector equivalence evidence.
Interfaces: Planned tests for fts_order, rank_ties, complementary_spans, budget_serialization and shared_search.
Dependencies: retrieval.search, retrieval.context, api, cli, evaluation.runner; offline pytest and fixed-vector fixtures.
Invariants: Keep diacritics, exclude gold/options from question-only retrieval, pin one profile/snapshot and distinguish rank dedup from evidence-span coverage.
Trace: RT-01–07, AP-01, EV-01/02/06, PK-02; paper 03/05/11.
"""
