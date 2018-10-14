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
            print("[%s] Url Request Success" % datetime.datetime.now())

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



def getKyochonAddress(sido, result):
    for sido2 in count():
        Kyochon_URL = 'http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%s&sido2=%s' % (
        str(sido), str(sido2 + 1))

        rcv_data = get_request_url(Kyochon_URL)
        if (rcv_data == None):
            return
        soupData = BeautifulSoup(rcv_data, 'html.parser')

        ul_tag = soupData.find('ul', attrs={'class': 'list'})
        for store_data in ul_tag.findAll('a', href=True):
            store_name = store_data.find('dt').get_text()
            store_address = store_data.find('dd').get_text().strip().split('\r')[0]
            store_sido_gu = store_address.split()[:2]
            result.append([store_name] + store_sido_gu + [store_address])


def CheogajipAddress(result):
    for page_idx in count():
        Cheogajip_URL = 'http://www.cheogajip.co.kr/bbs/board.php?bo_table=store&page=%s' % str(page_idx + 1)
        print(Cheogajip_URL)

        rcv_data = get_request_url(Cheogajip_URL)
        soupData = BeautifulSoup(rcv_data, 'html.parser')

        storeTable = soupData.find(class_='tbl_head01')
        store_trs = storeTable.table.tbody.findAll('tr')

        if (store_trs):
            for store_tr in store_trs:
                tr_tag = list(store_tr.strings)
                #print("tr_tag =", tr_tag)
                if tr_tag[0] == '게시물이 없습니다.':
                    return

                store_name = tr_tag[3]
                store_address = tr_tag[5]
                store_sido_gu = store_address.split()[:2]
                result.append([store_name] + store_sido_gu + [store_address])
        else:
            break

    return


from selenium import webdriver
import time

def GoobneAddress(result):
    Goobne_URL = 'http://www.goobne.co.kr/store/search_store.jsp'

    wd = webdriver.Chrome('C:\BigDeep\ChromeDriver\chromedriver.exe')
    wd.get(Goobne_URL)
    time.sleep(10)

    for page_idx in count():

        wd.execute_script("store.getList('%s')" % str(page_idx + 1))
        print("PageIndex [%s] Called" % (str(page_idx + 1)))

        time.sleep(5)

        rcv_data = wd.page_source

        soupData = BeautifulSoup(rcv_data, 'html.parser')

        for store_list in soupData.findAll('tbody', attrs={'id': 'store_list'}):
            for store_tr in store_list:
                tr_tag = list(store_tr.strings)
                if (tr_tag[0] == '등록된 데이터가 없습니다.'):
                    return result

                store_name = tr_tag[1]
                if (tr_tag[3] == ''):
                    store_address = tr_tag[5]
                else:
                    store_address = tr_tag[6]
                store_sido_gu = store_address.split()[:2]

                result.append([store_name] + store_sido_gu + [store_address])


def main():
    result = []

    sido_list = ['서울특별시', '부산광역시', '대구광역시', '제주특별자치도', '광주광역시',
                 '울산광역시', '인천광역시', '세종특별자치시', '경기도', '강원도', '경상북도',
                 '경상남도', '충청북도', '충청남도', '전라북도', '전라남도', '대전광역시']
    """
    sido_list1 = ['서울', '경기', '인천', '강원', '충북', '충남', '경북',
                  '경남', '대전', '대구', '전북', '전남', '광주', '울산', '부산',
                  '제주', '세종']
    """
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


    print('PERICANA ADDRESS CRAWLING START')
    sido_list[3] = '제주도'

    for sido in sido_list:
        getPelicanaAddress(sido, result)
        
    pericana_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    pericana_table.sido = pericana_table.sido.apply(lambda v: sido_dict.get(v, v))
    pericana_table.gungu = pericana_table.gungu.apply(lambda v: gungu_dict.get(v, v))
    pericana_table.to_csv("pericana_table3.csv", encoding="utf-8", mode='w', index=True)
    #sido_list[3] = '제주특별자치도'
    del result[:]
    print('PERICANA ADDRESS CRAWLING END')
    
    print('KYOCHON ADDRESS CRAWLING START')
    i = 0
    for sido in sido_list:  # sido1 분류에서 sido2 마지막 부분에 URL오류 발생함
        i = i + 1
        getKyochonAddress((i), result)
        
    kyochon_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    kyochon_table.sido = kyochon_table.sido.apply(lambda v: sido_dict.get(v, v))
    kyochon_table.gungu = kyochon_table.gungu.apply(lambda v: gungu_dict.get(v, v))
    kyochon_table = kyochon_table.reset_index().drop_duplicates(subset='store_address', keep='first').set_index('index')
    kyochon_table.to_csv("kyochon_table3.csv", encoding="utf-8", mode='w', index=True)
    del result[:]
    print('KYOCHON ADDRESS CRAWLING END')
    

    print('CHEOGAJIP ADDRESS CRAWLING START')
    CheogajipAddress(result)
    cheogajip_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    cheogajip_table.sido = cheogajip_table.sido.apply(lambda v: sido_dict.get(v, v))
    cheogajip_table.gungu = cheogajip_table.gungu.apply(lambda v: gungu_dict.get(v, v))
    cheogajip_table = cheogajip_table.reset_index().drop_duplicates(subset='store_address', keep='first').set_index('index')
    cheogajip_table.to_csv("cheogajip_table3.csv", encoding="utf-8", mode='w', index=True)
    del result[:]
    print('CHEOGAJIP ADDRESS CRAWLING END')

    print('GOOBNE ADDRESS CRAWLING START')
    GoobneAddress(result)
    goobne_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    goobne_table.sido = goobne_table.sido.apply(lambda v: sido_dict.get(v, v))
    goobne_table.gungu = goobne_table.gungu.apply(lambda v: gungu_dict.get(v, v))
    #goobne_table.sido[654] = '전라남도'
    #goobne_table.gungu[654] = '목포시'
    goobne_table = goobne_table[goobne_table.sido != ' ']
    goobne_table.to_csv("goobne_table3.csv", encoding="utf-8", mode='w', index=True)
    print('GOOBNE ADDRESS CRAWLING END')


if __name__ == '__main__':
    main()
