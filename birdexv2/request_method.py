import http.client


def post(params, ip='192.168.1.197:8080', path='/OmsMaster/Taking/'):
    try:
        conn = http.client.HTTPConnection(ip)
        headers = {"Content-type": "application/json"}
        conn.request("POST", path, params, headers)
        reponse = conn.getresponse()
    except http.client.HTTPException:
        print(http.client.HTTPException)
    if reponse.status == 200:
        return reponse.read().decode(encoding='utf-8', errors='strict')
    else:
        print(reponse.read())
        return {'request or reponse error'}
    conn.close()


def get(params, ip='192.168.1.197:8080', path='/OmsMaster/Taking/'):
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
        return {'serverError': 'serverBug'}
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
        return {'serverError': 'serverBug'}
    conn.close()


if  __name__ == '__main__':
    put()