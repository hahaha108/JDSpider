import requests
import lxml.etree
import lxml
import re

url = "https://item.jd.com/3035554.html"

response = requests.get(url)

html = lxml.etree.HTML(response.text)

infolist = html.xpath("//*[@id=\"detail\"]/div[2]/div//dl")

name = html.xpath("//div[@class='item ellipsis']/text()")[0]

print("商品名称：",name)

try:
    baozhuang = html.xpath("//div[@class='package-list']/p/text()")[0]
except:
    baozhuang = "未列明"
print("包装清单：",baozhuang)


# jieshao = html.xpath("//div[@class='item hide']/text()")[0]
# print("商品简介：",jieshao)


number = re.findall(r"com/(\d+)\.html",url)[0]
# print(number)

ajaxUrl = r"https://p.3.cn/prices/mgets?callback=jQuery6296303&type=1&area=1_72_4137_0&pdtk=&pduid=15103642583881863116775&pdpin=&pin=null&pdbp=0&skuIds=J_" + number + r"&ext=11000000&source=item-pc"

ajaxResponse = requests.get(ajaxUrl)
# print(ajaxResponse.text)
prices = re.findall('"p":"(.*?)"',ajaxResponse.text)[0]
print("价格：",prices)

for info in infolist:
    titles = info.xpath("./dt/text()")
    contents = info.xpath("./dd/text()")
    for title,content in zip(titles,contents):
        print(title,':',content)
