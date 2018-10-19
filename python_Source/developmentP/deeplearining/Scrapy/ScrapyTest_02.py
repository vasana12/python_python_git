import scrapy

class BlogSpider(scrapy.Spider):
    name = 'blogspider'
    start_urls = ['https://blog.scrapinghub.com']

    def parse(self, response):
        with open('aaaa.txt', 'ab') as f:
            for title in response.css('.post-header>h2'):

                f.write(str(title.css('a ::text').extract_first() + '\n').encode('utf-8'))
                yield {'title': title.css('a :;text').extract_first()}

            for next_page in response.css('div.prev-post > a'):
                yield response.follow(next_page, self.parse)