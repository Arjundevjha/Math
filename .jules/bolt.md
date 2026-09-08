# Bolt Performance Documentation

## 2025-05-20 - Polynomial Integration List Comprehension Optimization

**Learning:**
In Python, repeatedly validating exception conditions inside a loop and appending to list objects via `list.append()` incurs significant interpreter overhead. Hoisting `if -1 in powers` outside the loop and replacing list append loops with list comprehensions leverages C-level evaluation in CPython, reducing runtime.

**Action:**
When transforming input sequences into output sequences in mathematical utilities (such as polynomial integration), hoist invariant error checks out of the loop and utilize optimized list comprehensions.
