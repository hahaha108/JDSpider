# -*- coding: utf-8 -*-
import scrapy
from ..items import JdcommentItem


#评论抓取
class JdcommentSpider(scrapy.Spider):
    name = 'JDcomment'
    allowed_domains = ['jd.com']
    start_urls = ['https://item.jd.com/4824733.html']

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
    #
    # def parseCom(self,response):


