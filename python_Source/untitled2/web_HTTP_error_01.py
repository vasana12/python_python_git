import urllib.request

req = urllib.request.Request('http://www.daum.net/abc123.html')
try:
    f = urllib.request.urlopen(req)
    print(f.read(300).decode('utf-8'))
except urllib.error.HTTPError as e:
    print(e.code)
    print(e.read(400))

