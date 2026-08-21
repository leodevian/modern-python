---
name: test-coverage-audit
description: Find meaningful missing pytest coverage and add focused tests.
argument-hint: Optional module or coverage concern
---

# Test Coverage Audit

Start with `make coverage`, then inspect uncovered behavior alongside its tests.
Prioritize branches, validation, error paths, and public behavior. Avoid adding
tests only to execute trivial lines. Record source bugs for a separate fix task.
