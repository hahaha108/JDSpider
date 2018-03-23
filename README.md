# JDSpider<br>
## 京东爬虫
可以实现输入一个关键字后自动爬取相关的商品信息，也可以用于自定义爬取商品的评论。

## 使用方法
1.创建一个JD_spider实例对象<br>
2.选择爬取方法直接调用,一共有3种方法：
- crawl:用于抓取商品信息；
- crawl_comment:用于抓取评论；
- get_urls:返回爬取到的商品信息的url列表
<br>具体如下：
```python
    def crawl(self,serach_name):
        '''
        此方法用于爬取商品信息列表
        :param serach_name: 为所爬取类别关键字，如：'苹果手机'，类型为str
        '''
```
```python
    def crawl_comment(self,urls,pages=None):
        '''
        此方法用于爬取评论
        :param urls: 为商品详情页的url，如：'https://item.jd.com/11856959514.html'
                    可以为一个或多个，参数类型为str或者list
        :param pages: 设置爬取的页数，默认 None表示全部爬取
        '''
```
```python
    def get_urls(self,number = None):
        '''
        用于从爬到的商品信息中获取url列表
        :param number: 获取url的个数，默认None表示全部获取
        :return: 返回商品对应的url列表（可赋值给crawl_comment用于获取商品对应的评论）
        '''
```
## 爬取的商品信息存储格式如下：<br>
1.商品信息：直接存储在txt文本中
![](https://i.imgur.com/Q181AfO.jpg)
<br>
2.评论信息：按名称分类存储在评论文件夹内
![](https://i.imgur.com/9KnGBb6.jpg)

