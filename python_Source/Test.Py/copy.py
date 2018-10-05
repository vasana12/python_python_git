#-*-coding:utf8 -*-

from copy import copy
x=[1,2,3]
lst=[1,2,x]
lst1=copy(lst)
print(lst)
print(lst1)

print(lst==lst1)
print(id(lst)==id(lst1))

lst[2][1]=3
print(lst)
print(lst1)

