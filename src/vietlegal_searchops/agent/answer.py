"""Purpose: Own the shared one-pass search-to-answer flow and output/citation checks.
Inputs/outputs/artifacts: Gold-free QA/MCQ requests and pinned S1 will yield saved ranks, selected/actual context, answer/action/citations, raw outputs and structured failure records.
Interfaces: answer_question and validate_answer.
Dependencies: contracts, config, predictions, retrieval.search, retrieval.context, indexing.snapshots, agent.qwen; stdlib.
Invariants: Save actual serialized context/messages before Qwen and prediction before scoring; validate citations against sent spans and pinned sources, keep errors without repair, and never inspect gold or rewrite context outside the frozen profile.
Trace: QW-02/03/05, AP-02/05, EV-03; paper 05/08/11.
"""
