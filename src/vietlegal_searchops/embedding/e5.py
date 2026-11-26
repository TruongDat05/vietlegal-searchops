"""Purpose: Own E5 loading, token accounting, inference and encoder-release checks.
Inputs/outputs/artifacts: Explicit weights/tokenizer/profile and full prefixed inputs will yield 384-dimensional vectors, token counts and verified E1 reload manifests.
Interfaces: load_encoder, count_tokens, encode, validate_vectors and validate_encoder_release.
Dependencies: contracts, config; Sentence Transformers/PyTorch and NumPy.
Invariants: Use masked mean pooling and L2 normalization, finite matching-dtype vectors, exactly one query:/passage: prefix and total input limit 512; reject checkpoint/profile mismatch.
Trace: IX-02, TR-06/08, EN-02; paper 03/04/07.
"""
