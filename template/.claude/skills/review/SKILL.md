---
name: review
description: Review the current changes for real bugs before a commit or a pull request. Use when asked to review or check code.
---

# Review

1. Run `git diff` and `git diff --staged` to see the changes.
2. Read the surrounding code, not only the changed lines.
3. Look for, in this order:
   - Wrong logic and unhandled edge cases
   - Security problems: unchecked input, exposed secrets, missing auth checks
   - Broken callers of anything that changed
   - Missing tests for new behaviour
4. Report each problem with its file, its line and a concrete case that fails.

Skip style opinions. If nothing is wrong, say so.
