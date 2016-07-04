import xlrd
import xlwt
import time

case = {'caseID': '', 'title': '', 'term': '', 'op': '', 'except': '', 'result': '','version': '', 'billing': '', 'note': ''}
fname = 'E:/birdex/TestCases/AutoTestCase.xls'
bk = xlrd.open_workbook(fname)
try:
    sh = bk.sheet_by_name("Sheet1")
except:
    print("no sheet in %s named Sheet1" % fname)
nrows = sh.nrows
ncols = sh.ncols
print("nrows %d, ncols %d" % (nrows, ncols))
list = []
case1 = {'name':''}
test = []
case1['name'] = 'test1'
test.append(case1)
print(test)
case1['name'] = 'test2'
test.append(case1)
print(test)

for i in range(1, nrows):
        case['caseID'] = sh.cell_value(i, 0)
        case['title'] = sh.cell(i, 1)
        case['term'] = sh.cell(i, 2)
        case['op'] = sh.cell(i, 3)
        case['except'] = sh.cell(i, 4)
        case['result'] = sh.cell(i, 5)
        case['version'] = sh.cell(i, 6)
        case['billing'] = sh.cell(i, 7)
        case['note'] = sh.cell(i, 8)
        list.append(case)
        print(case)

print()
print(list)
for element in list:
    print(element)