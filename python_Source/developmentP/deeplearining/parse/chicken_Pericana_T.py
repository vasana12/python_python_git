import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from itertools import count


def get_request_url(url, enc='utf-8'):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            try:
                rcv = response.read()
                ret = rcv.decode(enc)
            except UnicodeDecodeError:
                ret = rcv.decode(enc, 'replace')

            return ret

    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

'''
#페리카나 HTML 구조
<table class="table mt20">
<tbody>
	<tr>
	    <td class="t_center">가양동점</td>
	    <td>서울특별시 강서구 강서로74길 12 (가양동)</td>
	    <td class="t_center">
	    02-3663-3700</td>
	    <td class="t_center"><a href="#none" class="button h22 btn_gray" onclick="store_view('126.84170552834682','37.56748111916124','가양동점','02-3663-3700','서울특별시 강서구 강서로74길 12 (가양동)' );">상세정보</a></td>
	</tr>
</tbody>
</table>
'''
def getPelicanaAddress(sido, result):
    for page_idx in count():

        Pelicana_URL = 'http://www.pelicana.co.kr/store/stroe_search.html?&branch_name=&gu=&si=%s&page=%s' % (
        urllib.parse.quote(sido), str(page_idx + 1))
        print("[%s] : [%s]" % (sido, str(page_idx + 1)))

        rcv_data = get_request_url(Pelicana_URL)
        soupData = BeautifulSoup(rcv_data, 'html.parser')

        store_table = soupData.find('table', attrs={'class': 'table mt20'})
        tbody = store_table.find('tbody')
        bEnd = True
        for store_tr in tbody.findAll('tr'):
            bEnd = False
            tr_tag = list(store_tr.strings)
            store_name = tr_tag[1]
            store_address = tr_tag[3]
            store_sido_gu = store_address.split()[:2]

            result.append([store_name] + store_sido_gu + [store_address])

        if (bEnd == True):
            return


def main():
    result = []

    sido_list = ['서울특별시', '부산광역시', '대구광역시', '제주특별자치도', '광주광역시',
                 '울산광역시', '인천광역시', '세종특별자치시', '경기도', '강원도', '경상북도',
                 '경상남도', '충청북도', '충청남도', '전라북도', '전라남도', '대전광역시']

    sido_alias = """서울시:서울특별시 서울:서울특별시 강원:강원도 경기:경기도 충남:충청남도  
                        충북:충청북도 경남:경상남도 경북:경상북도 전남:전라남도 전북:전라북도 
                        제주도:제주특별자치도 제주:제주특별자치도 제주시:제주특별자치도
                        세종시:세종특별자치시 세종:세종특별자치시
                        대전시:대전광역시 대전:대전광역시 대구시:대구광역시 대구:대구광역시
                        인천시:인천광역시 인천:인천광역시 광주시:광주광역시 광주:광주광역시
                        울산시:울산광역시 울산:울산광역시 부산시:부산광역시 부산:부산광역시"""
    sido_dict = dict(aliasset.split(':') for aliasset in sido_alias.split())

    gungu_alias = """고양시일산서구:고양시 고양시덕양구:고양시 고양시일산동구:고양시
                        부천시오정구:부천시 부천시소사구:부천시 부천시원미구:부천시
                        안산시단원구:안산시 안산시상록구:안산시
                        안양시동안구:안양시 안양시만안구:안양시
                        성남시중원구:성남시 성남시중원구:성남시 성남시분당구:성남시 성남시수정구:성남시 
                        양편군:양평군 여주군:여주시
                        수원시권선구:수원시 수원시장안구:수원시 수원시권선구:수원시 수원시영통구:수원시 수원시팔달구:수원시
                        용인시기흥구:용인시 용인시수지구:용인시 용인시처인구:용인시
                        포항시북구:포항시 포항시남구:포항시
                        창원시마산회원구:창원시 마산회원구:마산시 창원시진해구:창원시 진해시:창원시
                        창원시마산합포구:창원시 창원시회원구:창원시 창원시성산구:창원시 창원시의창구:창원시
                        상주시낙양동:상주시 상주시사벌면:상주시
                        청주시흥덕구:청주시 청주시서원구:청주시 청주시상당구:청주시 청주시청원구:청주시
                        천안시서북구:천안시 천안시동남구:천안시 
                        전주시덕진구:전주시 전주시완산구:전주시
                        성주읍:성주군 의성읍:의성군 강화읍:강화군 웅진군:옹진군
                        구좌읍:제주시 북제주군:제주시 신광로:제주시 용문로:제주시 천수로:제주시
                        군포시금정동79-1:군포시 군포시금정동79-1:군포시
                        세종특별자치시:세종시 조치원읍:세종시 
                        한솔동:세종시 도담동:세종시 도움3로:세종시 도움8로:세종시
                        나리로:세종시 갈매로:세종시 마음로:세종시 보듬3로:세종시 
                        소담1로:세종시 호려울로:세종시 누리로:세종시 달빛로:세종시
                        연기면:세종시 연동면:세종시 전의면:세종시
                        금남면:세종시 부강면:세종시 연서면:세종시 장군면:세종시
                        전동면:세종시
                        """
    gungu_dict = dict(aliasset.split(':') for aliasset in gungu_alias.split())

    #sido_list[3] = '제주도'

    for sido in sido_list:
        getPelicanaAddress(sido, result)

    pericana_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    pericana_table.sido = pericana_table.sido.apply(lambda v: sido_dict.get(v, v))
    pericana_table.gungu = pericana_table.gungu.apply(lambda v: gungu_dict.get(v, v))
    pericana_table.to_csv("pericana_table3.csv", encoding="utf-8", mode='w', index=True)
    # sido_list[3] = '제주특별자치도'
    del result[:]
    print('PERICANA ADDRESS CRAWLING END')


if __name__ == '__main__':
    main()