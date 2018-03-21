import json

import requests

requset_url = "https://sclub.jd.com/comment/productPageComments.action?productId=4706166&score=0&sortType=5&page=1&pageSize=10"
comment_response_str = requests.get(requset_url).text
response_json = json.loads(comment_response_str)
# print(response_json)
# print(type(response_json))
comments = response_json['comments']
for comment in comments:
    print(comment['creationTime'])
    print(comment['content'])
    print('______________________')


