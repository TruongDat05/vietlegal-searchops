"""Purpose: Own deterministic retrieval, evidence, MCQ, coverage and grouped comparison calculations.
Inputs/outputs/artifacts: Saved ranks/retained contexts and authorized qrels/gold will yield metric records, eligibility counts and paired source-group uncertainty summaries; persistence belongs to score.py.
Interfaces: evaluate_retrieval, evaluate_mcq, evaluate_coverage and compare_groups.
Dependencies: contracts; stdlib and NumPy.
Invariants: Deduplicate ranking by revision/unit while checking complete alternative evidence sets over retained spans; exclude ineligible empty-gold/challenge cases, preserve failures, pair variants by base case and report training-seed variation separately.
Trace: EV-01/04–06, H03; paper 05/09/10 and appendices.
"""
