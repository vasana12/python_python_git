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

def getKyochonAddress(sido1, result):
    for sido2 in count():
        Kyochon_URL = "http://www.kyochon.com/shop/domestic.asp?txtsearch=&sido1=%s&sido2=%s" %(str(sido1), str(sido2+1))
        print(Kyochon_URL)

        try :
            rcv_data = get_request_url(Kyochon_URL)
            soupData = BeautifulSoup(rcv_data, 'html.parser')

            ul_tag = soupData.find('ul',attrs={'class': 'list'})

            for store_data in ul_tag.findAll('a', href=True):
                store_name =store_data.find('dt').get_text()
                store_address = store_data.find('dd').get_text().strip().split('\t')[0]
                store_sido_gu = store_address.split()[:2]
                result.append([store_name] + store_sido_gu + [store_address])
        except:
            break
    return
def main():
    result =[]

    print("Kyochon 주소 크롤링 시작")

    for sido1 in range(1,18):
        getKyochonAddress(sido1, result)
    kyochon_table = pd.DataFrame(result, columns=('store', 'sido', 'gungu', 'store_address'))
    kyochon_table.to_csv("kyochon.csv", encoding="utf-8", mode ='w', index= True)
    del result[:]

    print('FINISHED')

if __name__ =="__main__":
    main()