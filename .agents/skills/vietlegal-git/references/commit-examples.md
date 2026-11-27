# Coherent commits and accurate messages

The unit of a commit is a purpose that a reviewer can understand and, when
practical, revert independently. File count is irrelevant. Keep production
behavior, matching tests and necessary docs together.

## Example grouping

Suppose the authorized worktree contains independent cache, API and documentation
changes. A sensible sequence is:

```text
fix(cache): reject incomplete embedding entries
feat(api): serve historical sources from pinned snapshots
docs(workflow): document H05 search and context handoff
```

The first commit includes the cache regression test. The second includes its
API/source tests and required contract changes. The third is separate only if
its handoff documentation is an independent update; documentation needed to
understand an earlier behavior change belongs with that earlier commit.

Other appropriate groups:

- Shared schema and consumers together when splitting them would break imports
  or wire compatibility.
- Package/lock changes together when establishing an environment prerequisite.
- A broad formatting-only change separate from behavior, if formatting was
  requested at all.
- A test-only commit for a genuinely independent coverage improvement. Do not
  split required tests away from their feature just to produce another commit.

If one file contains two independent changes, stage its relevant hunks separately.
If the changes cannot form correct intermediate states, retain a coherent larger
commit rather than creating artificial broken steps. A worktree with one change
requires only one commit.

## Message examples

```text
fix(context): retain complementary spans from the same source unit

Deduplicate overlapping ranges while preserving the separate rule and
exception spans needed by the selected evidence.

Validation: <actual relevant command and observed result>
```

```text
feat(indexing): preserve pinned snapshots during activation

Keep in-flight readers on their loaded snapshot while activating the validated
replacement, including historical source resolution.

Validation: <actual activation and source-resolution checks>
```

The validation markers are examples to replace, never claims to copy unchanged.
Keep the subject accurate to the staged patch, use the body only when useful and
state important limitations. Do not put unrelated implementation stories in one
long message to justify an unfocused commit.

## Index and worktree evidence

Review the exact staged content before committing. If later unstaged changes
are required for tests to pass, a whole-worktree pass does not validate the staged
commit. Reconsider the grouping or check an isolated staged snapshot. Preserve
pre-existing work and do not temporarily delete the user's changes to manufacture
a clean test state.

For an isolated check, materialize exactly the staged tracked files, additions
and deletions into a temporary tree; use the same locked runtime and declared
fixtures. Do not copy later unstaged/untracked work into it to make it pass.
Keep required ignored artifacts explicitly separate and disclose them. A plain
checkout of HEAD excludes staged changes; testing it does not test the new commit.
If isolation is unavailable, report which commits were checked only in the
combined worktree rather than inventing per-commit verification.

After committing, report the real SHA and subject for each commit. A local commit
does not prove a remote push; verify publication separately when requested.
