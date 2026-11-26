"""Purpose: Declare mandatory E5 fine-tuning and dev-only deployment selection.
Inputs/outputs/artifacts: T1 train/dev and pretrained E5 will produce D1/D2 checkpoints, measured run logs and a selected E1/index release through child modules.
Interfaces: Use train_e5.train and select.select_release directly.
Dependencies: none; no re-exports.
Invariants: Only E5 weights change; training and selection never consume test/calibration supervision or judge outputs.
Trace: TR-01–08, H02–H04/H06; paper 04/10.
"""
