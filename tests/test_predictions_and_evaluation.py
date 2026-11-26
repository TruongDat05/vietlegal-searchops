"""Purpose: Plan durable-before-scoring, deterministic metrics and experiment-accounting validation.
Inputs/outputs/artifacts: Known ranks/evidence sets, saved contexts and interrupted/error ledgers will yield eligibility, MCQ/coverage, grouped comparison and resume-order checks.
Interfaces: Planned tests for save_before_gold, complete_evidence_sets, grouped_pairs, uncertain_attempts and replay_costs.
Dependencies: predictions, evaluation.runner, evaluation.metrics, evaluation.score; offline pytest and fixtures.
Invariants: Scoring replays the actual saved context, empty evidence is not success, failures remain visible and variants/seeds are not independent source-group samples.
Trace: EV-01–08, EX-02–08, PK-02; paper 09–12 and appendices.
"""
