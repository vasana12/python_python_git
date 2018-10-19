import urllib.request
import datetime
import json
from crawling.Naver.config import *
import cx_Oracle as oci
import re

#[CODE_1]
def get_request_url(url):
    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-Id", client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    try:
        response = urllib.request.urlopen(req)      #정보추출
        if response.getcode() == 200:               #상태정보 == 200 => OK(성공)라는 의미
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')      #추출한 정보가 담겨져있움
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None

#[CODE_2]
def getNaverSearchResult(sNode, search_text, page_start, display):

    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" % sNode
    parameters = "?query=%s&start=%s&display=%s" % (urllib.parse.quote(search_text), page_start, display)

    url = base + node + parameters

    retData = get_request_url(url)
    #print("retData = ", retData)

    if(retData == None):        #추출한 데이터 없어
        return None
    else:
        print(retData)
        return json.loads(str(retData))     #JSON형식으로 리턴

#[CODE_3]
def getPostData(post, jsonResult):
    title = post['title']
    description = post['description']
    ##org_link = post['originallink']       #news
    bloggerlink = post['bloggerlink']      #blog를 검색할때
    link = post['link']
    pDate = post['postdate']
    bloggername = post['bloggername']

    ##Tue, 14 Feb 2017 18:46:00 +0900
    #pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    #pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'bloggerlink': bloggerlink, 'bloggername':bloggername, 'description':description,
                       'link': link, 'pDate':pDate,'title':title })
    return

#[오라클 연동]
def save_oracle(jsonResult):
    conn = oci.connect('hr/123456@localhost:1521/xe')
    cursor = conn.cursor()
    sql = "insert into naverBlog values (:bloggerlink, :bloggername, :description, :link, :pDate, :title)"

    # 1번째 방법 #사전객체
    # #cursor.executemany(sql, jsonResult)
    # for rec in jsonResult:
    #     try:
    #         cursor.execute(sql, rec)
    #     except:     #데이터중 encodidng 오류 데이터는 db저장에서 제외시킴
    #         pass

    #두번째
     # newdata = []    #사전(dict)객체를 튜플(tuple) 객체로 변환 후 저장
     # for data in jsonResult:
     #    newdata.append(str(data["bloggerlink"]).encode('utf-8').decode(encoding='utf-8').replace('\xa9','').replace('\xa0','')\
     #                   .replace('\u2013','').replace('\u200b','').replace('\u2027',''),
     #                   str(data["bloggername"]).encode('utf-8').decode(encoding='utf-8').replace('\xa9', '').replace('\xa0', '') \
     #                   .replace('\u2013', '').replace('\u200b', '').replace('\u2027', ''),
     #                   str(data["description"]).encode('utf-8').decode(encoding='utf-8').replace('\xa9', '').replace('\xa0', '') \
     #                   .replace('\u2013', '').replace('\u200b', '').replace('\u2027', ''),
     #                   str(data["link"]).encode('utf-8').decode(encoding='utf-8').replace('\xa9', '').replace('\xa0', '') \
     #                   .replace('\u2013', '').replace('\u200b', '').replace('\u2027', ''),
     #                   str(data["pDate"]).encode('utf-8').decode(encoding='utf-8').replace('\xa9', '').replace('\xa0', '') \
     #                   .replace('\u2013', '').replace('\u200b', '').replace('\u2027', ''),
     #                   str(data["title"]).encode('utf-8').decode(encoding='utf-8').replace('\xa9', '').replace('\xa0', '') \
     #                   .replace('\u2013', '').replace('\u200b', '').replace('\u2027', '')
     #                   )
     #

    # 3번째 방법
    for rec in jsonResult:
        try:
            cursor.execute(sql, rec)
        except: #데이터 중 encoding오류 데이터는 DB저장에서 일단 제외시킴
            print(rec)
            for reckey in rec:
                rec[reckey] = re.sub('[^가-힝0-9a-zA-Z<>&.?:/#\[\]\\s]', ' ', rec[reckey])     #[]에 없는 문자를 제거, ^~ :~를 제외한 나머지

            cursor.execute(sql, rec)     #수정된 데이터를 DB저장

            print(rec)

    conn.commit()


def main():
    jsonResult = []

    #'news', 'blog', 'cafearticle'
    sNode = 'blog'      #블로그에서 검색할거야ㅑㅑㅑ
    search_text = '문재인'
    display_count = 100      #1000개 출력, 1번에 100개씩 추출..?

    jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)
    print("jsonSearch = ", jsonSearch)

    while ((jsonSearch != None) and (jsonSearch['display'] != 0)):      #추출한 데이터가 있을 때
        for post in jsonSearch['items']:    # 'items' key에 가사가 저장되어 있음
            print(post)
            getPostData(post, jsonResult)

        nStart = jsonSearch['start'] + jsonSearch['display']
        jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)

    with open('%s naver_%s_DB.json' % (search_text, sNode), 'w', encoding = 'utf-8') as outfile:
        retJson = json.dumps(jsonResult,
                             indent=4, sort_keys=True,
                             ensure_ascii=False)
        outfile.write(retJson)

    print('%s_naver_%s.json SAVED' % (search_text, sNode))

    save_oracle(jsonResult)

if __name__ == "__main__":
    main()