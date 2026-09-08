## 2026-09-08 - Unbounded Input in Factorial Calculation (DoS)

**Vulnerability:**
Unbounded integer inputs (`n`) passed to `factorial()` and `factorial_decimal()` allow callers to trigger CPU and memory exhaustion (Denial of Service) via huge factorial calculations or deep recursive splits.

**Learning:**
Mathematical utilities that compute unbounded sequence products or powers must enforce strict input parameter upper bounds to protect against algorithmic complexity and resource exhaustion attacks.

**Prevention:**
Validate input types strictly (`isinstance(n, int)` and `not isinstance(n, bool)`) and enforce explicit upper boundary checks (`if n > 100000: raise ValueError(...)`) before processing expensive operations.
