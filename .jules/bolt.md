## 2025-05-22 - Optimize IndexedList lookups
**Learning:** Replacing 'if value in self: return self._dict[value]' with a try-except block and using '.get()' in 'add()' reduces redundant dictionary lookups. This 'Easier to Ask Forgiveness than Permission' (EAFP) pattern is faster in Python when the success case is common.
**Action:** Use single-lookup patterns (EAFP or .get()) for performance-critical dictionary operations.
