#-*-coding: utf-8 -*-

import http.client

conn = http.client.HTTPConnection("www.google.co.kr")
conn.request("POST","/index.html")
res = conn.getresponse()
print(res.status, res.reason)
data = res.read()
print(len(data))
print(data)