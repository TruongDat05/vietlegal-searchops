"""Purpose: Own post-prediction label joins, judge dispatch and final report persistence.
Inputs/outputs/artifacts: Durable P1 plus restricted G1, locked rubric/J1 and cost profiles will yield deterministic metrics, judge JSON, group/seed/coverage/cost reports and error queues.
Interfaces: score_predictions and write_reports.
Dependencies: contracts, config, predictions, datasets.release, evaluation.metrics, judge.deepseek; stdlib.
Invariants: Never invoke retrieval/generation or reconstruct current context; verify saved hashes before reading gold, leave judge errors unscored and preserve eligible/completed/scored denominators and actual-versus-replay costs.
Trace: EV-04/05/07/08, EX-05/08, H09; paper 09–12.
"""
