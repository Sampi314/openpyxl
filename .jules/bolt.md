# Bolt's Performance Journal

## 2025-05-14 - [Initial Critical Learnings]
**Learning:**
- Identified architectural bottlenecks: XML parsing and descriptor-based 'Serialisable' system.
- functools.lru_cache provides significant speedups for format-checking functions (up to 15x).
- Constant lookup tables should be frozensets for O(1) membership checks.
- BUILTIN_FORMATS_REVERSE provides O(1) membership test for builtin formats.
- node.tag.rpartition('}')[-1] is faster than regex for XML local name extraction.
- Using PYTHONDONTWRITEBYTECODE=1 avoids environment pollution from tracked __pycache__ files.

**Action:**
- Prioritize small (<50 lines), measurable wins.
- Measure first, optimize second.
- Document impact in PR descriptions.
- Use the identified patterns (lru_cache, frozenset, rpartition) where applicable.
