## 2025-05-18 - Iterative Binomial Coefficient Calculation

**Learning:** Recomputing binomial coefficients $C(n, r)$ independently in a loop via $nCr$ costs $O(r)$ work per term, summing to $O(n^2)$ total operations for expanding a binomial $(a+b)^n$. Using recurrence $C(n, r) = C(n, r-1) \times (n - r + 1) // r$ allows $O(1)$ updates per coefficient, reducing total expansion complexity to $O(n)$.

**Action:** Update binomial theorem expansion loops to calculate terms iteratively using previous coefficient state rather than recalculating combinations from scratch.
