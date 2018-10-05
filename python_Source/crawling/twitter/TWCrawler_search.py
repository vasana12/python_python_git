from twitter.config import *
import oauth2
import json



def oauth2_request(consumer_key, consumer_secret, access_token, access_secret):
    try:
        consumer = oauth2.Consumer(key=consumer_key, secret=consumer_secret)
        token = oauth2.Token(key=access_token, secret=access_secret)
        client = oauth2.Client(consumer, token)         #인증정보 저장됨
        return client
    except Exception as e:
        print(e)
        return None

def get_user_timeline(client, q):
    response, data = client.request("https://api.twitter.com/1.1/search/tweets.json?q="+q)
    print("data=",data)
    print("response=",response)
    print()
    try:
        if response['status'] == '200':
            return json.loads(data.decode('utf-8'))
    except Exception as e:
        print(e)
        return None

def main():
    client = oauth2_request(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET) #인증 준비
    q = input('검색할 키워드 입력=>')
    res = get_user_timeline(client, q) #토큰 생성

    with open('search_twitter.json', 'w', encoding='utf8') as outfile:
        setting_res = json.dumps(res,
                                 indent=4,
                                 sort_keys=True,
                                 ensure_ascii=False)
        outfile.write(setting_res)
    print(setting_res)
    print('search_twitter.json SAVED')

if __name__ == '__main__':
    main()