# -*- coding: utf-8 -*-
import scrapy
from scrapy.linkextractors import LinkExtractor
from scrapy.spiders import CrawlSpider, Rule


class BookCrawlSpider(CrawlSpider):
    #크롤러의 이름입니다. 실제 크롤링을 실행할 때 사용합니다.
    name = 'book_crawl'

    #크롤러 실행을 허용할 도메인을 여기서 지정합니다.
    #해당 서버에서 실행되다가 허용된 도메인 이외는 무시합니다.
    allowed_domains = ['hanbit.co.kr']


    #시작점으로 사용할 url 입니다.
    #리스트로 지정해 한 번에 여러 웹 페이지에서 크롤링을 시작하게 할 수 있습니다.
    start_urls = ['http://hanbit.co.kr/store/books/category_list.html?cate_cd=001',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=002',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=003',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=004',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=005',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=006',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=007',
                  'http://hanbit.co.kr/store/books/category_list.html?cate_cd=008',
    ]

    #크롤러가 어떻게 작동할지 규칙을 설정합니다.
    #크롤러는 시작점의 모든 링크를 검사한 후,
    #규칙에 맞는 링크가 있으면 정해진 콜백 메서드를 실행합니다.
    #follow가 True 이면 해당 페이지의 링크를 재귀적으로 위 작업을 반복합니다.
    rules = (
        Rule(
            # 크롤링할 링크를 정규 표현식을 이용해서 표현합니다.
            # store/books/look.php?p_code=B8463790401
            LinkExtractor(allow=r'store/books/look.php\?p_code=.*'),

            #해당 링크에 요청을 보내고 응답이 오면 실행할 콜백 메서드를 지정합니다.
            callback ='parse_item',

            #True 로 설정되어 있으면, 응답에 다시 한번 rules 를 적용해 재귀적으로 실행합니다.
            follow=True),
        #이렇게 여러 개으 규칙을 설정할 수 있습니다.
        #Rule(LinkExtractor(allow=r'.*'), callback = 'parse_item', follow=True),
        #store/books/category_list.html?page=2%cata_cd=003&srt=p_pub_date
        #Rule(LinkExtractor(allow=r'store/books/category_list\.html\?page=\d+&srt=p_pub_date'))
    )

    #CrawlSpider 클래스를 상속받으면 parse() 가 아닌 parse_item() 으로 작성. (오버라이딩)
    def parse_item(self, response):
        """rules 를 통과한 링크에 요청을 보내 응답을 받으면 Rule()에 설정한 콜백 메서드를 해당
        응답 결과에 실행합니다.
        따라서 response 를 파라미터로 받고Xpath 라든가 CSS 선택자를 이용해서 원하는 요소를 추출
        할 수 있습니다.
        """
        #앞서 설정한 item 에 맞춰 딕셔너리를 채우고 반환합니다.
        data = {}

        #책 이름
        data['book_title'] = response.xpath('//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/h3/text()').extract()
        #경로 찾는 법 : 오른쪽 마우스 클릭 후 copyXpath
        #//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/h3
        # 저자
        data['book_author'] = response.xpath(
            '//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[1][strong/text()="저자 : "]/span/text()').extract()
        '//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[1]/span'
        # 출간일
        data['book_pub_data'] = response.xpath(
            '//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[1][strong/text()="출간 : "]/span/text()').extract()

        # 번역자 이름
        data['book_translator'] = response.xpath(
            '//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[1][strong/text()="번역 : "]/span/text()').extract()

        data['book_isbn'] = response.xpath(
            '//*[@id="container"]/div[1]/div[1]/div[1]/div[2]/ul/li[4][strong/text()="ISBN : "]/span/text()').extract()

        print(data)
        return data
        #i['domain_id'] = response.xpath('//input[@id="sid"]/@value').extract()
        #i['name'] = response.xpath('//div[@id="name"]').extract()
        #i['description'] = response.xpath('//div[@id="description"]').extract()