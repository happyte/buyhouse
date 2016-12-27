# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class FangjiaItem(scrapy.Item):
    # define the fields for your item here like:
    FANGJIA_ADDRESS = scrapy.Field()  # 住房地址
    FANGJIA_NAME = scrapy.Field()       # 名字
    FANGJIA_PRICE = scrapy.Field()      # 房价
    FANGJIA_URL = scrapy.Field()        # 房源url
