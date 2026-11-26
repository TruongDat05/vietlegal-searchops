"""Purpose: Plan E5 input/cache, sampler and checkpoint-selection validation.
Inputs/outputs/artifacts: Tokenizer/profile/fixed-vector and train/dev fixtures will yield prefix/budget/cache, collision, schedule and re-encoding checks; no model load is planned for offline CI.
Interfaces: Planned tests for full_input_keys, profile_mismatch, sampler_collisions and dev_only_selection.
Dependencies: chunking.structure, embedding.e5, embedding.cache, training.train_e5, training.select; offline pytest and fixture tokenizer/encoder records.
Invariants: Test changed breadcrumbs/weights/backend, incomplete vectors and full checkpoint-specific re-encoding; equal optimizer steps do not imply equal contrastive batches.
Trace: IX-01–03, TR-01–08, PK-02; paper 03/04/07/10.
"""
