#coding=utf-8
#외부라이브러리 사용안하고 url로 데이터 불러오기
import urllib
import urllib.request
import json
import datetime
from Facebook.config import *

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)  # 정보추출, url open해서 해당 페이지 정보 불러옴
        if response.getcode() == 200:  # 상태정보 == 200 => OK(성공)라는 의미
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')  # 추출한 정보가 담겨져있움,  utf-8로 디코드해서 불러옴
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

def getInstaSearchResult(token, userID, limit):
    url = "https://graph.facebook.com/v3.1/%s"  % userID
    url += "/feed?fields=attachments,message,picture,link,name,caption,description,source&limit=%d&access_token=%s" % (limit, token)
    print(url)

    retData = get_request_url(url)
    print("retData = ", retData)

    if (retData == None):  # 추출한 데이터 없어
        return None
    else:
        return json.loads(str(retData))  # JSON형식으로 리턴

def getPostData(post, jsonResult):
    try:
        if post['message'] is not None:
            message = post['message']
        else:
            message = "None"
    except:
        return

    jsonResult.append({'message': message})
    print("jsonResult= ", jsonResult)

def main():
    jsonResult = []

    limit = 10
    jsonSearch = getInstaSearchResult(access_token, userID, limit)
    print("jsonSearch = ", jsonSearch)
    print("jsonSearch['data'] = ", jsonSearch['data'])

    for post in jsonSearch['data']:
        print("post : " , post)
        # getPostData(post, jsonResult)     요건 내가 원하는 데이터만 뽑을 때

        jsonResult.append(post)

    with open('instagram01.json' , 'w', encoding = 'utf-8') as outfile:
        retJson = json.dumps(jsonResult,
                             indent=4, sort_keys=True,
                             ensure_ascii=False)
        outfile.write(retJson)

    print('facebook_url.json SAVED')


if __name__ == "__main__":
    main()