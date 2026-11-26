"""Purpose: Own blind human-label preparation, agreement analysis, profile locking and separate audit.
Inputs/outputs/artifacts: Calibration P1/verified sources and independent human labels will yield blind packets, disagreement history, confusion/precision/recall/F1 reports and locked J1 manifests.
Interfaces: prepare_blind, compare_labels, lock_profile and audit_profile.
Dependencies: contracts, config, predictions, judge.deepseek; stdlib and NumPy.
Invariants: Record human labels before revealing verdicts, distinguish natural/controlled errors, declare zero-denominator and error-positive rules, tune only calibration and keep audit outputs unused for tuning.
Trace: JG-04–07, H08; paper 09/10/12.
"""
