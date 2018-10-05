#-*-coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request as req

#HTML 가져오기
url = "http://rss.joins.com/joins_news_list.xml"
res = req.urlopen(url)
#HTML 분석하기
soup = BeautifulSoup(res, "html.parser")
#원하는 데이터 추출하기 ---#1

for item in soup.find_all("item"):
    print("title:", item.title.string)
    print("description:", item.description.string)
    print('------------------------------------------------------------------')