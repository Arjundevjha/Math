## 2026-09-07 - Unbounded Terms in Nilakantha Algorithm (DoS Risk)

**Vulnerability:** Unbounded iteration count and precision parameter inputs in numerical series algorithms (such as `calculate_pi_nilakantha`) can lead to high CPU and memory resource consumption, causing Denial of Service (DoS).
**Learning:** Functions that construct high-precision calculations or run loop-based series expansions must validate that numerical arguments (`terms`, `precision`) fall within reasonable upper limits (e.g. 1 to 10,000) and explicitly reject non-integer types (including booleans which inherit from `int`).
**Prevention:** Always enforce strict upper and lower bounds on user-supplied calculation parameters and type checks using `isinstance(x, int)` and `not isinstance(x, bool)`.
