
#목록을 한꺼번에 묶어서 리턴 1,10:2,20:3,30 으로 리턴된다.
for x,y in zip([1,2,3],[10,20,30]):
    print(x+y)

#목록을 묶어서 set으로 리턴
print(set(zip(['a','b','c'],[1,2,3])))

#목록을 묶어서 dict로 리턴
keys= ['cat','dog','duck']
values=['야옹','멍멍','짹짹']
print(dict(zip(keys,values)))

dict1={'one':1,'two':2,'three':3}
for key, value in dict1.items():#목록을 key,value 로 리턴
    print(key, value)
