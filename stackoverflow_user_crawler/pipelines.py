# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html
import json
import os

class StackoverflowUserCrawlerPipeline(object):
    def process_item(self, item, spider):
        FILE_PATH = '/home/rookie/stackoverflow_json_files/'

        if not os.path.isdir(FILE_PATH):
            print("Creating Directory: " + FILE_PATH)
            os.makedirs(FILE_PATH, 755)

        if not os.path.isfile(FILE_PATH + item['username']):
            print("Writing to file: " + FILE_PATH + item['username'])
            with open(FILE_PATH + item['username'], 'w') as wr:
                line = json.dumps(
                    dict(item),
                    sort_keys=True,
                    indent=4,
                    separators=(',', ': ')
                )
                wr.write(line)
                wr.close()
        else:
            pass
        return item
