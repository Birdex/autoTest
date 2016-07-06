# -*- coding: utf-8 -*-
import json

from birdex_v2.IO import read
from birdex_v2.localTime import localTimeNum
from birdex_v2.requestMethod import post

dict_param = read('C:/Users/Administrator/Desktop/TestCases/orderforout/out_takingorder-0.json')
dict_param['tradeOrders'][0]['trackingNo'] = "xst" + str(localTimeNum())
json_param = json.dumps(dict_param)
postResult = post(json_param,path='/OmsAdaptor/package/create')
print(postResult)