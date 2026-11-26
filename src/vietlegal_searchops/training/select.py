"""Purpose: Own dev-only comparison, checkpoint-specific indexing and E1 handoff.
Inputs/outputs/artifacts: Scheduled candidate checkpoints, T1 dev qrels and a predeclared rule will yield per-seed dev records, selected checkpoint/seed and a matching encoder/snapshot manifest.
Interfaces: evaluate_candidates and select_release.
Dependencies: contracts, config, embedding.e5, indexing.build, evaluation.runner, evaluation.metrics; stdlib.
Invariants: Re-encode the whole corpus for every changed weights hash; apply locked clean/noisy guardrails without Qwen/judge calls and never choose checkpoints/seeds from test.
Trace: TR-03/04/06–08, H03/H06; paper 04/10/11.
"""
