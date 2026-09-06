## 2025-05-18 - Sliced active pentagonals for partition function

**Learning:** In hot DP loops that accumulate terms based on sequence boundaries (like Euler's pentagonal number theorem in `partition(n)`), checking bounds (`if g > i: break`) or iterating over inactive indices adds CPU overhead. Incrementally adding pentagonal numbers to active lists as `i` reaches `g`, and splitting into addition and subtraction lists (`active_pos` and `active_neg`), eliminates loop branch checks, removes sign multiplication (`total += sign * ...`), and significantly boosts performance.

**Action:** Maintain `active_pos` and `active_neg` lists, updating them only when `i` reaches new pentagonal boundaries `g`, and iterate directly over each list in separate tight loops.
