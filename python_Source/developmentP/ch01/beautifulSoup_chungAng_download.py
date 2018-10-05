#-*-coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.request
#HTML 가져오기
url = "http://rss.joins.com/joins_news_list.xml"
res = req.urlopen(url)
#HTML 분석하기
soup = BeautifulSoup(res, "html.parser")
#원하는 데이터 추출하기 ---#1

for item in soup.find_all("item"):
    print(item)
    print("title:", item.title.string)
    print("description:", item.description.stirng)
    print('------------------------------------------------------------------')
data = urllib.request.urlopen(url).read()
savename= "chungang.xml"
text = data.decode("utf-8")
with open(savename,mode="wb") as f:
    f.write(data)
