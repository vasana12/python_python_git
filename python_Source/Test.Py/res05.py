#-*-coding:utf8 -*-

import re

c=re.compile(r"app\w*") #패턴 등록
res=c.findall("application orange apple banana") #검색
print(res)

pat= re.compile(r'\w+') #패턴 등록
res01= pat.findall('puppy duck cat') #검색
print(res01)

pat =re.compile(r'(\w+)\s+(\d+)') #패턴 등록
res02=pat.findall ('puppy 10 duck 20 cat 30') #검색
print(res02)

pat =re.compile('\w+\s+\d+') #패턴 등록
res03=pat.findall('puppy 10 duck 20 cat 30') #검색
print(res03)

p=re.compile(r'(\d+)-(\d+)-(\d+)')
a=p.search('2016-12-25')
year, month, day, =a.groups()#그룹을 각각 색인 나누어 리턴
print(year,month,day)
print(a.group(1),a.group(2),a.group(3))
print(a.group(0))
