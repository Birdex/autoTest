# -*- coding: utf-8 -*-
import json
import time

from taking.now import now
from taking.requestMethod import *

TKdict = {
    'areaCode': '0315',
    'isCount': False,
    'procTK': {
        'date': '2016-06-06 10:35:21',
        'express': {
            'carrier': 'FedEx',
            'ext': {
                'comments': '',
                'files': [
                    ''
                ]
            },
            'no': 'XST201606071er57u6',
            'type': '空运',
            'way': {
                'flight': '',
                'from': '',
                'to': '',
                'via': [
                    ''
                ]
            }
        },
        'op': {
            'units': [
                {
                    'object': '/P:0'
                }
            ]
        },
        'parcels': [
            {
                'ext': {
                    'comments': '',
                    'label': ''
                },
                'items': [
                    {
                        'count': 300,
                        'ext': {
                            'batch': '100',
                            'brand': 'string',
                            'category': '音乐/电动',
                            'comments': '测试-3',
                            'pName': 'FisherPrice 费雪 声光安抚费雪小海马',
                            'spec': 'string',
                            'upc': '05120400370201',
                            'url': [
                                'http://item.meitun.com/itemDetail-31802-05120400370201.htm'
                            ]
                        },
                        'mCategory': 'string',
                        'mCode': '05120400370201',
                        'mName': 'FisherPrice 费雪 声光安抚费雪小海马',
                        'price': 79.00,
                        'priceUnit': 'string'
                    }
                ],
                'no': 'XST5601',
                'type': ''
            }
        ],
        'person': {
            'co': 'micro',
            'contact': {
                'address': '国人通信大厦',
                'ext': {
                    'email': '',
                    'mobile': '18923400863',
                    'note': ''
                }, ''
                'identityCard': '452127198411233034',
                'name': 'BurNing',
                'phone': '18923400863',
                'post': 'string'
            },
            'ext': {
                'group': 'B类',
                'id': 'micro003',
                'org': 'micro'
            },
            'name': '衡欣'
        }
    },
    'takeType': 'E2B',
    'warehouse': 'TM'
}
# print(json.dumps(tkdict,ensure_ascii=False,indent=4))
TKdict['procTK']['date'] = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))
TKdict["procTK"]["express"]["no"] = 'XST' + str(now())
params = json.dumps(TKdict)
# print(json.dumps(TKdict, ensure_ascii=False, indent=4))
postResult = json.loads(post(params))
print("postResult:" + json.dumps(postResult, ensure_ascii=False))
time.sleep(0.1)
if 'orderNo' in postResult:
    getResult = json.loads(get(postResult['orderNo']))
    print("getResult:" + json.dumps(getResult, ensure_ascii=False))
else:
    print(postResult)