## 2024-05-15 - Initial Performance Observations
**Learning:** Initial assessment of the openpyxl codebase reveals several areas where performance has been improved, such as optimizing `Worksheet._get_cell`, using `frozenset` for error codes, and using `functools.lru_cache` for format checking.
**Action:** Continue to look for similar patterns of redundant lookups, repeated regex processing, and inefficient membership tests.

## 2024-05-15 - XML Parsing Optimization
**Learning:** `node.tag.rpartition('}')[-1]` is significantly faster (~65%) than regex-based extraction for local names in XML parsing.
**Action:** Look for any remaining regex-based local name extractions in XML parsing code.

## 2024-05-15 - Lookup Optimizations
**Learning:** Single dictionary lookups (using `.get()` or `try-except`) are faster than double lookups (`if key in dict: return dict[key]`).
**Action:** Audit high-frequency methods for double lookups.

## 2024-05-15 - IndexedList Optimization
**Learning:** Optimizing `IndexedList` in `openpyxl/utils/indexed_list.py` by replacing double dictionary lookups with single lookups (EAFP pattern with try-except in `index` and `.get()` in `add`) provides a measurable speedup during shared string and style management. Measured ~50% improvement in `add` and `index` operations.
**Action:** Apply similar single-lookup patterns to other performance-critical classes using dictionary lookups.
