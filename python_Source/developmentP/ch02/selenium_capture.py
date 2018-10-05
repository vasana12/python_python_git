#http://phantomjs.org/download.html 판톰
#http://chromedriver.chromium.org/downloads 크롬 드라이버
from selenium import webdriver
url = "http://www.naver.com/"

#PhantomJS 드라이버 추출하기 ---1
browser1 = webdriver.PhantomJS('C:\BigDeep\phantomjs\phantomjs.exe')
#3초 대기하기
browser1.implicitly_wait(3)
#URL 읽어 들이기 ---3
browser1.get(url)
#화면을 캡처해서 저장하기
browser1.save_screenshot("Website1.png")
#브라우저 종료하기
browser1.quit()

browser2 = webdriver.Chrome('C:\BigDeep\ChromeDriver\chromedriver.exe')
browser2.implicitly_wait(3)
browser2.get(url)
browser2.save_screenshot("Website2.png")
browser2.quit()