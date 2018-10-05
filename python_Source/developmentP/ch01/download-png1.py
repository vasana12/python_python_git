#라이브러리 읽어 들이기 ---(#1)

import urllib.request
#URL과 저장 경로 지정하기
url = "http://file.mk.co.kr/meet/neds/2017/05/image_readtop_2017_320929_14947258072880662.jpg"
savename = "test.png"
#다운로드 ---(#2)
urllib.request.urlretrieve(url, savename)
print("저장되었습니다...!")