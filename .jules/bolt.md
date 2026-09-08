## 2026-09-07 - Optimizing Pentagonal Recurrence for Integer Partitions

**Learning:** When evaluating sequence recurrences with growing bounds and alternating signs (e.g. Euler's pentagonal theorem for integer partitions), maintaining active terms in separate positive and negative lists eliminates inner loop branching checks (`if g > i`) and sign multiplication overhead. Storing scalar `next_pos` and `next_neg` boundary values further avoids array index bounds checks inside the loop.

**Action:** Separate pentagonal numbers into positive and negative terms, accumulate active terms as thresholds are reached, and track boundary values in scalars.
