"""Purpose: Declare command dispatch for the shared VietLegal workflows.
Inputs/outputs/artifacts: Explicit commands/configurations will yield corpus, dataset, model, snapshot and run artifacts through their owning modules.
Interfaces: ingest, release-corpus, release-data, train-e5, select-checkpoint, build-index, update-index, verify-update, search, answer, evaluate, score and calibrate commands.
Dependencies: config, ingest.crawl, corpus.release, datasets.release, training.train_e5, training.select, indexing.build, indexing.update, indexing.verify, retrieval.search, agent.answer, evaluation.runner, evaluation.score, judge.calibrate; stdlib.
Invariants: Keep retrieval-only commands provider-free; separate prediction collection from gold-enabled scoring and report actual profiles without fallback.
Trace: EN-01, RT-07, EV-02/07, IX-09; paper 10/11.
"""
