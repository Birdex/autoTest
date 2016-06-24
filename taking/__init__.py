import http.client
import json


class Data(object):
    def __init__(self):
        pass
    def createTO(self):
        # 用with读写文件,以确保结束之后，调用close()
        with open('C:/Users/Administrator/Desktop/TestCases/takingorder-1.json', 'r', encoding='utf-8') as f:
            strTO = f.read()
        dictTO = eval(strTO)
        # ensure_ascii=False确保中文不出现乱码
        takingorder = json.dumps(dictTO, ensure_ascii=False, indent=2)
        # print(takingorder)
        return takingorder

class Request(object):
    def __init__(self):
       pass
    def post(self, ip, path, params):
        try:
            conn = http.client.HTTPConnection(ip, 8080, timeout=10)
            headers = {"Content-type": "application/json"}
            # conn.putrequest("http://192.168.1.197/OmsMaster/Taking", body, skip_accept_encoding="utf-8")
            conn.request("POST", path, params, headers)
            reponse = conn.getresponse()
        except http.client.HTTPException:
            print(http.client.HTTPException)
        print(reponse.status, reponse.reason)
        print(reponse.read())
        conn.close()
