# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from .items import JdcommentItem


class JdspiderPipeline(object):
    def __init__(self):
        self.file = open('./京东商品信息.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        if spider.name == 'jd':
            for name,content in zip(item['name'],item['content']):
                self.file.write(name+":"+content+"\n")
            self.file.write('购买网址：'+item['url']+'\n\n\n\n')
            self.file.flush()
        return item

    def __del__(self):
        self.file.close()

class JdcommentPipeline(object):
    def __init__(self):
        self.file = open('./商品评论信息.txt','w',encoding='utf-8')

    def process_item(self, item, spider):
        if spider.name == 'JDcomment':
        # if isinstance(item, JdcommentItem):
            print("1111111")
            self.file.write("日期："+item['date']+"\n")
            self.file.write(item['content']+'\n\n-----------------------------\n\n')
            self.file.flush()
        return item

    def __del__(self):
        self.file.close()