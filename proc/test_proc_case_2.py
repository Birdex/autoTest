# -*- coding: utf-8 -*-
import json
import time
from birdexv2.IO import read
from birdexv2.local_time import localTimeNum
from birdexv2.request_method import post


def setUp():
    """ 加工出口单，正常加工出库 """
    time.sleep(0.5)
# 正常加工出库
def testFunc1():
    dict_ProcOrder = read('D:/workspace/BirdexTest/outOrder.txt')
    report = read('D:/workspace/BirdexTest/report.txt')
    time.sleep(0.5)
    dict_ProcOrder['procPr']['parcel']['ext']['comments'] = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

    postResult = post(json.dumps(dict_ProcOrder), path='/OmsMaster/ProcOrder/')
    print("ProcTest result:", postResult)
    dict_postResult = json.loads(postResult)
    if ('orderNo' in postResult) & (dict_postResult['result'] == 'success'):
        report['resultBasic']['omsOrderNo'] = dict_postResult['orderNo']
        # 加工.分拣结果
        report['resultBasic']['result'] = 'fail'
        time.sleep(0.1)
        postResult = post(json.dumps(report), ip='192.168.1.197:8080', path='/OmsAgent/PROrderReport/')
        print("ProcReport result:", postResult)
        dict_postResult = json.loads(postResult)
        assert dict_postResult['result'] == 'success'
    else:
        print("ProcOrderCreate fail")
        assert False
def tearDown():
    print("Test end")

