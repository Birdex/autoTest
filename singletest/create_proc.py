# -*- coding: utf-8 -*-

import http.client
import json
import time

from birdexv2.local_time import localTimeNum
from birdexv2.request_method import *

POdict = {
    'deliverType': 'standard',
    'procPr': {
        'op': {
            'units': [
                {
                    'object': '/P:0/I:0'
                }
            ]
        },
        'parcel': {
            'ext': {
                'comments': '',
                'label': ''
            },
            'items': [
                {
                    'count': 30,
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
                    'priceUnit': 'CNY'
                }
            ],
            'no': '',
            'type': ''
        },
        'person': {
            'co': 'xieshitong',
            'contact': {
                'address': '',
                'ext': {
                    'email': '',
                    'mobile': '18923400863',
                    'note': ''
                },
                'identityCard': '511325198807070028',
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
    'warehouse': 'TM'
}
POdict['procPr']['parcel']['no'] = 'XST'+ str(localTimeNum())
params = json.dumps(POdict)
# print(json.dumps(POdict, ensure_ascii=False, indent=4))
postResult = json.loads(post(params, '192.168.1.197:8080', '/OmsMaster/ProcOrder/'))
print("postResult:" + json.dumps(postResult, ensure_ascii=False))
time.sleep(0.1)
if 'orderNo' in postResult:
    getResult = json.loads(get(postResult['orderNo'], path='/OmsMaster/ProcOrder/'))
    print("getResult:" + json.dumps(getResult, ensure_ascii=False))
else:
    print(postResult)