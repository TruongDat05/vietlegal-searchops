"""Purpose: Own format extraction and versioned text normalization.
Inputs/outputs/artifacts: Original HTML, structured data, DOC/DOCX or text PDF bytes will yield normalized revision text, extraction diagnostics and normalization provenance.
Interfaces: extract_normalize(raw_source, normalization_profile).
Dependencies: contracts, config; source-appropriate document readers and stdlib.
Invariants: Preserve structural separators before parsing, NFC accents, numbers, conditions and exceptions; changed normalization creates new text/hash and never rewrites originals.
Trace: DT-01/02/06/07; paper 02.
"""
