import timeit
from openpyxl import Workbook
from openpyxl.worksheet.worksheet import Worksheet
from openpyxl.cell import Cell

def benchmark_get_cell():
    wb = Workbook()
    ws = wb.active
    # Pre-populate some cells
    for r in range(1, 101):
        for c in range(1, 101):
            ws.cell(row=r, column=c, value=r*c)

    # Benchmark access to existing cells
    def access_cells():
        for r in range(1, 101):
            for c in range(1, 101):
                ws._get_cell(r, c)

    t = timeit.timeit(access_cells, number=100)
    print(f"Time for 100 iterations of accessing 10000 cells: {t:.4f}s")

if __name__ == "__main__":
    benchmark_get_cell()
