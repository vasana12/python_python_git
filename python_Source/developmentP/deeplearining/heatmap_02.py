import pandas as pd
import json
import matplotlib.pyplot as plt
import seaborn as sns # numpy, scipy 추가 설치할 것

fv_CFileName = '중국(112)_해외방문객정보_2011_2016.json'
jsonFV = json.loads(open(fv_CFileName, 'r', encoding='utf-8').read())
china_table = pd.DataFrame(jsonFV, columns=('yyyymm', 'visit_cnt'))
#print(china_table.head()) #head() 는 앞부분 5개까지만 출력함
print(china_table)

china_table.yyyymm = pd.to_datetime(china_table.yyyymm, format='%Y%m')
china_table['year'] = china_table.yyyymm.dt.year
china_table['month'] = china_table.yyyymm.dt.month
#print(china_table.head())
print(china_table)

fv_CFileName = '일본(130)_해외방문객정보_2011_2016.json'
jsonFV = json.loads(open(fv_CFileName, 'r', encoding='utf-8').read())
china_table = pd.DataFrame(jsonFV, columns=('yyyymm', 'visit_cnt'))
#print(china_table.head()) #head() 는 앞부분 5개까지만 출력함
print(china_table)

china_table.yyyymm = pd.to_datetime(china_table.yyyymm, format='%Y%m')
china_table['year'] = china_table.yyyymm.dt.year
china_table['month'] = china_table.yyyymm.dt.month
#print(china_table.head())
print(china_table)

fv_CFileName = '미국()_해외방문객정보_2011_2016.json'
jsonFV = json.loads(open(fv_CFileName, 'r', encoding='utf-8').read())
china_table = pd.DataFrame(jsonFV, columns=('yyyymm', 'visit_cnt'))
#print(china_table.head()) #head() 는 앞부분 5개까지만 출력함
print(china_table)

china_table.yyyymm = pd.to_datetime(china_table.yyyymm, format='%Y%m')
china_table['year'] = china_table.yyyymm.dt.year
china_table['month'] = china_table.yyyymm.dt.month
#print(china_table.head())
print(china_table)

#피봇테이블 생성.피봇 테이블은 set_index 명령과 unstack 명령을 사용해서 만든다.
china_table = china_table.set_index(['month', 'year'])['visit_cnt'].unstack(fill_value=0)
print(china_table)

#히트맵 작성
sns.heatmap(china_table)
plt.show()