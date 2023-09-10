# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class StackoverflowUserCrawlerItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    username = scrapy.Field()
    bio = scrapy.Field()
    tags = scrapy.Field()
    answers = scrapy.Field()
    question = scrapy.Field()
    people_reached = scrapy.Field()
    details = scrapy.Field()
    profile_views = scrapy.Field()
    last_seen = scrapy.Field()
    reputation_score = scrapy.Field()

