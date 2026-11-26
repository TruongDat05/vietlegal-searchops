"""Purpose: Own train-only negative mining, collision-aware sampling and E5 training.
Inputs/outputs/artifacts: T1 accepted pairs, authorized train groups and a locked D1/D2 schedule will yield reviewed negative pools, checkpoints, losses, token workload and resource logs.
Interfaces: mine_negatives and train.
Dependencies: contracts, config, datasets.release, datasets.splits, embedding.e5, retrieval.search; Sentence Transformers/PyTorch.
Invariants: Exclude known/held-out equivalent positives from negatives; balance base queries, avoid batch collisions, match D1/D2 steps/loss/batch and fixed final checkpoints across three planned seeds; accumulation is not a larger contrastive batch.
Trace: TR-01–05, DS-10; paper 04/06/10.
"""
