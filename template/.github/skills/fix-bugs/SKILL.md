---
name: fix-bugs
description: Fix confirmed bugs with focused regression tests.
argument-hint: Optional bug or module to fix
---

# Fix Bugs

Confirm the bug against current source, make the smallest focused change, add
a regression test that fails before the fix, and run `make lint` and `make test`.
Do not mix unrelated refactors or test-audit work into a bug fix.
