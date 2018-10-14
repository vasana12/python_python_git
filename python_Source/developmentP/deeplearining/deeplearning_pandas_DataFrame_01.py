import numpy as np
import pandas as pd

d = {'one' : pd.Series([1.,2.,3.], index =['a','b','c']), 'two' : pd.Series([1.,2.,3.,4,], index =['a','b','c','d'])}
print(d)
print('----------------------------------------')
df = pd.DataFrame(d) #마지막 행중 one 값은 NaN, two 보다 행이 하나 작음
print(df)
print()

print('----------------------------------------') # index 를 따로 적지 않으면 0 부터 시작한다.
d = {'one':pd.Series([1., 2., 3.]), #마지막 값은 NaN, two 보다 행이 하나 작음
     'two' : pd.Series([1., 2., 3., 4,])}
df = pd.DataFrame(d)
print(df)
print()

print('----------------------------------------')

d = {'one': [1., 2., 3., 4.],       #Series 가 아닌 DataFrame 사용시 칼럼별로 데이터의 길이가 같아야 한다.
     'two':[4., 3., 2., 1.]}
df = pd.DataFrame(d)
print(df)

print('----------------------------------------')
### dict ###
data2 = [{'a':1,'b':2}, {'a':5, 'b':10, 'c': 20}]
print(pd.DataFrame(data2))
print('----------------------------------------')

print(pd.DataFrame(data2, index=['first', 'second']))
print('----------------------------------------')

pf = pd.DataFrame(data2, columns=['a','b'], index=['first','second'])
print(pf) # columns 가 열이름으로 사용됨, 데이터에 있는 c 열은 출력 안됨
print('----------------------------------------')

print(pf.rename(columns={'a':'COL1'})) #열이름 'a' 를 'COL1' 으로 변경
print('----------------------------------------')

print(pf.set_index('b')) # 'b' 열을 인덱스로 사용
print('----------------------------------------')

###     merge       ###

data1 = [{'name':'Mark'},{'name':'Eric'}, {'name':'Jennifer'}]
df1 = pd.DataFrame(data1)
print(df1)
print('----------------------------------------')

df1['age'] = [10,11,12] #기존 df1 에 새로운 열을 추가함
print(df1)
print('----------------------------------------')

data2 = [{'sido':'서울'},{'sido':'경기'}, {'sido':'인천'}]
df2 = pd.DataFrame(data2)
print(df2)
print('----------------------------------------')

print(pd.merge(df1,df2, left_index=True, right_index=True))
a=pd.merge(df1,df2, left_index=True, right_index=True)
print('a=',a)
data3 = [{'tall': '175'},{'tall':'180'},{'tall':'165'}]
df3 = pd.DataFrame(data3)
print(df3)
print(pd.merge(a, df3, left_index=True, right_index=True))

df1 = pd.DataFrame({'고객번호':[1001, 1002, 1003, 1004, 1005, 1006, 1007],
                    '이름': ['둘리', '도우너', '또치', '길동','희동', '마이콜', '영희']},
                   columns=['고객번호', '이름'])
print(df1)
print('--------------------------------------')

df2 = pd.DataFrame({
    '고객번호' : [1001, 1001, 1005, 1006, 1008, 1001],
    '금액':[10000, 20000, 15000, 5000, 100000, 30000]
}, columns=['고객번호', '금액'])
print(df2)
print('--------------------------------------')

print(pd.merge(df1,df2)) #공통된 칼럼(고객번호)을 기준으로 merge
print('--------------------------------------')

#outer join 방식은 키 값이 한쪽에만 있어도 데이터를 보여준다.
print(pd.merge(df1, df2, how='outer'))
print('--------------------------------------')
print(pd.merge(df1, df2, how='left'))
print('--------------------------------------')
print(pd.merge(df1, df2, how='right'))
print('--------------------------------------')

df1= pd.DataFrame({
    '품종':['setosa', 'setosa', 'virginica', 'virginica'],
    '꽃잎길이': [1.4, 1.3, 1.5, 1.3]},
    columns=['품종', '꽃잎길이'])
print(df1)
print('--------------------------------------')
df2 = pd.DataFrame({
    '품종':['setosa', 'virginica', 'virginica', 'versicolor'],
    '꽃잎너비': [0.4, 0.3, 0.5, 0.3]},
    columns=['품종','꽃잎너비'])
print(df2)
print('--------------------------------------')
print(pd.merge(df1, df2))
print('--------------------------------------')

df3 = pd.DataFrame(
    [[1.,2.],
     [3.,4.],
     [5.,6.]], index=['a','c','e'], columns=['대구','부산']
)
print(df3)
print('--------------------------------------')
df4 = pd.DataFrame(
    [[7., 8.],
     [9., 10.],
     [11., 12.],
     [13., 14]],index =['b','c','d','e'], columns=['대구','광주'])
print(df4)
print('--------------------------------------')

print(pd.merge(df3,df4))
print('--------------------------------------')

print(pd.merge(df3, df4, left_index=True, right_index=True)) # 공통된 index 기준으로
print('--------------------------------------')

print(pd.merge(df3,df4 , how= 'outer'))

#리스트 데이터
data = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
print(data)
print('--------------------------------------')
print(data.values)
print('--------------------------------------')