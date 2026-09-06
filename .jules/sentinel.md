# Sentinel Security Learnings

## 2026-09-06 - Unbounded Input in Decimal Factorial Calculation (DoS Risk)

**Vulnerability:**
`factorial_decimal(n)` in `Math/utils/math_utils.py` accepted arbitrarily large integer inputs `n` without validating upper bounds, allowing callers to trigger expensive iterative multiplications with `Decimal` objects. Computing factorials for extremely large integers consumes CPU time and memory proportionally, creating a Denial of Service (DoS) vector.

**Learning:**
Mathematical calculation utilities handling arbitrary-precision types (such as Python big-ints or `decimal.Decimal`) must strictly validate inputs and enforce upper bound constraints. In addition, input type checks should disallow non-integer types (e.g. booleans, floats, strings) to prevent unexpected type coercion or errors.

**Prevention:**
Enforce strict input type validation (`isinstance(n, bool)` check before `isinstance(n, int)`) and a reasonable upper bound threshold (`n <= 100000`) at the function entry point before processing mathematical operations.
