import json
import re

#from konlpy.tag import Twitter # Twitter -> Okt 로 수정할 것

from konlpy.tag import Okt
from collections import Counter

import matplotlib.pyplot as plt
import matplotlib # \venv\Lib\site-packages\pytagcloud\fonts\font.json 파일 편집하고 해당 폰트파일을 복사할것.
from matplotlib import font_manager
import pytagcloud #pygame, simplejson 모듈을 추가로 설치할것
import webbrowser

#[CODE 1]
def showGraph(wordInfo):
    font_location = "c:/Windows/fonts/malgun.ttf"
    font_name = font_manager.FontProperties(fname=font_location).get_name()
    matplotlib.rc('font', family=font_name)

    plt.xlabel('주요 단어')
    plt.ylabel('빈도수')
    plt.grid(True)

    #print("wordInfo.values() =", wordInfo.values())    #단어수
    Sorted_Dict_Values = sorted(wordInfo.values(), reverse=True)    #단어수 내림차순 정렬
    Sorted_Dict_Keys = sorted(wordInfo, key=wordInfo.get, reverse=True) #키순(단어)으로 내림차순 정렬
    #print("Sorted_Dict_Values=", Sorted_Dict_Values)
    #print("Sorted_Dict_Keys=", Sorted_Dict_Keys)

    plt.bar(range(len(wordInfo)), Sorted_Dict_Values, align='center')   #막대바 그래프
    plt.xticks(range(len(wordInfo)), list(Sorted_Dict_Keys), rotation='70')     #막대바 x축 라벨

    plt.show()

#[CODE 2]
def saveWordCloud(wordInfo, filename):
    print("dict(wordInfo).items() = ",dict(wordInfo).items())
    #dict(wordInfo).items() 를 가지고 cololr, size, tag 가 담긴 딕셔너리를 구성
    taglist= pytagcloud.make_tags(dict(wordInfo).items(), maxsize= 80)
    #print("taglist",taglist)
    pytagcloud.create_tag_image(taglist, filename, size= (640, 480), fontname= 'korean', rectangular=False) #워드클라우드를 이미지 로 출력
    webbrowser.open(filename)

def main():
    # 여기서 파일의 경로는 실제 JSON데이터가 저장된 경로이다
    openFileName = 'chosun_facebook_2016-10-01_2017-03-12.json'
    # openFileName = 'jtbcnews_facebook_2016-10-01_2017-03-12.json'


    cloudImagePath = openFileName + '.jpg'

    rfile = open(openFileName, 'r', encoding='utf-8').read()

    jsonData = json.loads(rfile)
    message = ''
    #[CODE 3]
    for item in jsonData:
        if 'message' in item.keys():
            #print("message1 = ", message)
            #알파벳이나 숫자로 시작하는 문자열(item['message'] => r'[^\w]')을 ' '로 치환
            message = message + re.sub(r'[^\w]', ' ' , item['message']) + ' '   # 하나의 문자열로 편집
            #print("message =", message)
    #CODE4
    nip = Okt() # 형태분석을 쉽게 하기 위해 제공
    nouns = nip.nouns(message) #message 에서 명사 단어 추출해서 리스트로 반환
    print("nouns =",nouns)

    #Counter() : 명사 단어수를 카운트해서 사전식 객체로 반환하는 클래스
    count = Counter(nouns)
    print("count=", count)

    #[CODE 5]
    wordInfo = dict()
    #Counter 에 잇는 most_common(n) 메서드를 사용하면 상위 n개 (단어와 단어수) 를 리턴해 준다.
    for tags, counts in count.most_common(50):
        if(len(str(tags)) > 1):
            wordInfo[tags] = counts
            print("%s : %d" %(tags, counts))

    showGraph(wordInfo)
    saveWordCloud(wordInfo, cloudImagePath)

if __name__ =='__main__':
    main()

