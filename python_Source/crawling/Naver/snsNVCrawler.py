import urllib.request
import datetime
import json
from Naver.config import*
import cx_Oracle as oci
import re
#[CODE 1]
def get_request_url(url):

    req = urllib.request.Request(url)
    req.add_header("X-Naver-Client-id",client_id)
    req.add_header("X-Naver-Client-Secret", client_secret)
    try:
        response = urllib.request.urlopen(req)
        if response.getcode() == 200:
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None
#[CODE 2]
def getNaverSearchResult(sNode, search_text, page_start, display):

    base = "https://openapi.naver.com/v1/search"
    node = "/%s.json" %sNode
    parameters = "?query=%s&start=%s&display=%s" %(urllib.parse.quote(search_text),page_start,display)

    url = base + node + parameters

    retData = get_request_url(url)
    #print("retTData =",retData)

    if(retData == None):
        return None
    else:
        print(retData)
        return json.loads(str(retData))

#[CODE 3]
def getPostData(post, jsonResult):

    title = post['title']
    description = post['description']
    org_link = post['originallink']
    # org_link = post['bloggerlink']
    link = post['link']
    # pDate = post['postdate']
    # bloggername = post['bloggername']
    #Tue, 14 Feb 2017 18:46:00 +0900
    pDate = datetime.datetime.strptime(post['pubDate'], '%a, %d %b %Y %H:%M:%S +0900')
    pDate = pDate.strftime('%Y-%m-%d %H:%M:%S')

    jsonResult.append({'title':title, 'description':description,
                       'org_link':org_link, 'link':link,
                       'pDate':pDate})
    return

def main():
    jsonResult = []

    # 'news', 'blog', 'cafearticle'
    sNode = 'news'
    search_text = '문재인'
    display_count = 100

    jsonSearch = getNaverSearchResult(sNode, search_text, 1, display_count)
    print("jsonSearch=", jsonSearch)

    while((jsonSearch != None) and (jsonSearch['display'] !=0)):
        for post in jsonSearch['items']: # 'items' key 에 기사가 저장되어 있음
            getPostData(post,jsonResult)

        nStart = jsonSearch['start'] + jsonSearch['display']
        jsonSearch = getNaverSearchResult(sNode, search_text, nStart, display_count)
    with open('%s_naver_%s.json' %(search_text, sNode), 'w',encoding='utf-8') as outfile:
        retJson = json.dumps(jsonResult,
                             indent=4, sort_keys=True,
                             ensure_ascii = False,)
        outfile.write(retJson)

    save_oracle(jsonResult)
    print('%s_naver_%s.json SAVED' % (search_text, sNode))

def save_oracle(jsonResult):
    # 오라클 서버와 연결(Connection 맺기)
    conn = oci.connect('hr/123456@localhost:1521/xe')
    cursor = conn.cursor()  # cursor 객체 얻어오기
    sql = "insert into naverNews values (:description, :link, :org_link, :pDate,:title)"

    for rec in jsonResult :
        try:
            cursor.execute(sql,rec)
        except: #데이터중 encoding 오류 데이터는 DB 저장에서 일단 제외시킴
            print("rec1=",rec)
            for reckey in rec:
                rec[reckey] = re.sub('[^가-힝0-9a-zA-Z<>&.?:/#\[\]]','', rec[reckey]) # [] 에 없는 문자를 제거
            cursor.execute(sql,rec)
             #수정된 데이터를 DB 지정
            print(rec)
    conn.commit()
    # newdata = []  # 사전(dict) 객체를 튜플(tuple) 객체로 변환후 저장
    # for data in jsonResult:
    #     newdata.append((str(data["description"]).encode('utf-8').decode(encoding='utf-8').replace('\xa9','').replace('\xa0','').replace('\u2013','').replace('\u200b','').replace('\u2027','').replace('\u2027','').replace('\u2219','').replace('\u2022','').replace('\ufffd',''),
    #                     str(data["link"]).encode('utf-8').decode(encoding='utf-8').replace('\xa9', '').replace('\xa0','').replace('\u2013','').replace('\u200b','').replace('\u2027','').replace('\u2027','').replace('\u2219','').replace('\u2022','').replace('\ufffd',''),
    #                     str(data["org_link"]).encode('utf-8').decode(encoding='utf-8').replace('\xa9', '').replace('\xa0','').replace('\u2013','').replace('\u200b','').replace('\u2027','').replace('\u2027','').replace('\u2219','').replace('\u2022','').replace('\ufffd',''),
    #                     str(data["pDate"]).encode('utf-8').decode(encoding='utf-8').replace('\xa9', '').replace('\xa0','').replace('\u2013','').replace('\u200b','').replace('\u2027','').replace('\u2027','').replace('\u2219','').replace('\u2022','').replace('\ufffd',''),
    #                     str(data["title"]).encode('utf-8').decode(encoding='utf-8').replace('\xa9', '').replace('\xa0','').replace('\u2013','').replace('\u200b','').replace('\u2027','').replace('\u2027','').replace('\u2219','').replace('\u2022','').replace('\ufffd','')))
    #
    # sql = "insert into naverNews values (:description, :link, :org_link, :pDate,:title)"
    # cursor.executemany(sql, newdata)
    # conn.commit()
    # sql = "insert into naverNews values (:description, :link, :org_link, :pDate, :title)"
    # #cursor.executemany(sql, jsonResult)
    # for rec in jsonResult:
    #     #print(rec)
    #     try:
    #         cursor.execute(sql,rec)
    #     except: #데이터중 encoding 오류 데이터는 DB 저장에서 제외시킴
    #         pass
    # conn.commit()

if __name__=='__main__':
    main()











