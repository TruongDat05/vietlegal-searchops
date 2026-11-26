"""Purpose: Own independent target-state and retrieval parity verification.
Inputs/outputs/artifacts: Target sources, a candidate, locked query/tolerance policy and independent full-build vectors will yield revision/metadata/membership/input/profile/vector/FTS/rank differences and a hash-bound audit report.
Interfaces: verify_update.
Dependencies: contracts, config, indexing.build, indexing.snapshots, retrieval.search; stdlib and NumPy.
Invariants: Reconstruct reference without updater state; fixed-vector logic checks do not establish encoder accuracy, speed or cost; audit the same target/chunker/weights/dedup and never mutate/publish candidates.
Trace: IX-09/10, EX-07, H07; paper 07/10/12.
"""
