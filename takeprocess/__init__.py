# -*- coding: utf-8 -*-
import json

import time

from birdexv2.IO import read, readTemp
from birdexv2.local_time import localTimeNum
from birdexv2.request_method import post

# 读取揽收和揽收结果数据格式
dict_takeOrder = read('D:/workspace/BirdexTest/TKOrderSchema.txt')
report = read('D:/workspace/BirdexTest/report.txt')
# 设置参数具体值
dict_takeOrder['procTK']['express']['no'] = 'XST' + str(localTimeNum())
# dict_upResult['parcels'] = dict_takeOrder['procTK']['parcels']
# print(json.dumps(dict_upResult,ensure_ascii=False,indent=2))

# 揽收成功，揽收清点成功
dict_takeOrder['isCount'] = True
postResult = post(json.dumps(dict_takeOrder))
print("TakeTest result:", postResult)
dict_postResult = json.loads(postResult)
if ('orderNo' in postResult) & (dict_postResult['result'] == 'success'):
    report['resultBasic']['omsOrderNo'] = dict_postResult['orderNo']
    report['resultBasic']['result'] = 'success'
    time.sleep(0.1)
    postResult = post(json.dumps(report), ip='192.168.1.197:8080', path='/OmsAgent/TakeReport/')
    print("TakeReport result:", postResult)
    dict_postResult = json.loads(postResult)
    if dict_postResult['result'] == 'success':
        time.sleep(0.1)
        postResult = post(json.dumps(report), ip='192.168.1.197:8080', path='/OmsAgent/TakingCountingReport/')
        print("TakeCountReport result:", postResult)
        dict_postResult = json.loads(postResult)
        if dict_postResult['result'] =='success':
            assert True
        else:
            print("TakeCountReport fail")
            assert False
    else:
        print("TakeReport fail")
        assert False
else:
    print("TakeCreate fail")
    assert False
print("Test end")

