## 2026-09-07 - Unbounded Precision in Decimal nth_root Calculation (DoS Risk)

**Vulnerability:** Allowing an arbitrary or unbounded `precision` parameter when setting `decimal.getcontext().prec` in `nth_root()` allows malicious or accidental excessive allocation of CPU time and RAM, leading to Denial of Service (DoS) or process crash.

**Learning:** Unrestricted precision setting in Python's `decimal` module can cause extreme memory consumption and high execution times when computing arithmetic or iterative calculations (like Newton-Raphson method for root finding). Additionally, non-integer or boolean types (since `bool` inherits from `int`) must be explicitly validated to prevent bypasses.

**Prevention:** Enforce strict type validation (`isinstance(precision, int)` and `not isinstance(precision, bool)`) and explicit lower/upper numeric bounds (e.g., `1 <= precision <= 10000`) before calling `getcontext().prec = precision`.
