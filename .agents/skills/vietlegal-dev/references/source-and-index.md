# Source, encoder, index and retrieval rules

Read the relevant interface, artifact, dependency and assumption sections of
[ARCHITECTURE.md](../../../../ARCHITECTURE.md). This guide highlights requirements
that affect implementation choices; the architecture contains the full records.
Check the actual code and profiles instead of treating a planned name as an
implemented interface. Source/protocol changes must be explicit and traceable.

## Corpus and source identity

- Keep the scope on individual employment contracts: conclusion, probation,
  performance/amendment, suspension/temporary reassignment, termination, and
  rights/obligations upon termination. Related pay/time rules enter only as needed
  for those topics; broader insurance, collective labour, foreign-worker and
  case-law coverage are outside the initial scope.
- The source systems are vbpl.vn, congbao.chinhphu.vn and vanban.chinhphu.vn,
  including attachments traced from permitted pages. Validate redirects/CDN
  provenance rather than treating every external URL as an authorized source.
- Archive original bytes, page/file URLs, fetch metadata and hashes. Preserve
  document, revision, source-unit, occurrence and snapshot identities separately.
  Link duplicate publications without losing source provenance; amendment
  documents keep their own identity and relations.
- Normalize text with a versioned profile. Preserve Vietnamese diacritics,
  identifiers, numbers, units, conditions and exceptions. Source spans use absolute
  Unicode code-point offsets in locked normalized revision text, with `[start,end)`
  semantics. Check bounds, hashes and text slices; byte offsets are different.
- After normalization changes, create the appropriate new revision/release and
  review affected labels. Keep referenced historical text/originals available.
- Crawl, issue, consolidation and applicability dates have different meanings.
  Unverified metadata remains explicit. A snapshot or content hash identifies
  evidence; it does not establish that a provision is legally in force.
- Use bounded retries, rate limits, durable batch progress and idempotent fetches.
  Add format readers for formats actually used; OCR/automatic consolidation are
  optional extensions, not implicit implementation requirements.

## E5 inputs and embedding identity

- Use the designated `intfloat/multilingual-e5-small` backbone and the locked
  weights/tokenizer identity. Query and passage inputs use `query: ` and
  `passage: ` exactly once. Count the entire serialized input, including
  breadcrumb, prefix and special tokens, within 512 E5 tokens. Do not rely on
  silent tokenizer truncation that invalidates the recorded source coverage.
- Preserve the mapping from each chunk occurrence to all covered source spans.
  Splitting/merging chunks must not detach evidence from its revision text.
- The standard E5 profile uses attention-mask-aware mean pooling, 384-dimensional
  vectors and L2 normalization. Validate finiteness, dimension, dtype and norm
  under the declared tolerance. Test fixtures may use tiny synthetic vectors.
- Profile identity covers weights/checkpoint, tokenizer, preprocessing, prefixes,
  serialization, pooling, normalization and inference backend/dtype/quantization.
  Query and corpus profiles must match. Fail explicitly on missing/incompatible
  artifacts; do not silently select another checkpoint or backend.

## Exact-input reuse

The cache key is the pair of SHA-256 hashes for full UTF-8 input and the project's
canonical embedding-profile serialization. Avoid process-dependent `hash()` and
unrecorded input normalization. Store enough identity/shape/completion information
to validate a hit. Similarity or matching body text alone never authorizes reuse.

| Change | Required behavior |
| --- | --- |
| Metadata outside encoder input | Vector can hit; update metadata/source membership |
| Breadcrumb, prefix, serialized body or tokenizer changes | Recompute affected inputs under the new identity |
| Weights or inference profile changes | Use a new profile and matching corpus/query encoding |
| One occurrence sharing a vector is removed | Remove that membership; retain vectors/history still referenced |
| Partial/corrupt vector or incomplete journal item | Treat as incomplete work and recover explicitly |

Occurrence membership belongs to the snapshot, not the vector cache. No-edit
reuse can require zero encoding while still checking the target release.

## Updates, verification and publication

Full rebuild, document-incremental and exact-reuse modes must use the same target,
chunker, weights and input-dedup policy. Record initial cache scope and workload
so a baseline does not accidentally receive another run's cached work.

The independent reference rebuild reconstructs target state from the source
release. Old/candidate indexes, updater plans, their membership and the candidate
vector cache must not be inputs to that rebuild. In fixed-vector mode, a separate
predeclared input-to-vector fixture may be shared by both builds; it must not be
derived from the candidate. This checks software logic, not real inference/speed.

Verify revisions, metadata, occurrences, complete input/profile/vector mapping
and values, snapshot-local FTS and locked query ranks. Use declared numeric
tolerance and deterministic tie-breaking. The verifier produces a target-bound
report; it does not modify or publish the candidate.

Keep update -> verification -> publication orchestration in CLI/experiment
callers. The snapshot publisher consumes the matching audit report; it must not
import/call the verifier or updater and introduce a dependency cycle.

Build in staging; verify structural completeness, hashes, profiles, source/model
availability and loading before activation. Release/benchmark activation also
requires matching full-rebuild parity evidence. Resolve crash/rename/fsync and
startup reconciliation decisions before claiming durable recovery. Do not model
files, SQLite and external model calls as one atomic transaction.

Pin one loaded snapshot per request across lexical/dense search, context,
generation and citations. Prepublication failures preserve the old active state;
old requests and citations retain their historical references after activation.
Resume only verified work bound to the same job, target and profile. Avoid long
write transactions while waiting for embedding/provider work. Do not add artifact
garbage collection as a side effect of an update task.

## Retrieval and context

- Keep one implementation in `retrieval/search.py`, called by CLI, HTTP and the
  collector. `/search` produces ranks and deterministic selected context without
  initializing Qwen/DeepSeek clients or requiring their credentials. B0 performs
  lexical retrieval without computing query embeddings; dense/hybrid modes use
  the matching encoder. Answering adds the generator flow.
- Use snapshot-local FTS statistics. The baseline keeps diacritics with
  `unicode61 remove_diacritics 0`; escape/construct MATCH queries deliberately.
  FTS `bm25()` sorts ascending; dense normalized similarity sorts descending.
- Start with the documented exact-vector approach. Extra ANN/vector-service
  layers or an alternate lexical normalization require a concrete project need
  and a distinct profile, rather than an implicit replacement.
- Lock branch limits, RRF, top-k, preprocessing, tie-breaking and context policy.
  RRF sums `1 / (c + rank)` over the branches containing a result, using ranks
  starting at 1 and zero contribution from an absent branch. It does not add
  unlike raw scores. Initial proposal values are dev-tuned defaults, not universal
  constants; H0/H1 must use the same frozen fusion policy.
- Ranking deduplication by revision/unit differs from context deduplication.
  Preserve complementary rule/exception spans; remove actual overlaps without
  dropping all later evidence from the same unit.
- Count labels, breadcrumbs and metadata with the reference E5 tokenizer under
  the locked comparison budget. The initial 2,048-token context budget is distinct
  from the 512-token limit per encoder input. Check Qwen's actual input limits
  separately; record reductions, exact retained spans and ordered messages. Keep
  API and evaluator selection/budget behavior identical for the same profiles.
- Gold/reference answers do not enter query processing or context selection.
  The primary MCQ retrieval protocol uses the question alone, not answer options.
