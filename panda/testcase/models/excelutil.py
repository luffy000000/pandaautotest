import xlrd

class ExcelUtil():
    def __init__(self, excel_path, sheet_name):
        self.data = xlrd.open_workbook(excel_path)
        self.table = self.data.sheet_by_name(sheet_name)
        self.keys = self.table.row_values(0)
        self.rowNum = self.table.nrows
        self.colNum = self.table.ncols

    def dict_data(self):
        if self.rowNum <= 1:
            print('总行数小于１')
        else:
            r = []
            j = 1
            for i in range(self.rowNum - 1):
                s = {}
                values = self.table.row_values(j)
                for x in range(self.colNum):
                    s[self.keys[x]] = values[x]
                r.append(s)
                j += 1
            return r
