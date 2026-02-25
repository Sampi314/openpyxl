# Bolt's Performance Journal

## 2025-05-22 - [Optimized IndexedList for faster lookups]
**Learning:** Double dictionary lookups in core utility classes like `IndexedList` can be a significant bottleneck when processing large files with many unique strings or styles. Replacing "check then retrieve" with "get with default" or "try-except" (EAFP) improves performance by ~20%.
**Action:** Always prefer single lookup patterns in core data structures.

## 2025-05-22 - [Pre-populating _TYPES for None values]
**Learning:** `None` values are extremely frequent in Excel files. Pre-populating lookup tables for `type(None)` avoids repeated expensive type inference calls.
**Action:** Ensure common types like `NoneType` are cached in type mapping dictionaries.

## 2025-05-22 - [Frozenset for constant lookups]
**Learning:** Converting constant lookup tables from tuples to frozensets provides a measurable speed boost (~2.5x to 4x faster) for frequent membership checks.
**Action:** Use `frozenset` for any constant set of values used in membership tests (e.g., `ERROR_CODES`).
