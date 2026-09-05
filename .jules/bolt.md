## 2025-05-18 - Binary search for inverse monotonic functions (arcsin)
**Learning:** Numerical search for inverse trigonometric functions (like arcsin) on monotonic domains (e.g., [0, π/2]) using incremental linear steps (O(1/step)) suffers from thousands of expensive Taylor series iterations. Binary search (bisection method) reduces iterations to ~25 with O(log(1/eps)) complexity.
**Action:** When finding roots or inverse function approximations for monotonic mathematical functions, use binary search (bisection) instead of linear scan.
