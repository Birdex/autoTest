# Filename:time.py

import os, time

def now():
    now = time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))
    return now
    # print(now)
