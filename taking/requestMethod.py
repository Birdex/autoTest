import http.client
import config

def post(params):
    try:
        conn = http.client.HTTPConnection(config.url)
        headers = {"Content-type": "application/json"}
        conn.request("POST", config.path, params, headers)
        reponse = conn.getresponse()
    except http.client.HTTPException:
        print(http.client.HTTPException)
    print(reponse.status==200)
    if reponse.status == 200:
        return reponse.read().decode(encoding='utf-8',errors='strict')
    else:
        return {'serverError':'serverBug'}
        print(reponse.read())
    conn.close()

def get(orderNo):
    try:
        conn = http.client.HTTPConnection(config.url)
        conn.request("GET", config.path + orderNo)
        reponse = conn.getresponse()
    except http.client.HTTPException:
        print(http.client.HTTPException)
    if reponse.status == 200:
        return reponse.read().decode(encoding='utf-8', errors='strict')
    else:
        return {'serverError': 'serverBug'}
        print(reponse.read())
    conn.close()
    conn.close()

def put(params,orderNo):
    try:
        conn = http.client.HTTPConnection(config.url)
        headers = {"Content-type": "application/json"}
        conn.request("PUT", config.path + orderNo, params, headers)
        reponse = conn.getresponse()
    except http.client.HTTPException:
        print(http.client.HTTPException)
    if reponse.status == 200:
        return reponse.read().decode(encoding='utf-8', errors='strict')
    else:
        return {'serverError': 'serverBug'}
        print(reponse.read())
    conn.close()
    conn.close()