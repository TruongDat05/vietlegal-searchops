"""Purpose: Own legal-unit chunking and complete passage serialization together.
Inputs/outputs/artifacts: C1 source units, breadcrumbs and tokenizer/chunk profiles will yield C2 occurrences, ordered source-span maps, full passage inputs and hashes.
Interfaces: chunk_corpus and serialize_passage.
Dependencies: contracts, config, embedding.e5; tokenizer support only.
Invariants: Count prefix, breadcrumb, body and special tokens within 512; preserve complementary spans, attach prefix once and retain original source coordinates through splits/merges.
Trace: IX-01, RT-04; paper 02/03/05.
"""
