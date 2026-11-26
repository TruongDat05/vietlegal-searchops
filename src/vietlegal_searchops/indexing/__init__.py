"""Purpose: Declare full/update builds, immutable snapshot lifecycle and independent parity checks.
Inputs/outputs/artifacts: Target corpus/chunk/encoder releases will produce staged/published S1 bundles, recovery journals and verification reports through child modules.
Interfaces: Use build.full_build, update.update_index, snapshots.publish/pin and verify.verify_update directly.
Dependencies: none; no re-exports.
Invariants: Serving reads only validated immutable snapshots; correctness references cannot depend on old updater membership.
Trace: IX-04–10, RT-06, H07; paper 07.
"""
