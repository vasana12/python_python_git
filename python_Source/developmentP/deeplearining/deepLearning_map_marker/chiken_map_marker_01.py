import folium
import pandas as pd
import urllib.request
import datetime
import time
import json
import webbrowser
from Naver.config import *

# [CODE_1]
def get_request_url(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    try:
        response = urllib.request.urlopen(req)  # 정보추출
        if response.getcode() == 200:  # 상태정보 == 200 => OK(성공)라는 의미
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')  # 추출한 정보가 담겨져있움
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

# [CODE_2]
def getGeoData(address):
    base = "https://openapi.naver.com/v1/map/geocode"

    try:
        parameters = "?query=%s" % urllib.parse.quote(address) # quote() : 한글 텍스트를 퍼센트 형식으로 인코딩하기. <-> unquote()
    except:
        return None

    url = base + parameters

    retData = get_request_url(url)

    if retData == None:
        return None

    print("retData =", retData)

    jsonAddress = json.loads(retData)

    if 'result' in jsonAddress.keys():
        latitude = jsonAddress['result']['items'][0]['point']['y']
        longitude = jsonAddress['result']['items'][0]['point']['x']
    else:
        return None

    return [latitude, longitude]


def main():
    # [CODE_3]

    map = folium.Map(location=[37.5103, 126.982], zoom_start=12)

    filename1 = 'cheogajip_table2.csv'
    filename2 = 'goobne_table2.csv'
    filename3 = 'kyochon_table2.csv'
    filename4 = 'pericana_table2.csv'

    # [CODE_4]
    # ----------------------------처갓집 시작-----------------------------------------
    df = pd.read_csv(filename1, encoding='utf-8', index_col=0, header=0)
    for index, row in df.iterrows():  # df.iterrows() : 데이터 행을 반복하며 인덱스와 데이터행을 반환
        if index == 200:
            break

        geoData = getGeoData(row['store_address'])
        if geoData != None:
            folium.Marker(geoData, popup=row['store'], icon=folium.Icon(color='red')).add_to(map)
    # ----------------------------처갓집 끝-----------------------------------------

    # ----------------------------굽네 시작-----------------------------------------
    df = pd.read_csv(filename2, encoding='utf-8', index_col=0, header=0)
    for index, row in df.iterrows():  # df.iterrows() : 데이터 행을 반복하며 인덱스와 데이터행을 반환
        if index == 200:
            break
        geoData = getGeoData(row['store_address'])
        if geoData != None:
            folium.Marker(geoData, popup=row['store'], icon=folium.Icon(color='blue')).add_to(map)
    # ----------------------------굽네 끝-----------------------------------------

    # ----------------------------교촌 시작-----------------------------------------
    df = pd.read_csv(filename3, encoding='utf-8', index_col=0, header=0)
    for index, row in df.iterrows():  # df.iterrows() : 데이터 행을 반복하며 인덱스와 데이터행을 반환
        if index == 200:
            break
        geoData = getGeoData(row['store_address'])
        if geoData != None:
            folium.Marker(geoData, popup=row['store'], icon=folium.Icon(color='green')).add_to(map)
    # ----------------------------교촌 끝-----------------------------------------

    # ----------------------------페리카나 시작-----------------------------------------
    df = pd.read_csv(filename4, encoding='utf-8', index_col=0, header=0)
    for index, row in df.iterrows():  # df.iterrows() : 데이터 행을 반복하며 인덱스와 데이터행을 반환
        if index == 200:
            break
        geoData = getGeoData(row['store_address'])
        if geoData != None:
            folium.Marker(geoData, popup=row['store'], icon=folium.Icon(color='purple')).add_to(map)
    # ----------------------------페리카나 끝-----------------------------------------

    svFilename = 'two_table2.html'
    map.save(svFilename)
    webbrowser.open(svFilename) # elementary_school.html 파일을 웹브라우저로 실행

if __name__ =='__main__':
    main()
