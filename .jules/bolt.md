## 2025-05-15 - Optimizing Core Cell Binding
**Learning:** Pre-populating type caches and using frozensets for small constant lookups significantly reduces overhead in hot paths like `Cell._bind_value`. Binding `None` became ~81% faster.
**Action:** Always check for redundant `type(None)` or subclass checks in frequently called methods and consider pre-populating lookup dictionaries.

**Learning:** Be extremely careful when running tests or benchmarks that generate `__pycache__` files in repositories that mistakenly track them.
**Action:** Always use `PYTHONDONTWRITEBYTECODE=1` when running Python in such environments and use `git checkout -- .` to restore any accidentally deleted tracked artifacts.
