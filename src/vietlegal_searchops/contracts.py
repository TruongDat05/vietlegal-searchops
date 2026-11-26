"""Purpose: Define shared source, profile, snapshot, request, context and prediction contracts.
Inputs/outputs/artifacts: Versioned records will yield validated identities and canonical manifest/hash representations; no storage is owned here.
Interfaces: SourceSpan, CorpusManifest, EmbeddingProfile, SnapshotManifest, SearchRequest, SearchResult, ContextBundle and PredictionRecord.
Dependencies: none; stdlib only.
Invariants: Use revision-text hashes and absolute Unicode [start,end) spans; keep occurrence/vector identities distinct and exclude gold from serving records.
Trace: PL-03/05/06, EN-04; paper 02/07/11 and appendices.
"""
