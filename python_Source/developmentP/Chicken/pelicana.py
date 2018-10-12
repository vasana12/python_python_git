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

def pelicanaAddress(result):
    for page_idx in count():
        Pelicana_URL = "http://www.pelicana.co.kr/store/stroe_search.html?page=%s&branch_name=&gu=&si=" % str(page_idx + 1)
        print(Pelicana_URL)

        rcv_data = get_request_url(Pelicana_URL)
        soupData = BeautifulSoup(rcv_data, 'html.parser')

        storeTable = soupData.find(class_ = 'table mt20')
        store_trs = storeTable.tbody.findAll('tr')

        if(store_trs):
            for store_tr in store_trs:
                tr_tag = list(store_tr.strings)
                #print("tr_tag = ", tr_tag)
                if tr_tag[0] == '게시물이 없습니다.':
                    return

                store_name = tr_tag[1]
                store_address = tr_tag[3]
                store_sido_gu = store_address.split()[:2]
                result.append([store_name] + store_sido_gu + [store_address])
        else:
            break

    return

def main():
    result =[]

    print("페리카나 주소 크롤링 시작")

    pelicanaAddress(result)
    pelicana_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    pelicana_table.to_csv("pelicana.csv", encoding="utf-8", mode ='w', index= True)
    del result[:]

    print('FINISHED')

if __name__ =="__main__":
    main()
