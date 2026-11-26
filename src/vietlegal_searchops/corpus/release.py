"""Purpose: Own legal structure, source identities, revision relations and corpus release validation.
Inputs/outputs/artifacts: Raw manifests plus normalized texts will yield C1 units/spans, linked duplicates, date/status records, coverage and a locked corpus manifest.
Interfaces: release_corpus, validate_corpus and read_revision.
Dependencies: contracts, config, corpus.normalize; stdlib and SQLite.
Invariants: Check text slices against absolute code-point spans; distinguish crawl/issue/consolidation/validity dates, preserve unverified metadata and link amendments without synthetic consolidation.
Trace: DT-03–08, PL-02/03, H01; paper 02/12.
"""
