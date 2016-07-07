import xlrd

def readCell(cell):
    if cell.ctype == 2:
        return str(int(cell.value))
    elif cell.ctype == 3:
        return str(xlrd.xldate.xldate_as_datetime(cell.value, 0))
    elif cell.ctype == 4:
        if cell.value:
            return True
        else:
            return False
    else:
        return cell.value

case = {'caseID': '', 'title': '', 'term': '', 'op': '', 'except': '', 'result': '','version': '', 'billing': '', 'note': ''}
fname = 'E:/birdex/TestCases/AutoTestCase.xls'
# fname = 'TKOrder.xlsx'
bk = xlrd.open_workbook(fname)
try:
    sheet = bk.sheet_by_name("Sheet1")
except:
    print("no sheet in %s named Sheet1" % fname)
nrows = sheet.nrows
ncols = sheet.ncols
print("nrows %d, ncols %dsh.cell(i, 0)" % (nrows, ncols))
list = []
for i in range(0, ncols):
    print(sheet.cell(1, i).ctype)

for i in range(1, nrows):
    # case['caseID'] = sh.cell(i, 0).value
    case['caseID'] = readCell(sheet.cell(i, 0))
    case['title'] = readCell(sheet.cell(i, 1))
    case['term'] = readCell(sheet.cell(i, 2))
    case['op'] = readCell(sheet.cell(i, 3))
    case['except'] = readCell(sheet.cell(i, 4))
    case['result'] = readCell(sheet.cell(i, 5))
    case['version'] = str(sheet.cell(i, 6).value)
    case['billing'] = readCell(sheet.cell(i, 7))
    case['note'] = readCell(sheet.cell(i, 8))
    # list.append(case)
    list.append(case.copy())
    print(case)
print()
for element in list:
    print(element)

