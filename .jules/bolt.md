## 2025-05-18 - Decimal Creation in Ramanujan Loop

**Learning:** Replacing intermediate `Decimal` instantiations for integers inside high-precision loops (e.g. `Decimal(1103 + 26390 * k)` or `Decimal((4*k + 4) * ...)` or `Decimal(next_k**4) * Decimal(...)`) with native integer arithmetic multiplied directly against `Decimal` variables avoids repeated instantiation overhead and costly Decimal-by-Decimal division operations.

**Action:** Perform integer multiplication/division directly on `Decimal` loop terms (e.g., `term_multiplier = (term_multiplier * num_int) / den_int`) rather than casting each integer term to `Decimal` objects before arithmetic operations.
