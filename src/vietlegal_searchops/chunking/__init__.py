"""Purpose: Declare structure-aware chunk and encoder-input ownership.
Inputs/outputs/artifacts: C1 units and a chunk profile will produce C2 occurrences and exact serialized passage inputs through structure.py.
Interfaces: Use structure.chunk_corpus directly.
Dependencies: none; no re-exports.
Invariants: Chunk identities never replace gold source spans; shared vectors cannot erase occurrence provenance.
Trace: IX-01, PL-05; paper 02/03/05.
"""
