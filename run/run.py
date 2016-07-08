import json
import random

import time

import postgresql
import postgresql.driver as pg_driver

from birdexv2.IO import read
from birdexv2.request_method import post
from birdexv2.local_time import myOrderNum, localTimeNum

from birdexv2.batch_take import takeXLS, executeBatchTake

# 批量预报单
take_list = takeXLS(fileName='D:/pairs/take.xlsx')
# print(take_list[169])
# print(take_list[170])
# print(take_list[171])

executeBatchTake(take_list)
