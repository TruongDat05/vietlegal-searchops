"""Purpose: Own durable exact-input/profile embedding and query-cache entries.
Inputs/outputs/artifacts: UTF-8 serialized input plus canonical encoder profile will yield verified complete vectors or explicit misses in SQLite; no occurrence membership is stored here.
Interfaces: lookup_complete and store_complete.
Dependencies: contracts; stdlib and SQLite.
Invariants: Key full input/profile hashes including weights/tokenizer/preprocessing/pooling/normalization/backend/dtype; reject partial or invalid vectors, preserve history references and never reuse by body similarity.
Trace: IX-03/06/07, RT-02; paper 07/11.
"""
