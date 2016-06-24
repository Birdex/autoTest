# -*- coding: utf-8 -*-
import http.client
import json

from birdex_v2.readFile import read
from birdex_v2.now import now

params = read('D:/workspace/BirdexTest/TKOrderSchema.txt')
tmp = json.loads(params)
print(isinstance(tmp,str),tmp)
dict_param = eval(tmp)
print(isinstance(dict_param,dict),dict_param)
json_param = json.dumps(dict_param)
print(json_param)
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