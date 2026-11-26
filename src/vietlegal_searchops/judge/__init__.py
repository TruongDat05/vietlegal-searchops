"""Purpose: Declare DeepSeek semantic scoring and human-calibrated profile ownership.
Inputs/outputs/artifacts: Saved predictions, restricted gold and blind human labels will yield judge verdicts, calibration reports and locked J1 profiles through child modules.
Interfaces: Use deepseek.judge_saved and calibrate.prepare_blind/lock_profile directly.
Dependencies: none; no re-exports.
Invariants: Human labels precede machine verdicts; calibration and separate audit never tune serving or test-selected checkpoints.
Trace: JG-01–07, H08; paper 09/12.
"""
