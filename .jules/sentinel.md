## 2026-09-06 - Unbounded Terms in Ramanujan Algorithm (DoS Risk)

**Vulnerability:**
Accepting unbounded or excessively large `num_terms` input in iterative mathematical series computations allows potential Denial of Service (DoS) attacks via CPU and memory exhaustion.

**Learning:**
Bounding series iterations (e.g. `1 <= num_terms <= 10000`) and validating input types (ensuring integers, rejecting booleans and floats) prevents computational resource exhaustion while preserving accurate series evaluation.

**Prevention:**
Always validate all user-controlled numeric parameters for both valid data types and upper/lower bounds before executing iterative algorithms or modifying global execution context like `decimal.getcontext().prec`.
