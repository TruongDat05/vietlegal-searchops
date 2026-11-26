"""Purpose: Own HTTP routes and historical source-viewer data for the application.
Inputs/outputs/artifacts: Validated requests and pinned artifacts will yield search/answer/source/status responses and persisted request predictions; serve the comment-only web asset after implementation.
Interfaces: POST /search, POST /answer, GET /source and GET /status.
Dependencies: contracts, config, predictions, indexing.snapshots, retrieval.search, agent.answer; FastAPI.
Invariants: Reuse shared retrieval/context; resolve citations by snapshot/revision/hash, expose recorded update status, reject mismatches and exclude gold and credentials.
Trace: AP-01–06, QW-03/05, RT-06; paper 07/08/11.
"""
