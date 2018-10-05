import json
JSON_FILE="./test.json"
JSON_DATA={}

def read_json(filename):
    f = open(filename, 'rt') #문자열로 읽어옴
    #f = open(filename,'rt',encoding='utf-8')
    js = json.loads(f.read()) # 문자열로 읽어온 데이터 제이슨 형태로 변환
    f.close()
    return js

def proc_json():
    global JSON_FILE
    global JSON_DATA
    JSON_DATA = read_json(JSON_FILE)
    print(JSON_DATA)
    repos = JSON_DATA['snapshot']['repos']
    userid = JSON_DATA['snapshot']['userid']
    pw = JSON_DATA['snapshot']['passwd']

    print("repos value:"+repos)
    print("userid value:" + userid)
    print("pw value:"+pw)

if __name__=='__main__':
    proc_json()