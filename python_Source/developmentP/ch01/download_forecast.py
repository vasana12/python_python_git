import urllib.request
import urllib.parse
API ="http://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
#매개변수를 URL 인코딩합니다.---#1
values1 ={
    'stnld' : 108, 'date':20181001
}
values2 ={
    'date':20181001
}
params1 = urllib.parse.urlencode(values1)
params2 = urllib.parse.urlencode(values2)
#요청 전용 URL 을 생성합니다. ---#2
url = API + "?" + params1+"&"+params2
print("url=", url)
#다운로드합니다. ---#3
data = urllib.request.urlopen(url).read()
savename= "forecast.xml"
text = data.decode("utf-8")
print(text)
with open(savename,mode="wb") as f:
    f.write(data)