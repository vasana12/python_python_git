from selenium import webdriver

#PhantomJS 드라이버 추출하기
browser = webdriver.PhantomJS('C:\BigDeep\phantomjs\phantomjs.exe')
browser.implicitly_wait(3)
#적당한 웹 페이지 열기
browser.get("http://google.com")
#자바스크립트 실행하기
r = browser.execute_script("return 100 + 50")
print(r)
browser.quit()