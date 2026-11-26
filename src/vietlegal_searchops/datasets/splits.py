"""Purpose: Own equivalent-rule grouping, split assignment and leakage checks.
Inputs/outputs/artifacts: C1 units, equivalence reviews and group policy will yield source-group mappings, frozen train/dev/calibration/test manifests and overlap reports.
Interfaces: group_sources, freeze_splits and audit_overlap.
Dependencies: contracts, config; stdlib.
Invariants: Freeze groups before authoring; revisions, near-duplicates, variants and MCQ/QA inherit groups; shared search corpus text does not authorize held-out supervision.
Trace: DS-01/02/08/10, PL-04; paper 06/10.
"""
