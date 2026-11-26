"""Purpose: Own bundle staging, structural validation, loading, atomic publication and historical lookup.
Inputs/outputs/artifacts: Complete metadata/membership/vector/profile sets and release-audit evidence will yield immutable S1 manifests/projections, loaded handles and an active-reference record.
Interfaces: stage_bundle, validate_bundle, load_snapshot, publish, pin and resolve_source.
Dependencies: contracts, config, embedding.e5; stdlib, SQLite and NumPy.
Invariants: Validate all hashes/profiles/FTS rows before activation; pin one handle through generation/citations, retain referenced history and leave active state untouched on prepublication failure; never call updater/verifier from this module.
Trace: IX-08/10, RT-06, AP-01, H06/H07; paper 07/11.
"""
