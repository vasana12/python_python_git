#-*-coding:utf8 -*-

import re

a=re.search(r'\d+','abcd0123efgh')
print(a)
print(a.group()) #Match의 match를 그룹으로 리턴
print(a.start(),a.end())  #Match의 span(4,8)을 start(), end()로 리턴

r=bool(re.match('ba','I like banana')) #문자열의 시작부터 검색
print(r)
r1=bool(re.search('ba','I like banana')) #문자열의 전체에 대하여 검색
print(r1)

res= re.findall("app\w*","application orange apple banana")
print(res)

res=re.findall("a\w+","application a orange apple banana")
print(res)

res01=re.findall("a\w*","application a orange apple banana")
print(res01)