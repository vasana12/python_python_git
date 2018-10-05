#-*-coding:utf8 -*-

import re
#이스케이프 문자 적용되지 않는 코드
r=bool(re.search('\\\\\w+','\lanana'))
print(r)
#이스케이프 문자 적용한 코드
r02=bool(re.search(r'\\\w+',r'\banana'))
print(r02)
print(re.search('\\\\\w+','\\banana'))
print(re.search('\\\\\w+','\\banana'))
print(re.search(r'\\\w+',r'\banana'))