import urllib.request
from bs4 import BeautifulSoup
import pandas as pd
import datetime
from itertools import count
import xml.etree.ElementTree as ET
from selenium import webdriver
import time

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
#굽네치킨 HTML 형식
<tbody id="store_list">
    <tr class="on lows" idx="788" onclick="store.viewdt('788','37.2755111612','127.070853941');" id="788">
        <td>흥덕지구점<span><!--031-651-9294--></span></td>
        <td class="store_phone">
            <a href="javascript:void(0);" onclick="store.teldt('031-212-9293');">031-212-9293</a>
        </td>
        <td class="t_left">
    		<a href="javascript:void(0);">경기도 용인시 기흥구  흥덕1로 79번길 9, 105호</a>
    		<p>
    		<i class="online ">온라인</i>
     		<i class="coupon ">e-쿠폰</i>
			<!--<i class="cesco on">세스코</i>-->
			<i class="card_dis ">카드할인</i>
    		</p>
	</td>
</tr>
'''

def GoobneAddress(result):
    Goobne_URL = 'http://www.goobne.co.kr/store/search_store.jsp'

    wd = webdriver.Chrome('C:\BigDeep\ChromeDriver\chromedriver.exe')
    wd.get(Goobne_URL)
    time.sleep(3)

    for page_idx in count():

        wd.execute_script("store.getList('%s')" % str(page_idx + 1))
        print("PageIndex [%s] Called" % (str(page_idx + 1)))

        time.sleep(5)

        rcv_data = wd.page_source

        soupData = BeautifulSoup(rcv_data, 'html.parser')

        for store_list in soupData.findAll('tbody', attrs={'id': 'store_list'}):
            for store_tr in store_list:
                print(store_tr)
                tr_tag = list(store_tr.strings)
                if (tr_tag[0] == '등록된 데이터가 없습니다.'):
                    return result

                store_name = tr_tag[1]
                if (tr_tag[3] == ''):
                    store_address = tr_tag[5]
                else:
                    store_address = tr_tag[6]
                store_sido_gu = store_address.split()[:2] #전체주소에서 첫번째와 두번째 추출하여 리스트로 반환
                # 리스트 데이터(store,sido,gungu,store_address)를 result에 추가
                result.append([store_name] + store_sido_gu + [store_address])

    return


def main():
    result = []

    print('GOOBNE ADDRESS CRAWLING START')
    GoobneAddress(result)

    #goobne_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    #goobne_table.to_csv("goobne.csv", encoding="utf-8", mode='w', index=True)

    f = open('goobne_1.csv', 'wt', encoding='utf-8')
    f.write(',store,sido,gungu,store_address\n')
    i = 0
    for data in result:
        if len(data) != 4:
            continue # 데이터가 생략된 경우
        else:
            for k in range(0, 4):
                if ',' in data[k]:
                    data[k] = '"' + data[k] + '"'

        data_str = str(i) + ',' + data[0] + ',' + data[1] + ',' + data[2] + ',' + data[3] + "\n"
        print(data_str)
        f.write(data_str)
        i += 1

    f.close()
    print('FINISHED')


if __name__ == '__main__':
    main()