
import timeit
from openpyxl.utils.indexed_list import IndexedList

def benchmark_indexed_list():
    # Setup
    data = [f"value_{i}" for i in range(1000)]
    il = IndexedList(data)

    # Values already in list
    existing_values = data[::10]
    # Values NOT in list
    new_values = [f"new_value_{i}" for i in range(100)]

    def check_contains():
        for v in existing_values:
            v in il

    def check_index():
        for v in existing_values:
            il.index(v)

    def add_existing():
        for v in existing_values:
            il.add(v)

    print(f"Contains (existing): {timeit.timeit(check_contains, number=1000):.4f}s")
    print(f"Index (existing): {timeit.timeit(check_index, number=1000):.4f}s")
    print(f"Add (existing): {timeit.timeit(add_existing, number=1000):.4f}s")

if __name__ == "__main__":
    benchmark_indexed_list()
