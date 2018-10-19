import scrapy

class QouteSpider(scrapy.Spider):
    name = "quotes"

    def start_requests(self):       #자동 호출
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/,'
        ]
        for url in urls:
            print(url)
            yield scrapy.Request(url=url, callback=self.parse)  #요청, callback 함수=parse 로 전달

    def parse(self, response):          #
        page = response.url.split("/")[-2]
        print(page) # 1, 2
        filename = 'quotes-%s.html' %page
        with open(filename, 'wb') as f:
            f.write(response.body)      #응답받은 내용 중 body 에 있는 내용 출력
        self.log('Saved file %s' % filename)

