"""Purpose: Declare the official-source ingestion package.
Inputs/outputs/artifacts: Allowlisted discovery pages will produce archived originals, raw manifests and crawl checkpoints through crawl.py.
Interfaces: Use crawl.discover and crawl.fetch_batch directly.
Dependencies: none; no re-exports.
Invariants: Retain attachment origin links and never broaden source scope or treat crawl time as legal validity.
Trace: SR-01–08, PL-02; paper 02.
"""
