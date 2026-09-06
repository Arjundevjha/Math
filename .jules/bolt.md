## 2025-05-18 - Decimal Power Calculation Efficiency in Newton-Raphson `nth_root`

**Learning:**
In Python's C-accelerated `_decimal` module, computing `y ** (n - 1)` (where `n - 1` is `Decimal`) is highly optimized at C level using binary exponentiation algorithms when exponent is integer-valued or log/exp algorithms for arbitrary decimals.
Alternative formulations such as reformulating Newton-Raphson step as `y * (n - 1 + x / (y ** n)) / n` require computing $y^n$ (a higher degree power) and add an extra `Decimal` multiplication per iteration.
Benchmarking across standard precisions (50 to 2000 decimal places) showed that `y ** (n - 1)` direct power computation in `nth_root.py` remains optimal and faster than alternative reformulations.

**Action:**
Retain the current $y^{n-1}$ power term evaluation in `nth_root.py` while documenting quantitative performance characteristics across decimal precisions to avoid regressions or unnecessary arithmetic overhead.
