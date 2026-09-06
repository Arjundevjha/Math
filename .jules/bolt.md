## 2025-05-18 - Hoist Decimal Instantiation in Loop

**Learning:** Creating `Decimal` objects (e.g. `Decimal(4.0)`) inside tight loop iterations incurs heavy object instantiation and precision context conversion overhead in Python's `decimal` module.
**Action:** Always hoist invariant `Decimal` constants outside `for`/`while` loops in numerical computation routines.
