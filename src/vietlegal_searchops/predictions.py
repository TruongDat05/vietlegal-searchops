"""Purpose: Own prediction persistence, attempt accounting and resumable run ledgers.
Inputs/outputs/artifacts: Requests, ranks, selected/actual contexts, provider attempts and responses will produce immutable prediction records, payload hashes and run journals.
Interfaces: begin_run, save_context, save_prediction, resume_run and read_predictions.
Dependencies: contracts; stdlib and SQLite.
Invariants: Persist exact outbound context before dispatch and prediction/error before scoring; resume only matching frozen runs, distinguish uncertain requests from completed calls, and never store gold here.
Trace: EN-04/05, EV-03/08, QW-03; paper 08–11 and appendices.
"""
