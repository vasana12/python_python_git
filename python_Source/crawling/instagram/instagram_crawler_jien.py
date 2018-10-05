import datetime
import time
import urllib
import urllib.request
import json
import cx_Oracle as oci
import re

#[CODE_1]
def get_request_url(url):
    req = urllib.request.Request(url)

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
def getInstaSearchResult(token):
    url = "https://api.instagram.com/v1/users/self/media/recent/?access_token=%s" % token
    print(url)

    retData = get_request_url(url)
    print("retData = ", retData)

    if(retData == None):        #추출한 데이터 없어
        return None
    else:
        return json.loads(str(retData))     #JSON형식으로 리턴

#[CODE_3]
def getPostData(post, jsonResult):
    user_full_name = post['user']['full_name']
    user_profile_picture = post['user']['profile_picture']
    user_username = post['user']['username']
    created_time = time.ctime(int(post['created_time']))                #timestamp(초단위) 문자스트링으로 바꾸기..
    thumbnail_image = post['images']['thumbnail']['url']

    if post['caption'] is not None:
        caption_text = post['caption']['text']
        caption_created_time = time.ctime(int(post['caption']['created_time']))
    else:
        caption_text = "None"
        caption_created_time = "None"

    if len(post['tags']) == 0 :
        tags = "None"
    else:
        tags = ''
        for tag in post['tags']:
            tags += '#' + tag
        print("tags : ", tags)

    user_has_liked = post['user_has_liked']
    likes = post['likes']['count']
    comments = post['comments']['count']
    type = post['type']

    # print("len(post['carousel_media']) : ", len(post['carousel_media']))
    # if len(post['carousel_media']) == 0:
    #     carousel_media = "None"
    # else:
    #     carousel_media = len(post['carousel_media'])
    # carousel_media_thumbnail = post['carousel_media']['images'][0]['url']
    # carousel_media = post['carousel_media']

    jsonResult.append({'user_full_name': user_full_name, 'user_username': user_username, 'user_profile_picture': user_profile_picture, 'created_time': created_time,
                      'thumbnail_image': thumbnail_image, 'caption_text': caption_text, 'caption_created_time': caption_created_time, 'user_has_liked': user_has_liked,
                      'likes': likes, 'tags': tags, 'comments': comments, 'type': type})
    print("jsonResult" ,jsonResult)
    return

#[오라클 연동]
def save_oracle(jsonResult):
    conn = oci.connect('hr/123456@localhost:1521/xe')
    cursor = conn.cursor()
    sql = "insert into instagram values (:user_full_name,:user_username, :user_profile_picture, :created_time, :thumbnail_image, " \
                           ":caption_text, :caption_created_time, :user_has_liked, :likes, :tags, :comments, :type)"

    for rec in jsonResult:
        try:
            cursor.execute(sql, rec)
        except: #데이터 중 encoding오류 데이터는 DB저장에서 일단 제외시킴
            print(rec)
            for reckey in rec:
                rec[reckey] = re.sub('[^가-힝0-9a-zA-Z<>&.?:/#\[\]]', ' ', rec[reckey])     # ^~ :~를 제외한 나머지

            cursor.execute(sql, rec)     #수정된 데이터를 DB저장
            print(rec)

    conn.commit()

def main():
    jsonResult = []
    access_token = '1945681515.438bf94.df68efd6648d49daa5e0b03d1b349a58'
    jsonSearch = getInstaSearchResult(access_token)
    print("jsonSearch = ", jsonSearch)

    for post in jsonSearch['data']:
        print("post : " , post)
        getPostData(post, jsonResult)

    with open('instagram01.json' , 'w', encoding = 'utf-8') as outfile:
        retJson = json.dumps(jsonResult,
                             indent=4, sort_keys=True,
                             ensure_ascii=False)
        outfile.write(retJson)

    print('instagram01.json SAVED')

    save_oracle(jsonResult)

if __name__ =="__main__":
    main()
