import urllib.request

local_filename, headers = urllib.request.urlretrieve('http://python.org/')
html = open(local_filename)
print(html.name) # 지정한 파일 이름 출력
print(html.read(300))

