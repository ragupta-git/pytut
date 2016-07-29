__author__ = 'ragupta4'

def generate_xl(month):
    import xlwt
    wbk = xlwt.Workbook()
    sheet = wbk.add_sheet(month)
    row = 0
    line = ["EmpId", "Name", "Date", "Entry", "Exit", "Duration"]
    xlwt.easyxf('font: bold on')
    for col, value in enumerate(line):
        sheet.write(row, col, value)

    wbk.save('test.xls')

generate_xl("test")