"""Purpose: Declare normalized, structured and versioned corpus ownership.
Inputs/outputs/artifacts: Archived originals will produce hash-locked C1 corpus releases, source units and provenance through normalize.py and release.py.
Interfaces: Use normalize.extract_normalize and release.release_corpus directly.
Dependencies: none; no re-exports.
Invariants: Preserve document/revision/unit identities and historical source spans; amendments remain separate documents.
Trace: DT-01–08, H01; paper 02.
"""
