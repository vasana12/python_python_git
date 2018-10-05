#-*-coding:utf8 -*-

import re
p=re.compile(r'(\w+)\s+(?:\w+)\s+(\w+)')
a=p.search('abc def ghi') #공백으로 그룹을 나눈다.
print(a.groups())