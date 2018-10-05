# -*-coding:utf-8-*-
from bs4 import BeautifulSoup
from urllib.request import urlopen

start_date = input('조회할 시작날짜를 입력(ex:yyyymmdd -> 20181001) => ')
end_date = input('조회할 종료날짜를 입력(ex:yyyymmdd -> 20181001) => ')

start_year = int(start_date[0:4])
start_month = int(start_date[4:6])
start_day = int(start_date[6:8])
print(start_year, start_month, start_day)
end_year = int(end_date[0:4])
end_month = int(end_date[4:6])
end_day = int(end_date[6:8])
print(end_year, end_month, end_day)

f = open('bugschart(%s~%s).txt' % (start_date, end_date), 'wt', encoding='utf-8')  # 파일 쓸 준비

for y in range(start_year, end_year + 1):  # 벅스차트가 2006.09.22부터 존재하므로, 2006년부터!
    firstMonth = 1
    finalMonth = 13
    if y == 2006 and start_month < 9:
        firstMonth = 9  # 2006년은 9월부터 처리하기 위해 설정
    elif y == start_year and y == 2018:
        firstMonth = start_month
        finalMonth = end_month + 1
    elif y == start_year and y < end_year:
        firstMonth = start_month
    elif y == start_year and y == end_year:  # 시작년도와 끝년도가 동일할 경우
        firstMonth = start_month
        finalMonth = end_month + 1
    elif y == end_year:
        finalMonth = end_month + 1
    elif y == 2018 and end_month > 10:  # 2018년은 10월까지 처리하기 위해 설정
        finalMonth = 10 + 1

    print('firstMonth =', firstMonth, 'finalMonth =', finalMonth)
    for m in range(firstMonth, finalMonth):
        firstDay = 1
        finalDay = 32
        if y == 2006 and m == 9 and start_day < 22:
            firstDay = 22  # 2006년은 9월 22일부터 처리하기 위해 설정
        elif y == start_year and m == firstMonth and m == end_month:
            firstDay = start_day
            finalDay = end_day + 1
        elif y == start_year and m == firstMonth:
            firstDay = start_day
        elif y == end_year and m == end_month:
            finalDay = end_day + 1
        elif y == 2018 and m == 10:
            finalDay = 5  # 2018년 10월에는 4일만 수집

        print("firstDay =", firstDay, "finalDay =", finalDay)
        for d in range(firstDay, finalDay):
            if (m == 2 and d > 28):  # 2월은 28일까지로 가정
                break
            elif (m in [4, 6, 9, 11] and d > 30):
                break

            if len(str(m)) < 2:  # 월 자릿수가 2자리 미만 시 앞에 '0'추가
                mStamp = "0" + str(m)
            else:
                mStamp = str(m)
            if len(str(d)) < 2:  # 일 자릿수가 2자리 미만 시 앞에 '0'cnrk
                dStamp = "0" + str(d)
            else:
                dStamp = str(d)

            timestamp = str(y) + str(mStamp) + str(dStamp)
            print("날짜 : " + timestamp)
            url = urlopen("https://music.bugs.co.kr/chart/track/realtime/total?chartdate=" + timestamp)
            soup = BeautifulSoup(url, "html.parser", from_encoding="utf-8")
            artists = []  # 이 날 1위~100위에 등록된 가수들 목록
            artistRank = 0
            titles = []  # 이 날 1위~100위에 등록된 제목 목록
            titleRank = 0
            try:
                for link1 in soup.find_all(name='p', attrs={'class': 'artist'}):
                    try:
                        artist = link1.find('a').text
                        artists.append(artist)
                        artistRank += 1
                        # print('날짜:'+str(timestamp)+', 순위:'+str(artistRank)+', 가수:'+str(artist))
                    except AttributeError as artistError:  # 가수데이터가 존재하지 않을 경우 a태그가 없음
                        artist = 'N/A'
                        artist.append(artist)
                        artistRank += 1
                        # print('서비스 되지 않는 아티스트입니다. ' + str(artistRank) + "위")

                for link2 in soup.find_all(name='p', attrs={'class': 'title'}):
                    try:
                        title = link2.find('a').text
                        titles.append(title)
                        titleRank += 1
                        # print('날짜:' + str(timestamp) + ', 순위:' + str(titleRank) + ', 제목:' + str(title))
                    except AttributeError as titleError:  # 곡 데이터가 존재하지 않을 경우 a태그가 없더라.
                        title = 'N/A'
                        titles.append(title)
                        titleRank += 1
                        # print('서비스 되지 않는 곡입니다. '+str(titleRank)+"위")

                if (artistRank != titleRank):  # 혹시나 아티스트와 곡 목록 객수가 다르면 에러를 일으킨다.(디버깅용)
                    raise NotImplementedError

                for i in range(0, 100):
                    f.write(str(timestamp) + ',' + str(i + 1) + ',' + str(artists[i] + ',' + str(titles[i]) + '\n'))
                f.write('--------------------------------------------------\n')
                print('--------------------------------------------------')

            except AttributeError as e:  # p태그 자체가 존재하지 않을 경우, 데이터 없는 것으로 여기고 다음 루프로 넘어가게 한다.
                    print(timestamp + "이 날 데이터가 존재하지 않습니다.")
                    continue
            except NotImplementedError as notImpelemented: #위에서 정의한 디버깅용 에러가 나면 표시해준다.
                print('아티스트, 제목 최종랭킹 불일치')
            except IndexError as index : #웹페이지 자체 에러로 Top100 곡 객수가 100개가 안되면 인덱스에러로 표시한다.
                print('인덱스 에러/' + '아티스트 리스트 길이: ' +str(len(artists)) + '/곡 리스트 길이: '\
                      +str(len(titles)))