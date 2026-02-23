# Bolt's Performance Journal - openpyxl

## 2025-05-14 - Performance patterns in openpyxl

**Learning:** Frequently called utility functions like `is_date_format` in `openpyxl/styles/numbers.py` perform expensive regex operations. Since Excel files often reuse the same formats across many cells, these results are highly cacheable.
**Action:** Use `functools.lru_cache` on such functions.

**Learning:** `BUILTIN_FORMATS.values()` in Python 3 returns a view, and membership testing (`in`) against it is O(n).
**Action:** Use a dictionary or set for O(1) membership testing.

**Learning:** Constant lookup tables like `ERROR_CODES` in `openpyxl/cell/cell.py` are often implemented as tuples.
**Action:** Use `frozenset` for faster membership testing if the number of elements is more than a few.
