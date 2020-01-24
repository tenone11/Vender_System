import time
from datetime import date
import openpyxl
wb = openpyxl.load_workbook(filename='E:\\Test\\模拟供应商统计.xlsx')
ws = wb.active
var = ws.cell(13, 16).value
# var = date.isoformat(var)
print(isinstance(var, float))

