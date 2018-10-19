# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class HanbitBookItem(scrapy.Item):
    book_title = scrapy.Field() # 책 이름
    book_author = scrapy.Field() # 저자 이름
    book_translator = scrapy.Field() # 번역자 이름
    book_pub_date = scrapy.Field() #출간일
    book_isbn = scrapy.Field() #ISBN

    # define the fields for your item here like:
    # name = scrapy.Field()
    pass
