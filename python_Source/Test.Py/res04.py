#-*-coding:utf8 -*-

import re
res=re.sub("-",",","123-456-789") #형식을 변경
print(res)
res01=re.sub(r"[:|]",",","a:b|c") #구분자 통일
print(res01)
res02=re.sub('[:,|\s]','_','one:two tree|four',2) #변경횟수 제한
print(res02)

s=("grape orange apple banana GRAPE")
print(s)
c=re.compile('grape', re.I) #대소문자 구분하지 않음
print(c)
res=c.findall(s)
print(res)