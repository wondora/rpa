from openpyxl import Workbook

wb = Workbook()
ws = wb.active #현재 활성화된 워크시크 가져옴
ws.title = "NadoSheet"
wb.save("sample.xlsx")
ws.close()