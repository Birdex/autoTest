import http.client
conn = http.client.HTTPConnection("192.168.1.197", 8080)
conn.request("GET", "/OmsMaster/Taking/O2016052814TK000000402")
r1 = conn.getresponse()
print(r1.status, r1.reason, r1.read())
