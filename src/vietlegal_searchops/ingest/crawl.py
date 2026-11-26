"""Purpose: Own allowlisted discovery, bounded fetching and crawl recovery.
Inputs/outputs/artifacts: Seed/coverage URLs and prior crawl journals will yield original bytes, source metadata, hashes, extraction references and raw-source manifests.
Interfaces: discover and fetch_batch with explicit rate, retry, cache and resume profiles.
Dependencies: contracts, config; stdlib and httpx.
Invariants: Accept only the three approved sources and their traced attachments/CDNs; preserve originals, idempotent batches and unverified date/status fields.
Trace: SR-01–08, EN-04/05; paper 02.
"""
