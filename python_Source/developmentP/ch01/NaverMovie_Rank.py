#-*-coding: utf-8 -*-
from bs4 import BeautifulSoup
import urllib.request as req
import urllib.request

def rank_count():
    date = input('날짜를 입력하세요\nex)20181001 :')
    API = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
    values1 = {
        'sel': 'cnt'
    }
    values2 = {
        'date': date
    }
    params1 = urllib.parse.urlencode(values1)
    params2 = urllib.parse.urlencode(values2)
    url = API + "?" + params1 + "&" + params2
    print("url=", url)
    res = req.urlopen(url)
    # HTML 분석하기
    soup = BeautifulSoup(res, "html.parser")
    # 원하는 데이터 추출하기 ---#1
    tit3_list = soup.select("div.tit3 > a")
    for tit3 in tit3_list:

        print(tit3_list.index(tit3) + 1, ':', tit3.string)

def rank_cur():
    date = input('날자를 입력하세요\nex)20181001 :')
    API = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
    values1 = {
        'sel': 'cur'
    }
    values2 = {
        'date': date
    }
    params1 = urllib.parse.urlencode(values1)
    params2 = urllib.parse.urlencode(values2)
    url = API + "?" + params1 + "&" + params2
    print("url=", url)
    # HTML 가져오기
    res = req.urlopen(url)
    # HTML 분석하기
    soup = BeautifulSoup(res, "html.parser")
    # 원하는 데이터 추출하기 ---#1
    tit5_list = soup.select("div.tit5 > a")
    for tit5 in tit5_list:
        print(tit5_list.index(tit5) + 1, ':', tit5.string)

def rank_total_cur():
    date = input('날자를 입력하세요\nex)20181001 :')
    API = "https://movie.naver.com/movie/sdb/rank/rmovie.nhn"
    values1 = {
        'sel': 'pnt'
    }
    values2 = {
        'date': date
    }
    params1 = urllib.parse.urlencode(values1)
    params2 = urllib.parse.urlencode(values2)
    url = API + "?" + params1 + "&" + params2
    print("url=", url)
    # HTML 가져오기
    res = req.urlopen(url)
    # HTML 분석하기
    soup = BeautifulSoup(res, "html.parser")
    # 원하는 데이터 추출하기 ---#1
    tit5_list = soup.select("div.tit5 > a")
    for tit5 in tit5_list:
        print(tit5_list.index(tit5) + 1, ':', tit5.string)


def call_menu():
    while True:
        s = " 메뉴 "
        print(s.center(10, "*"))
        print("1.조회순")
        print("2.평점순(현재 상영영화)")
        print("3.평점순(모든 영화)")
        print("4.프로그램 종료")
        a=int(input("메뉴를 선택하세요(1~3) :"))
        if a==1:
            rank_count()
        elif a==2:
            rank_cur()
        elif a==3:
            rank_total_cur()
        else :
            break

if __name__ =='__main__':

    call_menu()