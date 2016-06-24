# -*- coding: utf-8 -*-
import http.client
import json

from birdex_v2.readFile import read
from birdex_v2.now import now

dict_param = read('D:/workspace/BirdexTest/TKOrderSchema.txt')
dict_param['procTK']['express']['no'] = "XST" + str(now())
json_param = json.dumps(dict_param)
try:
    conn = http.client.HTTPConnection("192.168.1.197:8080")
    headers = {"Content-type": "application/json"}
# conn.putrequest("http://192.168.1.197/OmsMaster/Taking", body, skip_accept_encoding="utf-8")
    conn.request("POST", "/OmsMaster/Taking", json_param, headers)
    reponse = conn.getresponse()
except http.client.HTTPException:
    print(http.client.HTTPException)
print(reponse.status, reponse.reason)
print(reponse.read().decode(encoding='utf-8'))
conn.close()