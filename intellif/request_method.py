import http.client
import base64


def post(params, ip='192.168.2.50:8083', path='/api/oauth/token'):
    try:
        conn = http.client.HTTPConnection(ip)
        headers = {"Content-type": "application/json", "Authorization": "Basic " + base64.b64encode("clientapp:123456")}
        # headers = {"Authorization", "Basic " + "clientapp:123456"}
        conn.request("POST", path, params, headers)
        reponse = conn.getresponse()
    except http.client.HTTPException:
        print(http.client.HTTPException)
    if reponse.status == 200:
        return reponse.read().decode(encoding='utf-8', errors='strict')
    else:
        print(reponse.read())
        return '''{"error":"clientError"}'''
    conn.close()


def get(params, ip='http://192.168.2.27:8000', path='/api/dbinfos/'):
    try:
        conn = http.client.HTTPConnection(ip)
        conn.request("GET", path + params)
        reponse = conn.getresponse()
    except http.client.HTTPException:
        print(http.client.HTTPException)
    if reponse.status == 200:
        return reponse.read().decode(encoding='utf-8', errors='strict')
    else:
        print(reponse.read())
        return '''{"error":"clientError"}'''
    conn.close()


def put(params, orderNo, ip='192.168.1.197:8080', path='/OmsMaster/Taking/'):
    try:
        conn = http.client.HTTPConnection(ip)
        headers = {"Content-type": "application/json"}
        conn.request("PUT", path + orderNo, params, headers)
        reponse = conn.getresponse()
    except http.client.HTTPException:
        print(http.client.HTTPException)
    if reponse.status == 200:
        return reponse.read().decode(encoding='utf-8', errors='strict')
    else:
        print(reponse.read())
        return '''{"error":"clientError"}'''
    conn.close()


if __name__ == '__main__':
    pass
