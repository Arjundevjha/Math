## 2025-05-18 - Replacing Repeated Append in Loop with List Comprehension

**Learning:** Replacing iterative `for` loops that repeatedly invoke `list.append()` with C-optimized list comprehensions reduces loop overhead and function call dispatch cost in Python. Additionally, moving invariant or early-exit checks (such as verifying `-1` is not in powers) prior to building lists avoids redundant list allocations during error conditions and simplifies the evaluation loop.
**Action:** Use list comprehensions and early-exit membership checks (`if -1 in powers:`) instead of `for` loops with `.append()` when constructing transformation lists in mathematical functions.
