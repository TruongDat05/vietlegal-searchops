"""Purpose: Own the independent full-corpus reference build.
Inputs/outputs/artifacts: Target C1 sources, chunk/encoder profiles and an explicit cold-cache or fixed-vector mode will yield fresh memberships, vectors, FTS/matrix projections and a staged S1 bundle.
Interfaces: full_build.
Dependencies: contracts, config, corpus.release, chunking.structure, embedding.e5, indexing.snapshots; stdlib and NumPy.
Invariants: Reconstruct target chunks/membership without prior indexes, updater plans or candidate caches; deduplicate only identical full inputs within the locked workload and re-encode each changed checkpoint.
Trace: IX-04/08, TR-06, PL-08; paper 07/10.
"""
