"""Purpose: Own document-incremental/exact-reuse planning and crash recovery.
Inputs/outputs/artifacts: Target C1, prior pinned S1, labeled events and locked cache policy will yield candidate memberships, durable job journals, workload/status records and staged bundles.
Interfaces: update_index and resume_update.
Dependencies: contracts, config, corpus.release, chunking.structure, embedding.e5, embedding.cache, indexing.snapshots; stdlib and SQLite.
Invariants: Bind resume to target/profile/job hashes; verify completed cache entries, separate occurrence removal from shared vectors, keep model waits outside write transactions and publish only through snapshots.
Trace: IX-05–08/10, AP-04, H07; paper 07.
"""
