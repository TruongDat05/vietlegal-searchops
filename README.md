# VietLegal SearchOps

A research project for Vietnamese labour-contract search and question answering. The design combines BM25 and multilingual E5 retrieval, Qwen answers with source citations, and incremental index updates with exact-input embedding reuse.

**Status:** architecture scaffold. Python modules, configuration, prompts, tests, and deployment files currently describe planned behavior. The application is not runnable yet, and no experiment results are included.

## Planned workflow

```mermaid
flowchart TD
    A[Official legal sources] --> B[Versioned corpus and legal chunks]
    B --> C[Freeze source-group splits]
    C --> D[Author train and dev data]
    D --> E[Fine-tune E5 and select on dev]
    B --> F[Build or update index with embedding reuse]
    E --> F
    F --> G[Full-rebuild parity and snapshot validation]
    G --> H[Publish immutable snapshot]

    Q[User question] --> R[BM25 + E5 retrieval with RRF fusion]
    H --> R
    R --> S[Select source-linked context]
    S --> T[Qwen answer with citations]
    R --> P[Save predictions and context]
    T --> P

    C --> U[Restricted held-out gold]
    P --> V[Metrics and human-calibrated DeepSeek judge]
    U --> V
```

Each request uses one pinned snapshot so retrieval, answers, and citations refer to the same source revisions. Retrieval-only runs need no LLM. Held-out gold enters scoring after predictions are saved; answer evaluation replays the exact context sent to Qwen.

## Repository guide

| Path | Purpose |
| --- | --- |
| `src/vietlegal_searchops/` | Planned ingestion, corpus, datasets, training, indexing, retrieval, answering, and evaluation modules |
| `config/`, `prompts/`, `rubrics/` | Configuration, prompt, and judging specifications |
| `tests/` | Planned offline checks and fixture requirements |
| `deploy/`, `web/` | Deployment and demo placeholders |
| `artifacts/` | Artifact layout and access rules; generated data is excluded from Git |

See [ARCHITECTURE.md](ARCHITECTURE.md) for module contracts and implementation order. The detailed workflow is available as [SVG](workflow.svg), [editable HTML](workflow.html), and [design notes](workflow_notes.md). Runtime requirements and setup commands will be added when implementation begins.
