---
name: vietlegal-git
description: Create coherent, clearly described Git commits for authorized VietLegal SearchOps changes, splitting independent work and preserving unrelated edits. Use when asked to commit, split commits or commit and push; includes optional Lazygit staging guidance.
---

# VietLegal Git workflow

Make history explain the changes. Creating code or skill files alone does not
request a commit. A commit request does not itself request a push or history
rewrite. Once scope is authorized, proceed without asking again for every commit.

Read [AGENTS.md](../../../AGENTS.md). Prefer ordinary Git for automated work.
If an interactive staging view is wanted and Lazygit is available, read
[the optional guide](references/lazygit.md); Lazygit is not required.

## Inspect and group

Inspect the branch, recent message style, worktree and index:

```bash
git status --short --branch
git log -5 --oneline
git diff --name-status
git diff --cached --name-status
git diff
git diff --cached
```

Inspect relevant untracked files too. Identify the requested changes and preserve
unrelated work/staging. If unrelated staged edits would enter a commit, resolve
scope without discarding the user's work. Ask only if ownership or target is
genuinely ambiguous. Check for an active merge/rebase/cherry-pick or unresolved
conflicts before ordinary commit work; do not continue someone else's operation
implicitly. If the user requests only staged changes, do not broaden that scope.

Group by one purpose or behavior, not file extension, file count or author:

- Keep a fix/feature with matching tests and necessary documentation.
- Separate independent fixes/features, broad formatting, environment changes
  and unrelated documentation updates.
- Order prerequisites before consumers. Keep inseparable interface/caller
  changes together so intermediate commits remain usable.
- A single coherent change can be one commit. Multiple independent changes must
  be split; never collapse the entire worktree into a catch-all commit.

See [commit examples](references/commit-examples.md) for project-specific groups.

## Stage and verify each commit

1. Stage explicit paths or selected hunks for this group; avoid blanket staging
   of a dirty worktree. For mixed files, use `git add -p -- path` interactively
   or an inspected index-only patch. Check a patch before applying it and
   preserve other working changes.
2. Inspect `git diff --cached --stat`, the whole `git diff --cached` and
   `git diff --cached --check`. Keep credentials and unrelated edits out. Keep
   restricted gold, generated weights and run artifacts out of ordinary commits;
   a release request needs its explicit artifact-sharing scope. Recheck HEAD and
   the staged patch before committing if another actor may have changed them.
3. Run relevant implemented checks. If unstaged later work can affect them,
   verify the staged snapshot in an isolated temporary checkout when needed,
   preserving the original index/worktree. A combined-worktree test does not
   prove every intermediate commit passes. Disclose validation limits; do not
   claim an unverified state is tested or commit a known broken split merely to
   increase commit count.
4. Write an accurate English message. Follow the established convention, otherwise
   use `type(scope): concrete behavior`: `feat`, `fix`, `refactor`, `test`, `docs`,
   `build`, `ci` or `chore`. Prefer a short, specific subject. Use the body for
   the reason, behavior and useful validation when needed. `update`, `changes`
   and `fix stuff` are insufficient complete explanations.
5. Commit the inspected group. Use separate `-m` arguments or a UTF-8 message
   file for multiline messages. Honor hooks; if they change files or fail,
   inspect the result and rerun affected checks instead of silently bypassing.
6. Inspect `git show --stat --oneline HEAD` and its actual patch. Repeat for the
   remaining groups. Recheck status; report SHAs/subjects and remaining work.
   If hooks or another actor change the staged set, inspect that change before
   retrying rather than automatically adding it to the next commit.

Amending old commits, squashing existing history, resetting/cleaning the worktree,
changing author identity and force-pushing are separate actions requiring their
own authorized scope, not shortcuts for ordinary commit work.

## Publish only when requested

For an authorized push, confirm the intended remote/branch and push the verified
sequence. Use branch tracking or an explicit destination to establish the target;
ask only when it is ambiguous, not merely to repeat an existing authorization.
A push-only request publishes existing commits rather than implicitly creating
new ones. Verify the remote ref equals the expected commit. On rejection because
the remote moved, inspect divergence and preserve both contributors' commits;
do not resolve it with a force-push. Report local commits separately from remote
publication or its failure.
