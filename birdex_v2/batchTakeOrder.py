import copy
import json
import postgresql.driver as pg_driver
import xlrd


from birdex_v2.IO import read, writeTXT
from birdex_v2.localTime import myOrderNum
from birdex_v2.requestMethod import post


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

def takeXLS(fileName='D:/PycharmProjects/BirdexTestForPython/birdex_v2/TKOrder.xlsx'):
    xls = xlrd.open_workbook(fileName)
    try:
        sheet = xls.sheet_by_name("Sheet1")
    except:
        print("no sheet in %s named Sheet1" % fileName)
    nrows = sheet.nrows
    ncols = sheet.ncols
    print("nrows %d, ncols %d" % (nrows, ncols))
    takeList = []
    takeOrder = read('D:/workspace/BirdexTest/TKOrderSchema.txt')
    for i in range(1, nrows):
        takeOrder['areaCode'] = readCell(sheet.cell(i, 0))
        takeOrder['takeType'] = readCell(sheet.cell(i, 1))
        takeOrder['warehouse'] = readCell(sheet.cell(i, 2))
        takeOrder['procTK']['express']['no'] = readCell(sheet.cell(i, 3))
        takeOrder['procTK']['parcels'][0]['items'][0]['count'] = int(sheet.cell(i, 4).value)
        takeOrder['procTK']['parcels'][0]['items'][0]['ext']['batch'] = readCell(sheet.cell(i, 5))
        takeOrder['procTK']['parcels'][0]['items'][0]['ext']['brand'] = readCell(sheet.cell(i, 6))
        takeOrder['procTK']['parcels'][0]['items'][0]['ext']['category'] = readCell(sheet.cell(i, 7))
        takeOrder['procTK']['parcels'][0]['items'][0]['ext']['comments'] = readCell(sheet.cell(i, 8))
        takeOrder['procTK']['parcels'][0]['items'][0]['ext']['pName'] = readCell(sheet.cell(i, 9))
        takeOrder['procTK']['parcels'][0]['items'][0]['ext']['upc'] = readCell(sheet.cell(i, 10))
        takeOrder['procTK']['parcels'][0]['items'][0]['mCode'] = readCell(sheet.cell(i, 11))
        takeOrder['procTK']['parcels'][0]['items'][0]['mName'] = readCell(sheet.cell(i, 12))
        takeOrder['procTK']['parcels'][0]['items'][0]['price'] = sheet.cell(i, 13).value
        takeOrder['procTK']['parcels'][0]['no'] = readCell(sheet.cell(i, 14))
        takeOrder['procTK']['person']['co'] = readCell(sheet.cell(i, 15))
        takeOrder['procTK']['person']['contact']['address'] = readCell(sheet.cell(i, 16))
        takeOrder['procTK']['person']['contact']['post'] = readCell(sheet.cell(i, 17))
        takeOrder['procTK']['person']['contact']['phone'] = readCell(sheet.cell(i, 18))
        takeOrder['procTK']['person']['contact']['ext']['mobile'] = readCell(sheet.cell(i, 19))
        takeOrder['procTK']['person']['contact']['ext']['email'] = readCell(sheet.cell(i, 20))
        takeOrder['procTK']['person']['contact']['ext']['note'] = readCell(sheet.cell(i, 21))
        takeOrder['procTK']['person']['contact']['identityCard'] = readCell(sheet.cell(i, 22))
        takeOrder['procTK']['person']['name'] = readCell(sheet.cell(i, 23))
        # list.append(takeOrder)
        takeList.append(copy.deepcopy(takeOrder))
        # print(takeOrder)
    return takeList

def executeBatchTake(takeList):
    for takeOrder in takeList:
        takeOrder["procTK"]["express"]["no"] = myOrderNum()
        postResult = json.loads(post(json.dumps(takeOrder)))
        print("postResult:" + json.dumps(postResult, ensure_ascii=False))
        writeTXT(json.dumps(postResult))
        orderNo = postResult['orderNo']
        result = postResult['result']
        db = pg_driver.connect(database="postgres", user="postgres", password="password", host="localhost", port="5432")
        db.execute('''create table IF NOT EXISTS take_result("orderNo" varchar(64), "result" text)''')
        db.execute('''insert into take_result values (orderNo,result)''')
    db.close()
