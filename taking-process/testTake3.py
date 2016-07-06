# -*- coding: utf-8 -*-
import json
import time
from birdex_v2.IO import read
from birdex_v2.localTime import localTimeNum
from birdex_v2.requestMethod import post


def setUp():
    # 揽收单isCount，揽收失败fail，揽收清点操作fail
    time.sleep(0.5)
def Testfunc3():
    # 读取揽收和揽收结果数据格式
    dict_takeOrder = read('D:/workspace/BirdexTest/TKOrderSchema.txt')
    report = read('D:/workspace/BirdexTest/report.txt')
    # 设置参数具体值
    time.sleep(0.5)
    dict_takeOrder['procTK']['express']['no'] = 'XST' + str(localTimeNum())
    dict_takeOrder['isCount'] = True
    postResult = post(json.dumps(dict_takeOrder))
    print("Take result:", postResult)
    dict_postResult = json.loads(postResult)
    if ('orderNo' in postResult) & (dict_postResult['result'] == 'success'):
        report['resultBasic']['omsOrderNo'] = dict_postResult['orderNo']
        report['resultBasic']['result'] = 'fail'
        time.sleep(0.1)
        postResult = post(json.dumps(report), ip='192.168.1.197:8080', path='/OmsAgent/TakeReport/')
        print("TakeReport result:", postResult)
        dict_postResult = json.loads(postResult)
        if dict_postResult['result'] == 'success':
            report['resultBasic']['result'] = 'fail'
            time.sleep(0.1)
            postResult = post(json.dumps(report), ip='192.168.1.197:8080', path='/OmsAgent/TakingCountingReport/')
            print("TakeCountReport result:", postResult)
            dict_postResult = json.loads(postResult)
            assert dict_postResult['result'] != 'success'
        else:
            print('TakeReport fail')
            assert False
    else:
        print("TakeCreate fail")
        assert False

def tearDown():
    print("Test end")

