# -*- coding: utf-8 -*-
import http.client

from birdex_v2.readFile import createTO
from birdex_v2.now import now

params = createTO('D:/workspace/BirdexTest/TKOrderSchema.txt')

params["procTK"]["no"] = "XST" + str(now())
params["areaCode"] = '123434'
# ensure_ascii=False确保中文不出现乱码
# to = json.dumps(params,ensure_ascii=False)

# print(takingorder)
# ip="192.168.1.197"
# path="OmsMaster/Taking"
# res = Request()
# res.post("192.168.1.197", "/OmsMaster/Taking", takingOrder)

try:
    conn = http.client.HTTPConnection("192.168.1.197", 8080, timeout=10)
    headers = {"Content-type": "application/json"}
    # conn.putrequest("http://192.168.1.197/OmsMaster/Taking", body, skip_accept_encoding="utf-8")
    conn.request("POST", "OmsMaster/Taking", params, headers)
    reponse = conn.getresponse()
except http.client.HTTPException:
    print(http.client.HTTPException)
print(reponse.status, reponse.reason)
print(reponse.read())
conn.close()
