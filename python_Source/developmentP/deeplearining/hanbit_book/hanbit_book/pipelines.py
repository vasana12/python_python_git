# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
from scrapy.exporters import JsonItemExporter # json 처리 위해 필요
from scrapy.exporters import CsvItemExporter    # csv 처리 위해 필요

class HanbitBookPipeline(object):

# Csv 형식으로 출력
#
# def __init__(self):
#     self.file = open("book_crawl.csv", 'wb')
#     self.exporter = CsvItemExporter(self.file, encoding='utf-8')
#     self.exporter.start_exporting()
#
#
# def close_spider(self, spider):
#     self.exporter.finish_exporting()
#     self.file.close()
#
#
# def process_item(self, item, spider):
#     self.exporter.export_item(item)
#     return item

    #json 형식으로 출력
    def __init__(self):
        self.file = open("book_crawl.json", 'wb')
        self.exporter = JsonItemExporter(self.file, encoding='utf-8', ensure_ascii=False)
        self.exporter.start_exporting()


    def close_spider(self, spider):
        self.exporter.finish_exporting()
        self.file.close()


    def process_item(self, item, spider):
        self.exporter.export_item(item)
        return item