"""Purpose: Declare fixed-weight Qwen answering and provider invocation ownership.
Inputs/outputs/artifacts: Gold-free queries and shared retrieval context will produce cited answers/actions, invocation records and persisted predictions through child modules.
Interfaces: Use answer.answer_question and qwen.complete directly.
Dependencies: none; no re-exports.
Invariants: Use one retrieval pass and explicit provider identity; source text is evidence rather than prompt instructions.
Trace: QW-01–05, H05; paper 08.
"""
