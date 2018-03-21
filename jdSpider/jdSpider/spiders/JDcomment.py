# -*- coding: utf-8 -*-
import json
import re

import requests
import scrapy
import time

from ..items import JdcommentItem


#评论抓取
class JdcommentSpider(scrapy.Spider):
    name = 'JDcomment'
    allowed_domains = ['jd.com']
    start_urls = ['https://item.jd.com/4824733.html']
    number = re.findall(r"com/(\d+)\.html", start_urls[0])[0]

    comment_page_baseurl = 'https://sclub.jd.com/comment/productPageComments.action?productId=' + number +'&score=0&sortType=5&page={0}&pageSize=10'

    def parse(self, response):
        print(response.text)
        comlist = response.xpath("//div[@id='hidcomment']/div[@class='item']//div[@class='o-topic']")
        print(comlist)
        for com in comlist:
            item = JdcommentItem()
            item['content'] = com.xpath(".//a/text()").extract()[0]
            item['date'] = com.xpath(".//span[@class='date-comment']/text()").extract()[0]

            yield item
    #     self.parseCom(response)
        page = 0
        while True:
            page += 1
            requset_url = self.comment_page_baseurl.format(str(page))
            comment_response_str = requests.get(requset_url).text
            response_json = json.loads(comment_response_str)

            comments = response_json['comments']
            for comment in comments:
                item = JdcommentItem()
                item['content'] = comment['creationTime']
                item['date'] = comment['content']

                yield item
            time.sleep(5)

    # def parseCom(self,response):


