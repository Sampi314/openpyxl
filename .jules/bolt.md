## 2025-05-15 - Cell and IndexedList Lookups
**Learning:** Pre-populating type caches and using EAFP (Easier to Ask for Forgiveness than Permission) patterns with try-except for dictionary lookups provides significant speedups in hot paths like cell binding and shared string management.
**Action:** Always look for double dictionary lookups (e.g., `if key in dict: return dict[key]`) and replace them with single lookups (e.g., `try-except` or `.get()`) in performance-critical code.
