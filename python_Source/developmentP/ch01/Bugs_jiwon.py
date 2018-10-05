# coding:utf-8
from urllib.request import urlopen
from bs4 import BeautifulSoup

start_date = input('조회할 시작날짜 입력 (ex:yyyymmdd) : ')
end_date = input('조회할 종료날짜 입력 (ex:yyyymmdd) : ')

start_year = int(start_date[0:4])
start_month = int(start_date[4:6])
start_day = int(start_date[6:8])
print(start_year, start_month, start_day)
end_year = int(end_date[0:4])
end_month = int(end_date[4:6])
end_day = int(end_date[6:8])
print(end_year, end_month, end_day)

f = open('bugschart(%s~%s).txt' % (start_date, end_date), 'wt', encoding='utf-8')

for y in range(start_year, end_year+1):
    firstMonth = 1
    finalMonth = 13
    if y == 2006 and start_month < 9:
        firstMonth = 9 #2006년은 9월부터 처리하기 위해 설정
    elif y == start_year and y == 2018:
        firstMonth = start_month
        finalMonth = end_month + 1
    elif y == start_year and y < end_year:
        firstMonth = start_month
    elif y == start_year and y == end_year:
        firstMonth = start_month
        finalMonth = end_month + 1
    elif y == end_year:
        finalMonth = end_month + 1
    elif y == 2018 and end_month > 10:
        finalMonth = 10 + 1

    print("first Month = ", firstMonth, "final Month = ", finalMonth)
    for m in range(firstMonth, finalMonth):
        firstDay = 1
        finalDay = 32
        if y == 2006 and m == 9 and start_day < 22:
            firstDay = 22
        elif y == start_year and m == firstMonth and m == end_month:
            firstDay = start_day
            finalDay = end_day + 1
        elif y == start_year and m == firstMonth:
            firstDay = start_day
        elif y == end_year and m == end_month:
            finalDay = end_day + 1
        elif y == 2018 and m == 10:
            finalDay = 5

        print("first day = ", firstDay, "final day = ", finalDay)
        for d in range(firstDay, finalDay):
            if m == 2 and d > 28:
                break
            elif m in [4,6,9,11] and d > 30:
                break

            if len(str(m)) < 2:
                mStamp = "0" + str(m)
            else:
                mStamp = str(m)
            if len(str(d)) < 2:
                dStamp = "0" + str(d)
            else:
                dStamp = str(d)

            timestamp = str(y) + str(mStamp) + str(dStamp)
            print("날짜 : " + timestamp)
            url = urlopen("https://music.bugs.co.kr/chart/track/day/total?chartdate=" + timestamp)
            soup = BeautifulSoup(url, "html.parser", from_encoding="utf8")
            artists = []
            artistRank = 0
            titles = []
            titleRank = 0

            try:
                for link1 in soup.find_all(name="p", attrs={"class" : "artist"}):
                    try:
                        artist = link1.find('a').text
                        artists.append(artist)
                        artistRank += 1
                    except AttributeError as artistError:
                        artist = 'N/A'
                        artists.append(artist)
                        artistRank += 1

                for link2 in soup.find_all(name="p", attrs={"class": "title"}):
                    try:
                        title = link1.find('a').text
                        titles.append(title)
                        titleRank += 1
                    except AttributeError as artistError:
                        title = 'N/A'
                        titles.append(title)
                        titleRank += 1

                if (artistRank != titleRank): #혹시 가수 수와 노래 수가 다르면 에러
                    raise NotImplementedError

                for i in range(0, 100):
                    f.write(str(timestamp) + ',' + str(i+1) + ',' + str(artists[i]) + ',' + str(titles[i] + '\n'))
                    f.write('-----------------------------------------------------------------------------\n')
                    print('------------------------------------------------------------------------------')

            except AttributeError as e: #p태그 자체가 존재하지 않을 경우 데티어 없는 것으로 여기고 다으 ㅁ루프로
                print(timestamp + "이날 데이터가 존재하지 않습니다")
                continue
            except NotImplementedError as notImplemented:
                print('아티스트 제목 최종랭킹 불일치')

            except IndexError as index:
                print('인덱스 에러 / ' + '아티스트 리스트 길이 : ' + str(len(artists)) + '/곡 리스트 길어 : ' \
                      + str(len(titles)))
f.close()