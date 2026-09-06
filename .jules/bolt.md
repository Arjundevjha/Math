## 2025-05-18 - Euler's pentagonal recurrence loop optimization
**Learning:** In sequence recurrences with growing bounds and alternating signs (e.g. Euler's pentagonal theorem for integer partitions), incrementally appending terms to separate positive and negative active term lists as thresholds are reached eliminates inner loop branching checks (`if g > i`) and sign multiplication overhead.
**Action:** When evaluating recurrence relations over precomputed or sequence-indexed lookup offsets, partition terms by sign/contribution and maintain active term sets to simplify inner loop arithmetic.
