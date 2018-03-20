# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html


class JdspiderPipeline(object):
    def __init__(self):
        self.file = open('./京东商品信息.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        for name,content in zip(item['name'],item['content']):
            self.file.write(name+":"+content+"\n")
        self.file.write('购买网址：'+item['url']+'\n\n\n\n')
        self.file.flush()
        return item

    def __del__(self):
        self.file.close()
