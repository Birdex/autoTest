import json
import random

import time

import postgresql
import postgresql.driver as pg_driver

from birdex_v2.requestMethod import post
from birdex_v2.localTime import myOrderNum

from birdex_v2.batchTakeOrder import takeXLS, executeBatchTake

# 批量预报单
takeList = takeXLS()
executeBatchTake(takeList)

# db = pg_driver.connect(database="postgres", user="postgres", password="password", host="localhost", port="5432")
# db.execute('''create table IF NOT EXISTS take_result("orderNo" varchar(64), "result" text)''')
# db.execute('''insert into test values ('xst',123,date'2016-09-06')''')
# db.close()