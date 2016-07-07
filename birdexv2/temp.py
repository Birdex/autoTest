# -*- coding: utf-8 -*-
import json

from birdexv2.IO import read
from birdexv2.local_time import localTimeNum
from birdexv2.request_method import post

# 读取揽收和揽收结果数据格式
dict_param = read('D:/workspace/BirdexTest/TKOrderSchema.txt')
dict_upResult = read('D:/workspace/BirdexTest/upResult.txt')
# 设置参数具体值
dict_param['procTK']['express']['no'] = 'XST' + str(localTimeNum())
dict_upResult['parcels'] = dict_param['procTK']['parcels']

print(dict_upResult['parcels'])
print(dict_upResult)
print(json.dumps(dict_upResult, ensure_ascii=False, indent= 2))

postResult1 = post(json.dumps(dict_upResult), path='/OmsAgent/TakeReport/')
print("singletest result:", postResult1)
# dict_postResult = eval(postResult)
# if ('orderNo' in postResult) & (dict_postResult['result'] == 'success'):
#     dict_upResult['resultBasic']['omsOrderNo'] = dict_postResult['orderNo']
#     print(json.dumps(dict_upResult, ensure_ascii=False))
#     postResult1 = post(json.dumps(dict_upResult), ip='192.168.1.197:8080', path='/OmsAgent/TakeReport')
#     print("singletest warehouse result:", postResult1)
