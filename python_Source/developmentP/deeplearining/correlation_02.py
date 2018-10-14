import json
import math

import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager

import pandas as pd

#[CODE_1]
def correlation(x,y):
    n = len(x)
    vals = range(n)

    x_sum = 0.0
    y_sum = 0.0
    x_sum_pow  = 0.0
    y_sum_pow = 0.0
    mul_xy_sum = 0.0

    for i in vals:
        mul_xy_sum = mul_xy_sum + float(x[i]) * float(y[i])
        x_sum = x_sum + float(x[i])
        y_sum = y_sum + float(y[i])
        x_sum_pow = x_sum_pow + pow(float(x[i]),2)
        y_sum_pow = y_sum_pow + pow(float(y[i]), 2)

    try:
        r = ((n * mul_xy_sum) - (x_sum * y_sum)) / math.sqrt( ((n * x_sum_pow) - pow(x_sum,2)) * ((n*y_sum_pow) - pow(y_sum, 2)) )

    except:
        r = 0.0

    return r

#[CODE_2]
def setScatterGraph(tour_table, fv_table, tourpoint):   #그래프 그리기

    #[CODE_8] # tour_table에서 tour_table['resNm'] == tourpoint을 만족하는 데이터를 추출하는 작업
    tour = tour_table[tour_table['resNm'] == tourpoint]
    #print("#################################################")
    #print("tour =", tour)
    #print("#################################################")
    merge_table = pd.merge(tour, fv_table, left_index=True, right_index=True)

    fig = plt.figure()

    plt.subplot(1, 3, 1)    #plt.subplot(1:행수, 3:열수, 1:인덱스(순서))
    plt.xlabel('중국인 입국수')
    plt.ylabel('외국인 입장객수')
    r1 = correlation(list(merge_table['china']), list(merge_table['ForNum']))   #상관관계 정리
    plt.title(r' = {:.5f}'.format(r1))
    plt.scatter(list(merge_table['china']), list(merge_table['ForNum']) ,edgecolor='none', alpha=0.75, c='black')

    plt.subplot(1, 3, 2)  # plt.subplot(1:행수, 3:열수, 1:인덱스(순서))
    plt.xlabel('일본인 입국수')
    plt.ylabel('외국인 입장객수')
    r2 = correlation(list(merge_table['japan']), list(merge_table['ForNum']))  # 상관관계 정리
    plt.title(r' = {:.5f}'.format(r2))
    plt.scatter(list(merge_table['china']), list(merge_table['ForNum']), edgecolor='none', alpha=0.75, c='black')

    plt.subplot(1, 3, 3)  # plt.subplot(1:행수, 3:열수, 1:인덱스(순서))
    plt.xlabel('미국인 입국수')
    plt.ylabel('외국인 입장객수')
    r3 = correlation(list(merge_table['usa']), list(merge_table['ForNum']))  # 상관관계 정리
    plt.title(r' = {:.5f}'.format(r3))
    plt.scatter(list(merge_table['china']), list(merge_table['ForNum']), edgecolor='none', alpha=0.75, c='black')

    #tight_layout() : subplot들이 Figure 객체의 영역 내에서 자동으로 최대 크기로 출력되게 해준다
    plt.tight_layout()

    plt.show()
    return [tourpoint, r1, r2, r3]

def main():

    font_location = "c:/Windows/fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    #[CODE_4]
    tpFileName = '서울특별시_관광지입장정보_2011_2016.json'
    jsonTP = json.loads(open(tpFileName, 'r', encoding='utf-8').read())
    tour_table = pd.DataFrame(jsonTP, columns=('yyyymm', 'resNm', 'ForNum'))    #'ForNum' = 외국인 입장객 수
    tour_table = tour_table.set_index('yyyymm')
    print("### tour_table ###")
    print(tour_table)
    print("##################")

    #[CODE_5]
    #tour_table에서 resNm필드를 인데싱후 unique한 값 저장
    if __name__ == '__main__':
        resNm = tour_table.resNm.unique()       #unique: 중복 제거
        print("resNm = ", resNm)
        print()

    #[CODE_6]
    fv_CFileName = '중국(112)_해외방문객정보_2011_2016.json'
    jsonFV = json.loads(open(fv_CFileName,'r', encoding='utf-8').read())
    china_table = pd.DataFrame(jsonFV, columns=('yyyymm', 'visit_cnt'))
    china_table = china_table.rename(columns={'visit_cnt': 'china'})
    china_table = china_table.set_index('yyyymm')
    print("### china_table ###")
    print(china_table)
    print("###################")

    fv_CFileName = '일본(130)_해외방문객정보_2011_2016.json'
    jsonFV = json.loads(open(fv_CFileName, 'r', encoding='utf-8').read())
    japan_table = pd.DataFrame(jsonFV, columns=('yyyymm', 'visit_cnt'))
    japan_table = japan_table.rename(columns={'visit_cnt': 'japan'})
    japan_table = japan_table.set_index('yyyymm')
    print("### japan_table ###")
    print(japan_table)
    print("###################")

    fv_CFileName = '미국(275)_해외방문객정보_2011_2016.json'
    jsonFV = json.loads(open(fv_CFileName, 'r', encoding='utf-8').read())
    usa_table = pd.DataFrame(jsonFV, columns=('yyyymm', 'visit_cnt'))
    usa_table = usa_table.rename(columns={'visit_cnt': 'usa'})
    usa_table = usa_table.set_index('yyyymm')
    print("### usa_table ###")
    print(usa_table)
    print("###################")


    #[CODE_7]
    fv_table = pd.merge(china_table, japan_table, left_index=True, right_index=True)
    fv_table = pd.merge(fv_table, usa_table, left_index=True, right_index=True)
    print(fv_table)

    r_list = []
    for tourpoint in resNm:
        #[CODE_9] resNm에 저장된 요소수 만큼 그래프를 r_list에 추가
        r_list.append(setScatterGraph(tour_table, fv_table, tourpoint))

    #[CODE_10]
    r_table = pd.DataFrame(r_list, columns=('tourpoint', 'china', 'japan', 'usa'))
    r_table = r_table.set_index('tourpoint')
    r_table = r_table.drop('서울시립미술관 본관')
    r_table = r_table.drop('서대문자연사박물관')
    r_table.plot(kind='bar', rot=70)    #막대그래프로 상관관계 표시
    plt.show()

if __name__ == "__main__":
    main()

