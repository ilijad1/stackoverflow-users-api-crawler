# -*- coding: utf-8 -*-
import scrapy
import re
from ..items import StackoverflowUserCrawlerItem

TOTAL_USERS = 11000000
USER_COUNTER = 1

class UsersSpider(scrapy.Spider):
    name = 'users'
    allowed_domains = ['stackoverflow.com/users']
    #start_urls = [l.strip() for l in open('/home/rookie/Documents/StackOverflow_Crawler/stackoverflow_user_crawler/stackoverflow_profile_links.txt').readlines()]
    start_urls = ['https://stackoverflow.com/users/10999949', 'https://stackoverflow.com/users/10999950', 'https://stackoverflow.com/users/10999951']
    def parse(self, response):
        item = StackoverflowUserCrawlerItem()

        username = response.css("html body.user-page.unified-theme div.container div#content.snippet-hidden div#mainbar-full.user-show-new div#main-content div#user-card.mt24.user-card div.grid.gs24 div.grid--cell.fl1.wmn0 div.grid.gs16 div.grid--cell.fl1.w0.overflow-x-hidden.overflow-y-auto.pr16.profile-user--about.about div.grid.fd-column.gs8.gsy div.grid--cell h2.grid.gs4.fw-wrap.ai-center.fs-headline1.lh-xs.fc-dark.wb-break-all.profile-user--name div.grid--cell.fw-bold::text").extract_first()
        bio = " ".join(response.xpath("//div[contains(@class,'grid--cell mt16')]//text()").extract())
        location = " ".join(response.xpath("(//div[@class='grid--cell fl1'])[1]//text()").extract())
        answers = response.xpath("(//div[contains(@class,'grid--cell fs-body3')])[1]//text()").extract_first()
        question = response.xpath("(//div[contains(@class,'grid--cell fs-body3')])[2]//text()").extract_first()
        people_reached = response.xpath("(//div[contains(@class,'grid--cell fs-body3')])[3]//text()").extract_first()
        social_profile = " ".join(response.css("div#user-card>div>div:nth-of-type(2)>div>div:nth-of-type(2)>div:nth-of-type(2)>ul>li:nth-of-type(2)>div>div:nth-of-type(2)>a::text").extract())
        membership_time = " ".join(response.css("div#user-card>div>div:nth-of-type(2)>div>div:nth-of-type(2)>div:nth-of-type(2)>ul>li:nth-of-type(3)>div>div:nth-of-type(2)::text").extract()) + " ".join(response.css("div#user-card>div>div:nth-of-type(2)>div>div:nth-of-type(2)>div:nth-of-type(2)>ul>li:nth-of-type(3)>div>div:nth-of-type(2)>span::text").extract())
        profile_views = response.css("div#user-card>div>div:nth-of-type(2)>div>div:nth-of-type(2)>div:nth-of-type(2)>ul>li:nth-of-type(4)>div>div:nth-of-type(2)::text").extract_first()
        #last_seen = " ".join(response.css("div#user-card>div>div:nth-of-type(2)>div>div:nth-of-type(2)>div:nth-of-type(2)>ul>li:nth-of-type(5)>div>div:nth-of-type(2)::text").extract_first()) + " ".join(response.css("div#user-card>div>div:nth-of-type(2)>div>div:nth-of-type(2)>div:nth-of-type(2)>ul>li:nth-of-type(5)>div>div:nth-of-type(2)>span::text").extract_first())
        reputation_score = response.xpath("//div[contains(@class,'grid--cell fs-title')]//text()").extract_first()
        tags_number = response.css("div#top-tags>h3>span::text").extract_first()

        #print("TAGS NUMBER = " +  re.sub('[(){}<>]', '', str(tags_number1)))

        if tags_number is not None:
            counter = int(re.sub('[(){}<>]', '', str(tags_number)))
        else:
            counter = 0

        details = {
            'social_profile': social_profile,
            'location': location,
            'profile_views': profile_views,
            'membership_time': membership_time
        }
        tags = []

        while counter > 0:
            print(counter)
            tag = response.xpath("(//a[@class='post-tag'])[" + str(counter) + "]//text()").extract_first()
            tags.append(tag)
            counter = counter - 1

        item['username'] = username
        item['bio'] = bio
        item['answers'] = answers
        item['question'] = question
        item['people_reached'] = people_reached
        #item['last_seen'] = last_seen
        item['reputation_score'] = reputation_score
        item['details'] = details
        item['tags'] = tags

        yield item
