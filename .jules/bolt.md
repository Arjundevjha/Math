## 2026-09-08 - Eliminating per-iteration sign-multiplying and Decimal conversions in Nilakantha series

**Learning:** In Python's `decimal` module, multiplying integer signs (`sign * Decimal(...)` or `sign *= -1`) within tight mathematical series loops triggers redundant `Decimal` object type conversions and multiplications on every iteration.
**Action:** Pre-allocate positive and negative `Decimal` constant terms (e.g., `four = Decimal(4)` and `neg_four = Decimal(-4)`) and swap their variable references (`curr_four, neg_four = neg_four, curr_four`) in the loop to eliminate intermediate sign multiplications without creating new `Decimal` instances or altering floating-point result precision.
