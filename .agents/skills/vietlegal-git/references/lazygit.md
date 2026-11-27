# Optional Lazygit staging

[Lazygit](https://github.com/jesseduffield/lazygit) provides an interactive Git
view, including hunk/line staging. Use it when requested and available with a
usable terminal. Automated work can use ordinary Git; installation is unnecessary
for the skill. Check installed on-screen help because keybindings can differ.

The upstream README's staging example uses:

| Key in the relevant view | Action |
| --- | --- |
| `0` on a changed file | Focus its diff |
| `Space` in the diff | Stage the selected hunk |
| `a` | Select individual lines |
| `v` | Select a line range |
| `Tab` | Switch staged/unstaged panes |
| `c` | Open committing from the diff |

Select only the current commit's changes and inspect the staged pane. Apply the
same coherent-group and message rules as the Git skill. Verify the resulting
index with `git diff --cached` and `git diff --cached --check` before committing.
TUI access does not authorize resetting, rewriting history or pushing.

Source: [upstream staging documentation](https://github.com/jesseduffield/lazygit#stage-hunks-or-individual-lines).
