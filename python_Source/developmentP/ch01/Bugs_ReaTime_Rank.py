#-*-coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import datetime

firstdate = input('조회할 기간의 첫번째 날짜를 입력하세요(ex:yyyymmdd -> 20181001)=>')
finaldate = input('조회할 기간의 마지막 날짜를 입력하세요(ex:yyyymmdd -> 20181001)=>')

url = 'https://music.bugs.co.kr/chart/track/realtime/total?chartdate='+firstdate
print("\nurl:", url)

html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
title_list = soup.select("p.title > a")
artist_list = soup.select("p.artist > a")
savename = firstdate+ '.xml'
i=0

with open(savename, mode="wt", encoding='utf-8') as f:
    for title in title_list:
        content = "%s\t%d\t%s\t%s" %(firstdate, title_list.index(title)+1,artist_list[i].string,title.string)
        i = i+1
        f.write(content+'\n')

    # print(title_list.index(title) + 1, ':', title.string)

#다운로드합니다. ---#3
# data = urllib.request.urlopen(url).read()
# savename= firstdate+'.xml'
# text = data.decode("utf-8")
#
# with open(savename,mode="wb") as f:
#     f.write(data)