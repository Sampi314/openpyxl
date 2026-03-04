## 2025-05-15 - Combined Micro-optimizations

**Learning:** Significant performance wins can be achieved by targeting high-frequency operations in the core of openpyxl: cell access, value binding, and utility list lookups.

1. **Worksheet._get_cell**: Replacing double lookup (`in` then `[]`) with a single `.get()` call improves existing cell access by ~27%. Deferring row validation to the cell creation path further streamlines the hot path.
2. **Cell._bind_value**: Pre-populating the `_TYPES` cache with `type(None)` avoids redundant calls to `get_type` for empty cells. Using a `frozenset` for `ERROR_CODES` provides O(1) lookups during string binding.
3. **IndexedList**: Replacing `if x in self: return self._dict[x]` with a `try-except KeyError` pattern in `index()` and using `.get()` in `add()` halves the number of dictionary lookups in these methods, benefiting style and shared string management.

**Action:** Always look for double-lookup patterns in dictionaries and consider pre-populating type caches for common types like `NoneType`.
