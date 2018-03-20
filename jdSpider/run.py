from scrapy import cmdline


# 爬取商品信息
# cmdline.execute("scrapy crawl jd -a serach_name=电视机".split())

#爬取评论信息
cmdline.execute("scrapy crawl JDcomment".split())