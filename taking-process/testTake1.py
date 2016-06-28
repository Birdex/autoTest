# -*- coding: utf-8 -*-
import json
import time
from birdex_v2.readFile import read
from birdex_v2.now import now
from birdex_v2.requestMethod import post


def setUp():
    "带清点的揽收单，上传揽收结果success，清点结果failure"
    time.sleep(0.5)
#需要清点的揽收单，揽收成功，清点失败
def testFunc1():
    dict_takeOrder = read('D:/workspace/BirdexTest/TKOrderSchema.txt')
    report = read('D:/workspace/BirdexTest/report.txt')
    time.sleep(0.5)
    dict_takeOrder['procTK']['express']['no'] = 'XST' + str(now())
    dict_takeOrder['isCount'] = True
    postResult = post(json.dumps(dict_takeOrder))
    print("singleTest result:", postResult)
    dict_postResult = json.loads(postResult)
    if ('orderNo' in postResult) & (dict_postResult['result'] == 'success'):
        report['resultBasic']['omsOrderNo'] = dict_postResult['orderNo']
        #揽收成功
        report['resultBasic']['result'] = 'success'
        time.sleep(0.1)
        postResult = post(json.dumps(report), ip='192.168.1.197:8080', path='/OmsAgent/TakeReport/')
        print("TakeReport result:", postResult)
        dict_postResult = json.loads(postResult)
        if dict_postResult['result'] == 'success':
            #揽收清点失败
            report['resultBasic']['result'] = 'failure'
            time.sleep(0.1)
            postResult = post(json.dumps(report), ip='192.168.1.197:8080', path='/OmsAgent/TakingCountingReport/')
            print("TakeCountReport result:", postResult)
            dict_postResult = json.loads(postResult)
            # if dict_postResult['result'] == 'fail':
            #     assert True
            # else:
            #     print("TakeCountReport sure return fail")
            #     assert False
            assert dict_postResult['result'] == 'fail'
        else:
            print("TakeReport sure return success")
            assert False
    else:
        print("TakeCreate fail")
        assert False

def tearDown():
    print("Test end")

