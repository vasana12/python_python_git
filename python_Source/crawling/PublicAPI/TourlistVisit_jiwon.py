import urllib.request
import datetime
import json
import matplotlib.pyplot as plt
import matplotlib
from matplotlib import font_manager
from PublicAPI.config import *

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)  # 정보추출, url open해서 해당 페이지 정보 불러옴
        if response.getcode() == 200:  # 상태정보 == 200 => OK(성공)라는 의미
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')  # 추출한 정보가 담겨져있움, utf-8로 디코드해서 불러옴
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

#[CODE_1]
def getNatVisitor(yyyymm, nat_cd, ed_cd):
    #API부분은 문서 참조
    end_point = "http://openapi.tour.go.kr/openapi/service/EdrcntTourismStatsService/getEdrcntTourismStatsList"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&YM=" + yyyymm
    parameters += "&NAT_CD=" + nat_cd
    parameters += "&ED_CD=" + ed_cd

    url = end_point + parameters

    retData = get_request_url(url)


    if (retData == None):  # 추출한 데이터 없어
        return None
    else:
        return json.loads(retData)  # JSON형식으로 리턴

def main():
    jsonResult = []

    #중국 112 일본 130 미국 275
    national_code = "275"
    ed_cd = "E"

    nStartYear = 2011
    nEndYear = 2017

    for year in range(nStartYear, nEndYear):
        for month in range(1, 13):
            # {1: 0 > 2}에서 0 > 2는 str(month) 길이가 1자리일 때 앞에 0으로 채워서 2자리 만듦(1번에 들어가는 month는 최소2자리여야해)

            yyyymm = "{0}{1:0>2}".format(str(year), str(month))
            jsonData = getNatVisitor(yyyymm, national_code, ed_cd)

            print(json.dumps(jsonResult,
                             indent=4, sort_keys=True,
                             ensure_ascii=False))

            if (jsonData['response']['header']['resultMsg'] == 'OK'):
                krName = jsonData['response']['body']['items']['item']["natKorNm"]
                krName = krName.replace(' ', '')
                iTotalVisit = jsonData['response']['body']['items']['item']["num"]
                print('%s_%s : %s' % (krName, yyyymm, iTotalVisit))
                jsonResult.append({'nat_name': krName, 'nat_cd': national_code,
                                   'yyyymm': yyyymm, 'visit_cnt': iTotalVisit})

    cnVisit = []
    VisitYM = []
    index = []
    i = 0
    for item in jsonResult:
        index.append(i)
        cnVisit.append(item['visit_cnt'])
        VisitYM.append(item['yyyymm'])
        i = i + 1

    with open('%s(%s)_해외방문객정보_%d_%d.json' % (krName, national_code, nStartYear, nEndYear - 1), 'w', encoding='utf-8') as outfile:
        retJson = json.dumps(jsonResult,
                             indent=4, sort_keys=True,
                             ensure_ascii=False)
        outfile.write(retJson)

    font_location = "c:/Windows/fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    plt.xticks(index, VisitYM)
    plt.plot(index, cnVisit)
    plt.xlabel('방문월')
    plt.ylabel('방문객수')
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    main()
