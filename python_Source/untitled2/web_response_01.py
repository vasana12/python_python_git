#-*-coding: utf-8 -*-

import urllib.request

response = urllib.request.urlopen('http://www.python.org') #해당 사이트 연결
print('RESPONSE:', response)
print('URL:',response.geturl())

headers = response.info()
print('DATE :', headers['date'])
print('HEADERS:')
print('-----')
print(headers)

data = response.read()
print('LENGTH :',len(data))
print('DATA:')
print('-----')
print(data.decode())


