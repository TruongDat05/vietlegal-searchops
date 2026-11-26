"""Purpose: Declare separated prediction collection, deterministic metrics and saved-output scoring.
Inputs/outputs/artifacts: Public cases will yield P1 first; P1 plus authorized labels later yield metrics, judge outputs and reports through child modules.
Interfaces: Use runner.collect_predictions, metrics.evaluate_retrieval and score.score_predictions directly.
Dependencies: none; no re-exports.
Invariants: Retrieval sweeps remain provider-free; gold access starts only after durable prediction collection.
Trace: EV-01–08, EX-01–08, H03/H09; paper 09–11.
"""
