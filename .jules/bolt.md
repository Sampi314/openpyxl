# Bolt's Performance Journal

## 2025-05-22 - [Format Check Optimization]
**Learning:** Functions like `is_date_format` and `is_builtin` are called millions of times during workbook processing. Regex-based checks in `is_date_format` are particularly expensive when repeated for the same format strings.
**Action:** Use `functools.lru_cache` for expensive format validation and O(1) dictionary/set lookups for membership tests.

## 2025-05-22 - [Membership Lookup Optimization]
**Learning:** `ERROR_CODES` was defined as a tuple, leading to O(n) lookup time. Converting to `frozenset` provides O(1) lookup.
**Action:** Always prefer `frozenset` or `set` for static membership lookups.
