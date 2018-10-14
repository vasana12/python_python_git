import numpy as np
import pandas as pd
from pandas import Series
import numpy as np

#리스트 데이터
data = pd.DataFrame([[1,2,3],[4,5,6],[7,8,9]])
print(data)
print('--------------------------------------')
print(data.values)
print('--------------------------------------')

#사전 데이터
dict_data = {'city': ['서울', '부산', '대구'],
             'year': [2000, 2001, 2002],
             'pop' : [4000, 1000, 2000]}

data = pd.DataFrame(dict_data)
print(data)
print('--------------------------------------')

#columns을 지정하면 지정한 순으로 출력
data = pd.DataFrame(dict_data, columns=['year', 'city', 'pop'])
print(data)
print('------------------------------------------')
data = pd.DataFrame(dict_data, columns=['city', 'pop', 'year'])
print(data)
print('------------------------------------------')

# index 지정
data = pd.DataFrame(dict_data, columns = ['city', 'pop', 'year'], index=['one', 'two', 'three'])
print(data)
print('------------------------------------------')

#column 가져오기
print(data.columns)
print('------------------------------------------')

#index 가져오기
print(data.index)
print('------------------------------------------')

#column 을 선택하여 추출
print(data['city'])
print('------------------------------------------')
print(data['year'])
print('------------------------------------------')

# ix, loc : 행에 접근할 때 사용되는 속성으로 index 를 name 속성으로 지정한다.
print(data.ix['one']) # index 'one' 에 해당하는 행 데이터 출력
print('------------------------------------------')
print(data.loc['one'])
print('------------------------------------------')
print(data.ix['one']['year'])
print(data.loc['one']['year'])
print('------------------------------------------')
#iloc : index position(위치값) 을 이용하여 추출
print(data.iloc[0:2])
print('------------------------------------------')
print(data.iloc[1:])
print('------------------------------------------')
print(data.year.iloc[1])
print('------------------------------------------')
print(data.year.iloc[1:])
print('------------------------------------------')

#빈 칼럼 추가 : debt, NaN (값없음) 으로 출력됨
data = pd.DataFrame(dict_data, columns=['city', 'pop', 'year', 'debt'], index=['one', 'two', 'three'])
print(data)
print('------------------------------------------')

#NaN 값 채우기
data['debt'] =10
print(data)
print('------------------------------------------')

data['debt'] = np.arange(3) #np.arange(3) : 0, 1, 2
print(data)
print('------------------------------------------')

val = Series([100,200,300], index=['one','two','three'])
data['debt'] = val
print(data)
print('------------------------------------------')

print(data.T) # T : 행과 열을 바꿔준다