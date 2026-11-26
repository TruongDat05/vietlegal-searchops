"""Purpose: Own query processing, snapshot BM25/dense exact search and RRF orchestration.
Inputs/outputs/artifacts: Gold-free requests, locked profiles and pinned S1 will yield B0/D0/D1/D2/H0/H1 ranks, source mappings, timings and deterministic selected context; no durable rankings cache is initially required.
Interfaces: search.
Dependencies: contracts, config, embedding.e5, embedding.cache, indexing.snapshots, retrieval.context; SQLite FTS5 and NumPy.
Invariants: Keep diacritics with unicode61 remove_diacritics 0, escape MATCH, rank FTS bm25 ascending and dense cosine descending; lock tie-break/candidate limits, reject mismatches and preserve complementary spans.
Trace: RT-01–07, EV-02, H05; paper 03/05/11.
"""
