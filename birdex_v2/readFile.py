# -*- coding: utf-8 -*-

import json


def readTemp(path):
    # 用with读写文件,以确保结束之后，调用close()
    with open(path, 'r', encoding='utf-8') as f:
        str_param = f.read()
    to = json.dumps(str_param)
    tmp = json.loads(to)
    dict_param = eval(tmp)
    return dict_param


def read(path):
    with open(path, 'r', encoding='utf-8') as f:
        str_param = f.read()
    dict_param = json.loads(str_param)
    return dict_param
