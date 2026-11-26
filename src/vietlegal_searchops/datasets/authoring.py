"""Purpose: Own evidence-first drafts, variants, MCQ and evidence-removal challenge specifications.
Inputs/outputs/artifacts: Split-authorized C1 spans, prompts and reviews will yield draft questions/positives/gold, variant links, controlled challenge targets and raw Qwen provenance.
Interfaces: author_cases, derive_variants, derive_mcq and propose_challenges.
Dependencies: contracts, config, corpus.release, datasets.splits, agent.qwen; stdlib.
Invariants: Use only each split's authorized evidence, protect numbers/meaning, review alternative evidence across challenge targets, and require human acceptance rather than model-certified gold.
Trace: DS-03–09, EN-05; paper 06/12.
"""
