"""Purpose: Own gold-free retrieval/MCQ/QA collection and locked experiment execution.
Inputs/outputs/artifacts: Public case manifests, frozen profiles and run budgets will yield resumable P1 ranks/contexts/responses, attempt ledgers and resource/latency records.
Interfaces: collect_predictions and collect_update_measurements; support in-process shared code or the same HTTP contracts.
Dependencies: contracts, config, predictions, indexing.snapshots, indexing.update, indexing.verify, retrieval.search, agent.answer; httpx and stdlib.
Invariants: Retrieval mode calls neither Qwen nor judge; persist selected context even without generation, log actual context for answers, prevent concurrent/uncertain retry double-counting and never load gold.
Trace: EV-02/03/07/08, EX-01–07, H03/H09; paper 10/11.
"""
