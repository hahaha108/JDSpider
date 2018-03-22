import re

import os
from scrapy import cmdline
from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from jdSpider.jd.spiders import jd,JDcomment


class JD_spider:

    def __init__(self):
        pass

    def crawl(self,serach_name):
        '''
        此方法用于爬取商品信息列表
        :param serach_name: 为所爬取类别关键字，如：'手机'，类型为str
        '''
        cmdline.execute("scrapy crawl jd -a serach_name={0}".format(serach_name).split())


    def crawl_comment(self,urls,pages=None):
        '''
        此方法用于爬取评论
        :param urls: 为商品详情页的url，如：'https://item.jd.com/11856959514.html'
                    可以为一个或多个，参数类型为str或者list
        :param pages: 设置爬取的页数，默认 None表示全部爬取
        '''

        settings = get_project_settings()
        process = CrawlerProcess(settings=settings)
        process.crawl(JDcomment.JdcommentSpider,urls,pages)

        process.start()

    def get_urls(self,number = None):
        '''
        用于从爬到的商品信息中获取url列表
        :param number: 获取url的个数，默认None表示全部获取
        :return: 返回商品对应的url列表
        '''
        if not os.path.exists('京东商品信息.txt'):
            raise RuntimeError('未检索到商品信息，请先爬取')

        with open('京东商品信息.txt','r',encoding='utf-8') as file:
            txt = file.read()
            urllist = re.findall('购买网址：(.+?html)',txt)
            if not  number:
                return urllist
            else:
                return urllist[:number]

# if __name__ == '__main__':
#     JD = JD_spider()
#     print(JD.get_urls())
