import urllib.request

req = urllib.request.Request('http://www.my_server.org')

try:
    urllib.request.urlopen(req)
except urllib.error.URLError as e:
    print(e.reason)
