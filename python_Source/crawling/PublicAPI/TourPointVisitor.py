import urllib.request
import datetime
import json
import math
from PublicAPI.config import *

def get_request_url(url):

    req = urllib.request.Request(url)

    try :
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" %(datetime.datetime.now(),url))
        return None
#[CODE 1]
def getTourPointVisitor(yyyymm, sido, gungu, nPagenum, nItems):
    #API 부분은 문서 참조
    end_point = "http://openapi.tour.go.kr/openapi/service/TourismResourceStatsService/getPchrgTrrsrtVisitorList"

    parameters = "?_type=json&serviceKey=" + access_key
    parameters += "&YM=" +yyyymm
    parameters += "&SIDO=" + urllib.parse.quote(sido)
    parameters += "&GUNGU=" + urllib.parse.quote(gungu)
    parameters += "&RES_NM=&pageNo=" + str(nPagenum)
    parameters += "&numOfRows=" + str(nItems)

    url = end_point + parameters

    retData = get_request_url(url)

    if(retData == None):
        return None
    else:
        return json.loads(retData)

#[CODE 2]
def getTourPointData(item, yyyymm, jsonResult):
    #print("item =", item)
    addrCd = 0 if 'addrCd' not in item.keys() else item['addrCd'] #실행중 이부분에 간혹 오류 발생(데이터 끝에 도달시)
    gungu = '' if 'gungu' not in item.keys() else item['gungu']
    sido = '' if 'sido' not in item.keys() else item['sido']
    resNm = '' if 'resNm' not in item.keys() else item['resNm']
    rnum = '' if 'rnum' not in item.keys() else item['rnum']
    ForNum = 0 if 'csForCnt' not in item.keys() else item['csForCnt']
    NatNum = 0 if 'csNatCnt' not in item.keys() else item['csNatCnt']
    jsonResult.append({'yyyymm': yyyymm, 'addrCd':addrCd,
                       'gungu':gungu, 'sido':sido, 'resNm':resNm,
                       'rnum':rnum, 'ForNum':ForNum, 'NatNum': NatNum})
    return

def main():

    jsonResult = []

    #sido = '부산광역시'
    #gungu = '해운대구'
    sido = '서울특별시'
    gungu = ''
    #nPagenum = 1
    #nTotal = 0
    nItems = 100 #한번에 요청하는 데이터 개수

    nStartYear = 2011
    nEndYear = 2017

    try : #try ~ except 영역 추가(예제에 없음)
        for year in range(nStartYear, nEndYear): #2011 ~ 2016
            for month in range(1, 13):
                #{1:0>2} 에서 0>2 는 str(month) 길이가 1자리일때 앞에 0으로 채워서 2자리 만듬
                yyyymm = "{0}{1:0>2}".format(str(year), str(month))

                nPagenum = 1

        #[CODE 3]
        while True:
            jsonData = getTourPointVisitor(yyyymm, sido, gungu, nPagenum, nItems)
            #print(jsonData)
            if (jsonData['response']['header']['resultMsg']=='OK'): #['resultMsg'] 에 정상적이면 'OK' 저장 되어 있음
                nTotal = jsonData['response']['body']['totalCount'] #['totalCount'] 에 요청한 전체 item 수가 저장

                if nTotal == 0:
                    break
                for item in jsonData['response']['body']['items']['item']:
                    getTourPointData(item, yyyymm, jsonResult)
                nPage = math.ceil(nTotal/100)
                if(nPagenum == nPage):
                    break

                nPagenum += 1
            else:
                break

        with open('%s_관광지입장정보_%d_%d.json' %(sido, nStartYear, nEndYear-1), 'w', encoding='utf-8') as outfile:
            retJson = json.dumps(jsonResult,
                                 indent=4, sort_keys=True,
                                 ensure_ascii=False)
            outfile.write(retJson)
    except AttributeError as e : #예외처리 기능 추가 (예제에 없음)
        print(e.args)
        """
        with open('%s_관광지입장정보_%d_d.json' %(sido, nStartYear, nEndYear-1), 'w', encoding='utf8') as outfile:
            retJson = json.dumps(jsonResult,
                            indent=4, sort_keys=True,
                            ensure_ascii=False)
            outfile.write(retJson)
        """
    print('%s_관광지입장정보_%d_%d.json SAVED' %(sido, nStartYear, nEndYear-1))

if __name__ == '__main__':
    main()
