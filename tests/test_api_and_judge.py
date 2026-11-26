"""Purpose: Plan HTTP/source, Qwen output and DeepSeek calibration contract checks.
Inputs/outputs/artifacts: Mocked requests/provider responses, historical snapshots and blind human-label fixtures will yield schema, source-membership, retry/budget and calibration identity results.
Interfaces: Planned tests for source_route, actual_context, provider_identity, verdict_errors and blind_calibration.
Dependencies: api, agent.qwen, agent.answer, judge.deepseek, judge.calibrate; offline pytest and fake provider responses.
Invariants: Never call live providers in CI; reject missing artifacts/gold payloads, preserve citation errors, require pre-verdict human labels and audit separately from calibration.
Trace: QW-01–05, JG-01–07, AP-01–06, PK-02; paper 08/09/11.
"""
