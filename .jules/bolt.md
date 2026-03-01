## 2025-05-15 - [Optimization] Double Lookup in High-Frequency Paths
**Learning:** High-frequency operations like accessing cells or binding values often used double dictionary lookups (e.g., `if key in dict: return dict[key]`). In Python, this doubles the hash calculation and search overhead.
**Action:** Use `dict.get(key)` or `try-except KeyError` (EAFP) to perform a single lookup, especially in core classes like `Worksheet`, `Cell`, and `IndexedList`.
