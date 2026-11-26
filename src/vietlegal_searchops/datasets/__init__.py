"""Purpose: Declare source-group data construction and restricted-label release ownership.
Inputs/outputs/artifacts: C1 evidence will produce frozen splits, T1 train/dev releases, public case payloads and separate G1 gold through child modules.
Interfaces: Use splits.freeze_splits, authoring.author_cases and release.release_datasets directly.
Dependencies: none; no re-exports.
Invariants: Keep related revisions, variants and MCQ/QA in one split; held-out gold never enters serving.
Trace: DS-01–11, H02/H04; paper 06.
"""
