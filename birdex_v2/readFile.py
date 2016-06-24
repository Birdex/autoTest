# -*- coding: utf-8 -*-

import json


def read(path):
    # 用with读写文件,以确保结束之后，调用close()
    with open(path, 'r', encoding='utf-8') as f:
        str_param = f.read()
    to = json.dumps(str_param)
    tmp = json.loads(to)
    dict_param = eval(tmp)
    return dict_param
