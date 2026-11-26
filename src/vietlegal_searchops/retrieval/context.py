"""Purpose: Own source-preserving evidence selection and exact context serialization.
Inputs/outputs/artifacts: Ranked source spans and a frozen budget/serialization profile will yield ordered ContextBundle text, source labels, retained-span maps and payload hashes for prediction records.
Interfaces: select_context and fit_context.
Dependencies: contracts, config, embedding.e5; tokenizer support only.
Invariants: Never use gold; deduplicate overlapping spans while keeping complementary evidence, count all labels/metadata within the E5 comparison budget and record every Qwen-limit reduction with retained spans/profile identity.
Trace: RT-04, QW-03, EV-01; paper 03/05/08/09.
"""
