import oauth2
import json
import datetime
from twitter.config import *
import cx_Oracle as oci
#[CODE 1]
def oauth2_request(consumer_key, consumer_secret, access_token, access_secret):
    try:
        consumer = oauth2.Consumer(key=consumer_key, secret=consumer_secret)
        token = oauth2.Token(key=access_token, secret=access_secret)
        client = oauth2.Client(consumer, token)         #인증정보 저장됨
        return client
    except Exception as e:
        print(e)
        return None
#[CODE 2]
def get_user_timeline(client, screen_name, count=50, include_rts='False'):  #리트윗 한 것 제외
    base = "https://api.twitter.com/1.1"
    node = "/statuses/user_timeline.json"
    fields = "?screen_name=%s&count=%s&include_rts=%s"%(screen_name,count,include_rts)
    #fields = "?screen name=%s"%(screen_name)
    url = base + node + fields

    response, data = client.request(url)
    print("data=",data)
    print("response=",response)
    try:
        if response['status'] == '200':
            return json.loads(data.decode('utf-8'))
    except Exception as e:
        print(e)
        return None

def getTwitterTwit(tweet, jsonResult):

    tweet_id = tweet['id_str']

    if 'text' not in tweet.keys():
        tweet_message = ''      # text 없으면 빈 문자열로 처리
    else:
        tweet_message = tweet['text']

    screen_name = '' if 'user' not in tweet.keys() else tweet['user']['screen_name']
    #user가 key에 존재하지 않으면 true -> screen_name 에 저장
    #or
    #user사 key 에 존재하고 screen_name 이 존재하면 -> screen_name 에 저장

    tweet_link = ''
    if tweet['entities']['urls']: #list
        for i, val in enumerate(tweet['entities']['urls']):
            tweet_link = tweet_link+tweet['entities']['urls'][i]['url']+''
            #entities 의 urls 의 i 번째 url
    else :
        tweet_link=''

    hashtags = ''
    if tweet ['entities']['hashtags']: #list #hastags 가 비어
        for i, val in enumerate(tweet['entities']['hashtags']):
            hashtags = hashtags + tweet['entities']['hashtage'][i]['text']+ ''
    else:
        hashtags = ''

    if 'created_at' in tweet.keys():
        #Twitter used UTC Format. EST = UTC + 9 (Korean Time) Format ex: Fri Feb 10 03:57:27 +0000 2017
        tweet_published = datetime.datetime.strptime(tweet['created_at'], '%a %b %d %H:%M:%S +0000 %Y')
        tweet_published = tweet_published + datetime.timedelta(hours=+9)
        tweet_published = tweet_published.strftime('%Y-%m-%d %H:%M:%S')
    else:
        tweet_published = ''

    num_favorite_count = 0 if 'favorite_count' not in tweet.keys() else tweet['favorite_count']
    num_comments = 0
    num_shares = 0 if 'retweet_count' not in tweet.keys() else tweet['retweet_count']
    num_likes = num_favorite_count
    num_loves = num_wows = num_hahas = num_sads = num_angrys = 0

    jsonResult.append({'post_id':tweet_id,'message':tweet_message,
                       'name':screen_name, 'link':tweet_link,
                       'created_time':tweet_published,'num_reactions':num_favorite_count,
                       'num_comments':num_comments, 'num_shares':num_shares,
                       'num_likes':num_likes, 'num_loves':num_loves,
                       'num_wows':num_wows, 'num_hahas':num_hahas,
                       'num_sads':num_sads, 'num_angrys':num_angrys, 'hashtags': hashtags})

#[CODE 4]
def main():
    conn = oci.connect('hr/123456@localhost:1521/xe')
    cursor = conn.cursor()  # cursor 객체 얻어오기

    sql_create = """create table twitter
                (created_time date,
                    hashtage varchar2(30),
                    link varchar2(100),
                    message varchar2(100),
                    name varchar2(100),
                    num_angrys varchar2(100),
                    num_comments varchar2(100),
                    num_hahas varchar2(100),
                    num_likes number,
                    num_loves number,
                    num_reactions varchar2(100),
                    num_sads number,
                    num_shares number,
                    num_wows number,
                    post_id varchar2(100)
                );
            """
    sql_insert = "insert into sungjuk (created_time, hashtage, link,message, name,num_angrys, num_comments, \
               num_hahas, num_likes, num_loves,num_reactions,num_sads,num_shares,num_wows,post_id )values(?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)"

    screen_name = "kjyoung9300" #krungy21:트위터 계정 사용

    num_posts = 50

    jsonResult = []             #json 형식으로 데이터 저장

    client = oauth2_request(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN , ACCESS_SECRET) #인증 준비
    tweets = get_user_timeline(client, screen_name) #토큰 생성
    #print(len(tweets))

    for tweet in tweets:
        getTwitterTwit(tweet, jsonResult)
        cursor.execute(sql_insert, jsonResult[i][],jsonResult[i],
              jsonResult[3],jsonResult[1],jsonResult[2],
              jsonResult[13],jsonResult[6],jsonResult[11],
              jsonResult[8],jsonResult[9],jsonResult[5],
              jsonResult[12],jsonResult[7],jsonResult[10],jsonResult[0])
    print(jsonResult[0])
    with open('%s_twitter.json' %(screen_name), 'w', encoding='utf-8') as outfile:
        str_= json.dumps(jsonResult,
                         indent=4, sort_keys=True,
                         ensure_ascii=False)
        outfile.write(str_) #출력 파일생성
    print('%s_twitter.json SAVED'%(screen_name))

if __name__ =='__main__':
    main()
    # 오라클 서버와 연결(Connection 맺기)
    conn = oci.connect('hr/123456@localhost:1521/xe')
    cursor = conn.cursor()  # cursor 객체 얻어오기

