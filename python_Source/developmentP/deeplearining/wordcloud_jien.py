import json
import re
# pygame, simplejson, pytagcloud모듈 설치
#from konlypy.tag import Twitter # Twitter -> Okt로 수정할것
from konlpy.tag import Okt
from collections import Counter

import matplotlib.pyplot as plt
import matplotlib       #venv#Lib\site-packages\pytagcloud\fonts\font.json 파일 편집하고 해당 폰트파일을 복사할것.
from matplotlib import font_manager

import pytagcloud   #pygame, simplejson모듈 추가로 설치할것
import webbrowser

#[CODE_1]
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

#[CODE_2]
def saveWordCloud(wordInfo, filename):
    print("dict(WordInfo).items() = ", dict(wordInfo).items())
    #dict(wordInfo).items()를 가지고 color, size, tag가 담긴 딕셔너리를 구성
    taglist = pytagcloud.make_tags(dict(wordInfo).items(), maxsize=80)
    #print("taglist ", taglist)
    pytagcloud.create_tag_image(taglist, filename, size=(640, 480), fontname='korean', rectangular=False)       #워드클라우드를 이미지로 출력
    webbrowser.open(filename)

def main():
    #여기서 파일의 경로는 실제 JSON데이터가 저장된 경로이다
    #openFileName = 'chosun_facebook_2016-10-01_2017-03-12.json'
    openFileName = 'jtbcnews_facebook_2016-10-01_2017-03-12.json'

    cloudImagePath = openFileName + '.jpg'

    rfile = open(openFileName, 'r', encoding='utf-8').read()

    jsonData = json.laods(rfile)
    message = ''

    #[CODE_3]
    for item in jsonData:
        if 'message' in item.keys():
            #print("message1 = ", message)
            #알파벳이나 숫자로 시작하는 문자열(item['message'] => r'[^\w]')을 ' '로 치환
            message = message + re.sub(r'[^\w]', ' ' , item['message']) + ' '   # 하나의 문자열로 편집
            #print("message =", message)

    #[CODE_4]
    nlp = Okt()   #형태분석을 쉽게 하기 위해서 제공
    nouns = nlp.nouns(message)   #message에서 명사 단어 추출해서 리스트로 반환
    print("nouns = ", nouns)

    #Counter() : 명사 단어수를 카운트해서 사전식 객체로 반환하는 클래스
    count = Counter(nouns)
    print("count = ", count)

    #[CODE_5]
    wordInfo = dict()
    #Counter에 있는 most_com