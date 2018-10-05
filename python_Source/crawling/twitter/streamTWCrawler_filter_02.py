from twitter.config import *
import oauth2
import json
import datetime
import time

def oauth2_request(consumer_key, consumer_secret, access_token, access_secret):
    try:
        consumer = oauth2.Consumer(key=consumer_key, secret=consumer_secret)
        token = oauth2.Token(key=access_token, secret=access_secret)
        client = oauth2.Client(consumer, token)         #인증정보 저장됨
        return client
    except Exception as e:
        print(e)
        return None

def getTwitterTwit(tweet, jsonResult):
    tweet_id = tweet['id_str']
    tweet_message = '' if 'text' not in tweet.keys() else tweet['text']

    screen_name = '' if 'user' not in tweet.keys() else tweet['user']['screen_name']

    tweet_link = ''
    if tweet['entities']['urls']:  # list
        for i, val in enumerate(tweet['entities']['urls']):
            tweet_link = tweet_link + tweet['entities']['urls'][i]['url'] + ''

    else:
        tweet_link = ''

    hashtags = ''
    if tweet['entities']['hashtags']:  # list
        for i, val in enumerate(tweet['entities']['hashtags']):
            hashtags = hashtags + tweet['entities']['hashtags'][i]['text'] + ''

    else:
        hashtags = ''

    if 'created_at' in tweet.keys():
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

    jsonResult.append({'post_id': tweet_id, 'message': tweet_message, 'name': screen_name,
                       'link': tweet_link, 'created_time': tweet_published, 'num_reactions': num_favorite_count,
                       'num_comments': num_comments, 'num_shares': num_shares, 'num_likes': num_likes,
                       'num_loves': num_loves, 'num_wows': num_wows, 'num_hahas': num_hahas,
                       'num_sads': num_sads, 'num_angrys': num_angrys, 'hashtags': hashtags})

def get_user_timeline(client, track):
    response, data = client.request("https://stream.twitter.com/1.1/statuse/filter.json?track="+track)
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

    jsonResult = []
    # filter_name = '탄핵, 박근혜, 광화문'
    track = '문재인, 김정은'
    # filter_name = '

    client = oauth2_request(CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_SECRET)  # 인증 준비
    f= get_user_timeline(client, track)

    try:
        f = get_user_timeline(client, track)
        cnt = 0  # 추가
        while True:
            line = f.readline()
            if line:
                try:
                    tweet = json.loads(line.decode('utf-8'))
                    print('####[Scrapped Time: %s]' % datetime.datetime.now())
                    print(tweet['text'])

                    # tweet에 담긴 정보를 jsonResult에 추가하는 부분
                    getTwitterTwit(tweet, jsonResult)
                    cnt = cnt + 1  # 추가
                    # print('cnt = ', cnt)  # 추가

                    # 종료를 시키기 위해 일부러 넣어준 부분
                    # pyCharm에선 Ctrl-C가 작동 안됨.
                    if cnt == 10:
                        break  # 추가
                except ValueError as ve:
                    print(ve)
                except KeyError as e:
                    print(e)
            else:
                # 내용이 없다는 의미
                print('#')
                time.sleep(0.1)
    except KeyboardInterrupt:
        # Ctrl-C Detected
        f.close()
        with open('filter_twitter.json', 'w', encoding='utf-8') as outfile:
            retJson = json.dumps(jsonResult, indent=4, sort_keys=True, ensure_ascii=False)

            outfile.write(retJson)

        print('%s_twitter.json SAVED' % (filter))
if __name__ == '__main__':
    main()