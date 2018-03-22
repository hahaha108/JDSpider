# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import random

import os

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
    # def __init__(self):
    #     self.file = open(str(random.randint(1,99999))+ '.txt','w',encoding='utf-8')

    url = ''

    def process_item(self, item, spider):
        if spider.name == 'JDcomment':
            filename = item['name'] + '.txt'
            filepath = './京东商品评论'
            if not os.path.exists(filepath):
                os.makedirs(filepath)
            filepath = os.path.join(filepath,filename)

            if not os.path.exists(filepath):
                file = open(filepath,'w',encoding='utf-8')
                self.url =item['url']
                file.write(self.url + '\n\n')
            else:
                #有些同类页面评论内容重复，判断防止重复
                if item['url'] == self.url:
                    file = open(filepath,'a',encoding='utf-8')
                else:
                    return item

            # if isinstance(item, JdcommentItem):
            #     print("1111111")
            file.write("日期："+item['date']+"\n")
            file.write(item['content']+'\n\n-----------------------------\n\n')
            # file.flush()
            file.close()
        return item

