# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface

from news_about_events.settings import FEED_EXPORT_FIELDS
import os

from scrapy import signals
from scrapy.exporters import CsvItemExporter


class NewsAboutEventsPipeline:
    def __init__(self):
        self.filename: str = None

    @classmethod
    def from_crawler(cls, crawler):
        pipeline = cls()
        crawler.signals.connect(pipeline.spider_opened, signals.spider_opened)
        crawler.signals.connect(pipeline.spider_closed, signals.spider_closed)
        return pipeline

    def spider_opened(self, spider):
        self.file = open(f'default.csv', 'w+b')
        self.exporter = CsvItemExporter(self.file)
        self.exporter.fields_to_export = FEED_EXPORT_FIELDS
        self.exporter.start_exporting()

    def spider_closed(self, spider):
        self.exporter.finish_exporting()
        self.file.close()
        os.rename("default.csv", f"{self.filename}")

    def process_item(self, item, spider):
        self.filename = item.pop("d_csv")
        self.exporter.export_item(item)
        return item
