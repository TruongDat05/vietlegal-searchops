"""Purpose: Own dataset auditing, role-specific exports and restricted gold contracts.
Inputs/outputs/artifacts: Reviewed drafts, groups and source manifests will yield T1 pilot/release train/dev, gold-free case payloads, separate G1 gold/qrels, audit logs and datasheets.
Interfaces: release_datasets, validate_datasets, load_training_release and load_gold; define TrainingSample and GoldRecord here.
Dependencies: contracts, config, corpus.release, datasets.splits; stdlib.
Invariants: Only accepted benchmark cases ship; evidence sets use verified source atoms, train/dev handoffs exclude held-out gold, and post-freeze label fixes create new versions.
Trace: DS-07/10/11, PL-04, H02/H04; paper 06/09 and appendices.
"""
