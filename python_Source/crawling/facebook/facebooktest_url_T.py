import urllib.request
import json
import datetime

def get_request_url(url):
    req = urllib.request.Request(url)

    try:
        response = urllib.request.urlopen(req)  # 정보추출, url open해서 해당 페이지 정보 불러옴
        if response.getcode() == 200:  # 상태정보 == 200 => OK(성공)라는 의미
            print("[%s] Url Request Success" % datetime.datetime.now())
            return response.read().decode('utf-8')  # 추출한 정보가 담겨져있움, utf-8로 디코드해서 불러옴
    except Exception as e:
        print(e)
        print("[%s] Error for URL : %s" % (datetime.datetime.now(), url))
        return None


if __name__ == "__main__":
    base = "https://graph.facebook.com/v3.1/"
    id = "2202665160008650"
    fields = "attachments,message,picture,link,name,caption,description,source"
    access_token = "EAAFYTaMh9ZCIBAEafElYY5X77t3HKZAlIINV2A49BHTOzJ5k8upiCVeQznvaVsjvGz3ZCK8c5yshazNDMkneOeyHpeldysCemDcGjlZB03GZCvkD1ZBS7ZAx0kCZCLReZCoUVAPXcaFUOprLfiSZA2DzfsI1ZB3DM4vq6IoRBFSg6Rpvizrq6IXO4AYnvyRZB0Xlk3fbvuRByTookkL064TEWZAs4"
    limit = "10"

    url = base + id + "/feed?fields" + fields + "&access_token=" + access_token + "&" + limit

    res = get_request_url(url)
    json_res = json.loads(res)

    f = open("facebook_posts_04.txt", "wt")
    # f = open("facebook_posts_04.json", "w", encoding='utf-8')

    print(json_res)
    # f.write(json.dumps(json_res, indent=4, sort_keys=True, ensure_ascii=False))
    # sort_keys : json형식으로 이뿌게 정렬, ensure_ascii-false한글출력

    f.write(res)

    print("===========================================================================")
    for res in json_res['data']:
        print(res)

        for key in res:
            print(key, ":", res[key])