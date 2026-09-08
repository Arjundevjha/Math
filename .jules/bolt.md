## 2025-02-18 - Decimal Exponentiation in Newton-Raphson nth_root Iteration

**Learning:**
In Python's C-accelerated `_decimal` module (`libmpdec`), computing $y^{n-1}$ directly via `y_dec ** n_minus_one_dec` is faster than reformulating Newton-Raphson iteration to compute $y^n$ directly (e.g. `(y_dec ** n_dec) / y_dec` or `(x_dec * y_dec) / (y_dec ** n_dec)`).

In `libmpdec`, arbitrary Decimal exponentiation $y^p$ employs C-level binary exponentiation / LN-EXP approximations. Computing $y^n$ instead of $y^{n-1}$ requires the same high-precision exponentiation cost while introducing additional high-precision `Decimal` divisions/multiplications per Newton-Raphson iteration. Benchmarks across precision levels (50 to 1000 digits) show:
- `y_dec ** (n_dec - 1)` [Current]: ~0.054s (precision 50), ~2.42s (precision 1000)
- `(y_dec ** n_dec) / y_dec` [Reformulation 1]: ~0.055s (+2.5%), ~3.68s (+52.0%)
- `(x_dec * y_dec) / (y_dec ** n_dec)` [Reformulation 2]: ~0.049s (-8.6% at low precisions), ~3.07s (+26.7% at high precisions)

**Action:**
Keep the existing `y_dec ** n_minus_one_dec` implementation in `Math/Numerical_Methods/Functions/nth_root/nth_root.py` to prevent performance degradation at high Decimal precisions.
