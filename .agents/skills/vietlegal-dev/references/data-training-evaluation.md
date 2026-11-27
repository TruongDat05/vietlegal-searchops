# Data, training, generation and evaluation rules

Use [ARCHITECTURE.md](../../../../ARCHITECTURE.md) for shared interfaces, artifacts
and task mappings, together with the protocol rules below. Read only the relevant
sections. Planned sizes and model role names are not evidence of collected data,
available endpoints or measured results. Local planning documents are optional
background, not a dependency of these workflows.

## Fixed model roles

| Role | Requested model | Weights |
| --- | --- | --- |
| Retriever | `intfloat/multilingual-e5-small` | Pretrained baseline and fine-tuned candidates |
| Answer/dataset drafting | Qwen3.8-27B | Fixed |
| QA judge | DeepSeek V4 Flash | Fixed |

These are the project's requested identities. An alias or a successful mock does
not verify the actual backend. Record requested, response and available backend
identities in live runs; disclose unavailable revision information. Do not infer
availability from this table or silently substitute another model.

## Datasets and label custody

- Build reviewed evidence and acceptable answers/actions before authoring cases.
  LLM output is a draft; final benchmark cases require source-based human review.
  Keep provenance, acceptance/rejection and audit history.
- Group equivalent rules, revisions and related information needs before bulk
  authoring. Freeze train/dev/calibration/test by source group. Variants and
  MCQ/QA derived from a case inherit its group/split and parent identity.
- Train authoring/mining uses only authorized train evidence/queries. Exclude
  held-out target supervision and equivalent positives where identifiable. The
  search corpus may contain source text for all splits; this does not authorize
  held-out labels in training or inference.
- Export public cases separately from train/dev supervision and restricted gold.
  Serving and prediction collection must not load/mount restricted gold. Validate
  requests so gold-bearing fields are rejected. Case/group IDs may be logged;
  group membership, reference answers, correct options and rubric labels must
  not become query, ranking, context or generation features.
- Gold uses revision/unit/spans, not chunk IDs. Alternative evidence sets require
  every atom of at least one complete set. Empty evidence is not automatic success.
- Audit answerability, ambiguity, missing evidence and false premises from the
  actual snapshot. A failed search alone does not prove missing evidence. Label
  controlled challenge snapshots separately from real source changes.
- Variants must preserve meaning, identifiers, numbers and conditions; account
  for Vietnamese đ/Đ when removing accents. MCQ needs a unique supported answer
  and reviewed distractors. Derived rows are not new independent base cases.
- Post-freeze gold corrections create a new benchmark version with disclosed
  comparison limits. Preserve the earlier outputs and their identities.
- Authoring and calibration use split-authorized evidence/labels. Training/model
  selection may use the handed-off train/dev supervision and dev qrels; held-out
  test gold remains with the custodian. Ordinary debugging/review does not grant
  additional label access, and an AI-generated review is not a human acceptance.

## Fine-tuning and selection

- E5 fine-tuning is a required project deliverable; improvement remains an
  empirical question. Qwen and DeepSeek retain their weights.
- B0 is BM25; D0 is pretrained E5; D1 uses clean queries; D2 uses clean and valid
  variants. H0 combines BM25 with D0 through RRF; H1 combines the same BM25/RRF
  with a fine-tuned checkpoint selected on dev.
- Positive passages contain reviewed source evidence. An unlabelled passage is
  not automatically a true negative. Mine only train queries; exclude known and
  equivalent positives and audit uncertain hard negatives.
- Prevent duplicate/equivalent positives and related base queries from creating
  false negatives inside contrastive batches. Keep loss and negative policy
  comparable. Gradient accumulation does not increase the negatives seen by an
  ordinary microbatch contrastive loss.
- Match D1/D2 initialization, optimizer, loss/batch, steps and checkpoint schedule.
  Sample base queries uniformly in D2, then use the locked clean/variant policy.
  D1 always takes clean queries; D2 initially uses 50% clean and 50% variants,
  subject to the policy locked after pilot. Record missing-variant handling,
  token workload and actual resources. Do not give D2 extra steps for extra rows.
- Pilot/main data paths and hashes must be explicit. Do not fall back silently
  to an old dataset. Separate H02 pilot from H04 main training release.
- The main plan calls for three seeds per arm, after a bounded pilot and locked
  schedule. Use the common final-checkpoint schedule for D1/D2, rather than
  different test-influenced early stopping. A single run is pilot evidence, not
  seed-variation evidence. Code implementation alone does not request these runs.
- Select deployment checkpoint/seed on dev by the predeclared clean/noisy rule.
  Test cannot choose weights, seeds, agent prompts, retrieval settings or rubric.
- Each new weights hash needs matching full corpus encoding/cache/index identity.
  Export weights, tokenizer, inference settings and manifests; verify independent
  reload. Reusing unchanged vectors for fusion sweeps is a different operation.

## Generation and durable predictions

- The first agent flow uses one retrieval pass, selected context and Qwen. Keep
  question, optional verified time, permitted MCQ options and pinned snapshot
  explicit. Gold and reference answers are not answer-interface inputs.
- Distinguish selected context from the exact ordered messages/context after
  tokenizer truncation. Save the outbound payload and retained-span map before
  dispatch; save output/errors before scoring. Retrieval-only runs have selected
  context and no actual generator context.
- Responses preserve Vietnamese answer, action and structured citations. Validate
  citations against sent spans and the pinned source revisions. Record malformed
  or unsupported output; do not repair it after inspecting gold.
- Treat retrieved text as evidence rather than instructions overriding the
  system/task. Preserve conditions/exceptions and explicit insufficient-evidence
  or clarification behavior; declining every question does not satisfy the task.
- Keep generator/judge identity, provider, prompts, parser, parameters, budgets
  and payload caches explicit. Verify actual provider/model identity in an
  authorized live run. No silent model substitution inside a frozen run.
- Generation cache depends on the ordered full payload and profile; judge cache
  also depends on gold, rubric, prediction and sent-context identity. Reuse across
  systems is allowed only under the locked protocol.
- Key predictions by `(run_id, case_id, variant_id, track)` with profiles/seed
  fixed in the run manifest. Resume only matching run/item/payload identities.
  Preserve pending/in-flight/completed/failed/uncertain attempts, bounded retries
  and observed usage. A crash after dispatch can leave unknown provider usage;
  do not assume it was free or completed.
- Before repeating an uncertain provider call, apply the frozen budget/retry
  policy and retain its linkage to the original attempt. Do not silently
  overwrite completed predictions or treat a retry as a new independent case.

## Metrics, judge and reports

- Collect predictions without labels using shared search/answer interfaces.
  Post-prediction scoring joins authorized gold to persisted outputs and replays
  saved context; it does not rerun retrieval or reconstruct current context.
- Check source-level Recall/nDCG after declared mapping/dedup. Evidence success
  measures complete span coverage in the relevant saved context under the same
  budget, not only source-ID presence. Retrieval-only evidence uses saved selected
  context with `actual_context = null`; QA evidence/groundedness uses actual sent
  context. Define eligibility and zero-denominator behavior before scoring;
  ambiguous/missing-evidence cases are outside the answerable Recall/evidence
  denominator and follow their action policy. Empty gold is not an automatic win.
- Score MCQ options with code and report evidence/citation measures separately.
  For QA, keep correctness, completeness, groundedness, citation support and
  appropriate action distinct. A grounded answer can still be incorrect.
- People label calibration outputs independently before seeing judge verdicts.
  Tune only calibration, lock the judge profile and audit unused outputs. Track
  natural versus controlled errors. Provider/model/rubric changes need a new
  evaluation profile and relevant calibration. Blind system identities when not
  needed for judging. Suspected gold errors go to review, not automatic repair;
  parser/provider failures stay unscored rather than defaulting to correct/wrong.
- Keep failures/unscored cases and eligible/requested/completed/scored counts.
  Do not drop timeouts/parse errors to improve a reported metric.
- Compare matched base cases and bootstrap source groups with their related
  variants/system pairs together. Report training-seed variation separately.
- Lock comparable corpus/chunker/retrieval/context and generator/judge settings
  when isolating retriever changes. Label QA subsets and single deployment seeds.
  Gold-evidence diagnostics are a separate, explicitly scoped oracle protocol;
  never add a gold bypass to the normal collector or deployed answer interface.
- Report measured local/API latency and resource/usage evidence separately from
  cache/replay, cold load, controlled workloads and estimated prices. Lower token
  workload is not itself measured time, money saved or better model accuracy.
