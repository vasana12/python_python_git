#-*-coding:utf8 -*-
a=set([1,2,3])  #리스트를 셋으로 변환
print(a,type(a))
b=tuple({5,6,7}) #셋을 튜플로 변환
print(b,type(b))
c=list('hello')   #문자열을 리스트로 변환
print(c, type(c))
d=dict([[1,2],[3,4]])   #dict로 변환 할 때는 각 키, 밸류로 변환
print(d,type(d))
e=dict([(3,26),(4,44)])  #dict로 변환
print(e, type(e))