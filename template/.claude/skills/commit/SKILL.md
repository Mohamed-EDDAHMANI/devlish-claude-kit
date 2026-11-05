---
name: commit
description: Write a clean commit for the current changes. Use when asked to commit.
---

# Commit

1. Run `git status` and `git diff` to see what changed.
2. If the changes do unrelated things, propose separate commits.
3. Stage files by name. Never stage secrets or build output.
4. Write the message:
   - First line under 72 characters, in the imperative: "Fix login redirect"
   - Add a body only if the reason isn't obvious. Explain why, not what.
5. Match the style of `git log --oneline -10`.

Don't push unless asked.
