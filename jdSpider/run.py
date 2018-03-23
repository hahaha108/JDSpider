from jdSpider.main_spider import JD_spider

if __name__ == '__main__':
    # 获取对象
    spider = JD_spider()
    # 爬取商品
    # spider.crawl('苹果手机')
    # 获取商品url列表
    urls = spider.get_urls(10)
    print(urls)
    # 爬取评论
    spider.crawl_comment(urls,5)
