# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class NewsAboutEventsItem(scrapy.Item):
    header = scrapy.Field()
    text = scrapy.Field()
    tag = scrapy.Field()
    link = scrapy.Field()
    d_csv = scrapy.Field()
