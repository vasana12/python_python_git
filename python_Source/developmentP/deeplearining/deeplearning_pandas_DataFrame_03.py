import numpy as np
import pandas as pd
from pandas import Series, DataFrame
import numpy as np

series1 = Series(np.arange(5.0), index= ['a','b','c','d','e'])
print(series1)

series2 = series1.drop('c')
print(series2)

series3 = series1.drop(['a','b']) #인덱스 'a', 'b' 를 한꺼번에 삭제
print(series3)

#DataFrame 에서 특정 colunm , row 삭제
data = {'state' : ['Ohio','Ohio','Ohio','Nevada','Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
df = DataFrame(data, columns=['year', 'state', 'pop'], index = ['00', '01', '02', '03', '04'])
print(df)
print('--------------------------')
#디폴트는 행 삭제 (axis=0), 열 삭제하려면 axis=1 로 설정.
df2= df.drop('04') #행 삭제
print(df2)
print('--------------------------')

df3 = df.drop('pop', axis=1) #열 삭제
print(df3)
print('--------------------------')

#인덱스의 리스트를 전달해서 여러 행을 한번에 삭제도 가능
df4 = df.drop(['03','04'])
print(df4)
