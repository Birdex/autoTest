# -*- coding: utf-8 -*-
import json

import time

from birdex_v2.IO import read
from birdex_v2.localTime import localTimeNum
from birdex_v2.requestMethod import post

dict_param = read('C:/Users/Administrator/Desktop/TestCases/orderforout/out_transorder-2.json')
dict_param['tradeOrders'][0]['logisticsOrder']['logisticsId'] = "xst" + str(localTimeNum())
dict_param['tradeOrders'][0]['paymentTime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
json_param = json.dumps(dict_param)
postResult = post(json_param,path='/OmsAdaptor/order/create')
print(postResult)