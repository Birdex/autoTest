# -*- coding: utf-8 -*-
import json
import time
from birdex_v2.readFile import read
from birdex_v2.now import now
from birdex_v2.requestMethod import post, get

# 读取揽收和揽收结果数据格式
dict_takeOrder = read('E:/birdex/TestCases/outPort/outProcOrder.txt')
report = read('D:/workspace/BirdexTest/report.txt')
# 设置参数具体值
dict_takeOrder['tradeOrders'][0]['trackingNo'] = 'XST' + str(now())
dict_takeOrder['tradeOrders'][0]['logisticsOrder']['logisticsId'] = 'xieshitong' + str(now())
dict_takeOrder['tradeOrders'][0]['paymentTime'] = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

postResult = post(json.dumps(dict_takeOrder), path='/OmsAdaptor/order/create/')
dictResult = json.loads(postResult)
print("postResult:" + json.dumps(dictResult, ensure_ascii=False))
time.sleep(0.1)
if 'orderNo' in postResult:
    getResult = json.loads(get(postResult['orderNo']))
    print("getResult:" + json.dumps(getResult, ensure_ascii=False))
else:
    print(postResult)