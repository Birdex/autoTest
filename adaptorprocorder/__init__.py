# -*- coding: utf-8 -*-
import json

import time

from birdexv2.IO import read
from birdexv2.local_time import localTimeNum
from birdexv2.request_method import post

dict_param = read('C:/Users/Administrator/Desktop/TestCases/orderforout/out_transorder-2.json')
dict_param['tradeOrders'][0]['logisticsOrder']['logisticsId'] = "xst" + str(localTimeNum())
dict_param['tradeOrders'][0]['paymentTime'] = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
json_param = json.dumps(dict_param)
postResult = post(json_param,path='/OmsAdaptor/order/create')
print(postResult)