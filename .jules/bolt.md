## 2025-05-15 - [Format and Error Code Checking Optimizations]
**Learning:** Frequently called format-checking functions (like `is_date_format`) that use regex or string splitting are prime candidates for `lru_cache`, providing up to 15x speedups. Constant lookup tables should always use `frozenset` or existing reverse-lookup dictionaries for O(1) membership tests.
**Action:** Always check if a frequently used lookup table can be converted to a set/frozenset, and apply `lru_cache` to pure functions that perform expensive string or regex operations.

## 2025-05-15 - [Tracked Artifacts Warning]
**Learning:** This repository has tracked `__pycache__` files. Deleting them registers as a git deletion, which pollutes the diff.
**Action:** Do NOT delete `__pycache__` folders in this repo. Use `PYTHONDONTWRITEBYTECODE=1` to avoid creating new ones, and `git restore` if any were accidentally deleted.
