---
name: bug-hunt
description: Find the root cause of a bug step by step instead of guessing. Use for errors, crashes and wrong behaviour.
---

# Bug hunt

1. Reproduce the bug and write down the exact steps and error.
2. Read the full error and the code it points to.
3. State one hypothesis about the cause.
4. Test it with a log, a small script or a failing test.
5. If it is wrong, drop it and form a new one. Don't stack fixes.
6. Fix the root cause, not the symptom.
7. Confirm the original steps now work, then remove debug code.

After three failed hypotheses, stop and report what you learned.
