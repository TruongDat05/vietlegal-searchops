"""Purpose: Declare the single shared search and context interface.
Inputs/outputs/artifacts: Gold-free questions and pinned S1 handles will produce ranks and source-mapped selected context through search.py and context.py.
Interfaces: Use search.search and context.select_context directly from CLI, HTTP and evaluation collection.
Dependencies: none; no re-exports.
Invariants: Preserve original queries, explicit profiles and one snapshot; retrieval never reads benchmark gold or judge output.
Trace: RT-01–07, H05; paper 03/05/11.
"""
