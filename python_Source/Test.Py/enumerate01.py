#-*-coding:utf8 -*-
#enumerate() 함수 미사용한 경우

fruit =['apple','watermelon','peach','pear']
for i in range(len(fruit)):
    print(i+100,fruit[i])

print('--------------------')

#enumerate()함수 사용 한 경우
for i, res in enumerate(fruit,100):
    print(i,res)
print('--------------------')
for val in enumerate(fruit, 100):
    print(val)