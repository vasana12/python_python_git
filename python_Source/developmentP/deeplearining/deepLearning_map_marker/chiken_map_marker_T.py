import folium
import pandas as pd
import urllib.request
import datetime
import time
import json
import webbrowser
from Naver.config import *
from pandas import Series, DataFrame

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

    print("###########페리카나#########")
    filename = 'pericana_table2.csv'
    df = pd.read_csv(filename, encoding='utf-8', index_col=0, header=0)
    geoData =[]
    for index, row in df.iterrows():
        if row['sido'] == '서울특별시':
            geoData = getGeoData(row['store_address'])
            if geoData != None:
                folium.Marker(geoData, popup=row['store'], icon=folium.Icon(color='purple')).add_to(map)

    print("##########교촌치킨#########")
    filename = 'kyochon_table2.csv'
    df = pd.read_csv(filename, encoding='utf-8', index_col=0, header=0)
    geoData = []
    for index, row in df.iterrows():
        if row['sido'] == '서울특별시':
            geoData = getGeoData(row['store_address'])
            if geoData != None:
                folium.Marker(geoData, popup=row['store'], icon=folium.Icon(color='green')).add_to(map)

    print("##########처갓집#########")
    filename = 'cheogajip_table2.csv'
    df = pd.read_csv(filename, encoding='utf-8', index_col=0, header=0)
    geoData = []
    for index, row in df.iterrows():
        if row['sido'] == '서울특별시':
            geoData = getGeoData(row['store_address'])
            if geoData != None:
                folium.Marker(geoData, popup=row['store'], icon=folium.Icon(color='red')).add_to(map)

    print("##########굽네치킨#########")
    filename = 'goobne_table2.csv'
    df = pd.read_csv(filename, encoding='utf-8', index_col=0, header=0)
    geoData = []
    for index, row in df.iterrows():
        if row['sido'] == '서울특별시':
            geoData = getGeoData(row['store_address'])
            if geoData != None:
                folium.Marker(geoData, popup=row['store'], icon=folium.Icon(color='blue')).add_to(map)

    #[CODE]
    map.save("geomap.html")
    webbrowser.open("geomap.html")

if __name__ =='__main__':
    main()
