import pandas as pd
import matplotlib
import matplotlib.pyplot as plt
import json
import seaborn as sns
from matplotlib import font_manager


def show_heatMap(fv_CFileName):
    jsonFV = json.loads(open(fv_CFileName, 'r', encoding='utf-8').read())
    # json 데이터를 행렬구조로 만드는 부분
    # 컬럼을 두개만 뽑는다.
    heatmap_table = pd.DataFrame(jsonFV, columns=('yyyymm', 'visit_cnt'))

    heatmap_table.yyyymm = pd.to_datetime(heatmap_table.yyyymm, format='%Y%m')
    heatmap_table['year'] = heatmap_table.yyyymm.dt.year
    heatmap_table['month'] = heatmap_table.yyyymm.dt.month
    # print(china_table.head()) # head()는 앞부분 5개까지만 출력한다.
    print('### heatmap_table ###')
    print(heatmap_table)
    print('##################')

    # 피봇테이블 생성, 피봇 테이블은 set_index 명령과 unstack 명령을 사용해서 만든다.
    # >>>>>>>>>>>>>>>>>>>>>> set_index 쓰는 방법 익혀두기 <<<<<<<<<<<<<<<<<<<<<<<
    heatmap_table = heatmap_table.set_index(['month', 'year'])['visit_cnt'].unstack(fill_value=0)

    plt.title(fv_CFileName[0:2])
    sns.heatmap(heatmap_table)
    plt.show()
    return heatmap_table


def main():
    font_location = 'C:/Windows/fonts/malgun.ttf'
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    list = ['중국(112)_해외방문객정보_2011_2016.json',
            '일본(130)_해외방문객정보_2011_2016.json',
            '미국(275)_해외방문객정보_2011_2016.json']

    tbl_list = []

    for i in range(3):
        tbl_list.append(show_heatMap(list[i]))

    fig = plt.figure()
    fig.suptitle('외국인 방문객 분석')
    plt.subplot(1, 3, 1)
    plt.title('중국')
    sns.heatmap(tbl_list[0])

    plt.subplot(1, 3, 2)
    plt.title('일본')
    sns.heatmap(tbl_list[1])

    plt.subplot(1, 3, 3)
    plt.title('미국')
    sns.heatmap(tbl_list[2])

    plt.show()


if __name__ == "__main__":
    main()