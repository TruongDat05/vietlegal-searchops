"""Purpose: Declare checkpoint-specific E5 inference and exact-input vector reuse.
Inputs/outputs/artifacts: Full query/passage inputs and encoder profiles will yield validated vectors, encoder releases and cache entries through child modules.
Interfaces: Use e5.load_encoder/encode and cache.lookup_complete/store_complete directly.
Dependencies: none; no re-exports.
Invariants: Never mix checkpoint, tokenizer or inference profiles; vector reuse never supplies occurrence membership.
Trace: IX-02/03, TR-06/08; paper 03/07.
"""
