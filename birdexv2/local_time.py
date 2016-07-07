# Filename:time.py
import datetime
import os, time
import random


def localTimeNum():
    return time.strftime("%Y%m%d%H%M%S", time.localtime(time.time()))

def localTimeStandard():
    return str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time())))

def myOrderNum():
    return 'XST' + str(localTimeNum()) + datetime.datetime.now().strftime("%f") + random.choice('qwertyuiopasdfghjklzxcvbnm')