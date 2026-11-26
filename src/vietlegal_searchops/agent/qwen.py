"""Purpose: Own the Qwen request adapter, payload cache and attempt accounting.
Inputs/outputs/artifacts: Serialized messages, explicit provider/model profile and budget will yield raw responses, request/response identities, usage/errors and complete cache records.
Interfaces: complete and validate_response_identity.
Dependencies: contracts, config; httpx and stdlib.
Invariants: Keep requested Qwen3.8-27B weights/prompt/thinking/sampling fixed; cache exact ordered payload/profile only, distinguish replay from live calls, bound retries and never silently change model/provider.
Trace: QW-01/04, EN-03–05, DS-03; paper 08/10/11.
"""
