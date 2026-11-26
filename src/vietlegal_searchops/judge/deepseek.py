"""Purpose: Own fixed-profile DeepSeek judging, rubric/schema parsing, retries and verdict cache.
Inputs/outputs/artifacts: Saved P1 actual context, gold and locked rubric/profile will yield per-dimension JSON verdicts/reasons, identity/usage records, cache entries or unscored review errors.
Interfaces: judge_saved and validate_verdict.
Dependencies: contracts, config; httpx and stdlib.
Invariants: Blind system labels, report five QA dimensions separately, key cache by gold/rubric/prediction/context/provider settings and record requested/response/backend identities; profile changes require recalibration and never self-repair gold.
Trace: JG-01–03/06/07, EV-07; paper 09/12.
"""
