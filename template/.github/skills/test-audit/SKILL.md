---
name: test-audit
description: Audit pytest coverage and quality against the package source.
argument-hint: Optional module or test concern
---

# Test Audit

Review public behavior, error paths, and meaningful edge cases. Prefer shared
fixtures, factory helpers, parametrization, and short behavioral assertions.
Do not test trivial implementation details. If an audit reveals a source bug,
record it for a separate bug-fixing task instead of fixing it here.
