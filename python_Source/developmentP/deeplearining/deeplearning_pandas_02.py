import numpy as np
import pandas as pd
s = pd.Series(np.random.randn(5))   #난수 생성
print(s)

s = pd.Series(np.random.randn(5), index=['F','U','C','K','U'])
print(s)
print()

d = {'a':0.,'b':1.,'c':2.}
print(pd.Series(d))
print()

print(pd.Series(d , index=['a','b','B','c'])) #B 인덱스는 매핑되는 값이 없어서 NaN
print()

print(pd.Series(7, index =['a','b','c','d','e'])) #index 에 7 이 다 매핑된다.
print()

s= pd.Series([1,2,3,4,5], index = ['a','b','c','d','e'])
print(s['b'], s[1]) #  s 의 0 번째 위치값 출력
print()

print(s[:3]) #0 번째 부터 2번째까지
print()

print(s[[4,1]]) #s 의 4와 1위치 값 으로  출력
print()

print(np.power(s,2)) # 거듭제곱 출력
print()