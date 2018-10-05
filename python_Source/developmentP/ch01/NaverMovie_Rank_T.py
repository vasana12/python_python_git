#-*-coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request
import sys

print('1. 조회순')
print('2. 평점순(현재상영영화)')
print('3. 평점순(모든영화)')

menu = input('\n영화랭킹 메뉴를 선택하세요!!!=>')
if menu =='1':
    sel = 'cnt'
elif menu =='2':
    sel = 'cur'
elif menu == '3':
    sel = 'pnt'
else:
    print('메뉴를 잘못선택하셨습니다!!')
    sys.exit()

menudate = input('조회할 날짜를 입력하세요(ex:yyyymmdd -> 20181001)=>')
url = 'http://movie.naver.com/movie/sdb/rank/rmovie.nhn?sel=' +sel + '&date='+menudate
print("\nurl:", url)

html = urllib.request.urlopen(url)
soup = BeautifulSoup(html, 'html.parser')
if sel == 'cnt':
    movie_list = soup.findAll('div', attrs={'class':'tit3'})
else :
    movie_list = soup.findAll('div', attrs={'class':'tit5'})
#print(movie_list)
i = 1
print("\n순위\t 영화제목")
print('-----------------------')
for movie in movie_list:
    print(i, '\t\t', movie.a.string)
    i = i+1
    if i > 50:
        break
