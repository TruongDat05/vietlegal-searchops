"""Purpose: Plan incremental parity, recovery and immutable-publication validation.
Inputs/outputs/artifacts: Labeled update events, fixed vectors and fresh full-build fixtures will yield membership/FTS/rank parity, crash/resume and concurrent-pin validation results.
Interfaces: Planned tests for all_update_modes, independent_reference, publication_failures, resume and historical_sources.
Dependencies: indexing.build, indexing.update, indexing.snapshots, indexing.verify, retrieval.search; offline pytest and fixtures.
Invariants: Cover no-edit/metadata-only/add/edit/delete/shared-vector and partial-cache events; candidate failures preserve active state, old requests retain history and verification cannot trust updater membership.
Trace: IX-04–10, RT-06, EX-07, PK-02; paper 07.
"""
