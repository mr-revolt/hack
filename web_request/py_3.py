import re

import requests, bs4, pprint

res = requests.get('https://so.youku.com/search_video/q_hello')

with open('web_requests.html', 'wb') as fd:
    for chunk in res.iter_content(chunk_size=10000000):
        fd.write(chunk)
    # res.raise_for_status()
# html = res.text
# yk_regex = re.compile(
#     r'<div\sclass="sk-mod">' + '.*?<a.*?data-spm="dtitle"\stitle="(.*?)".*?href="(.*?)">.*?</a>.*?</div>'
#     , re.S)
# result = re.findall(yk_regex, html)
# print(result)
# youku_file = open('web_request.html', 'wb')
# for chunk in res.iter_content(100000):
#     youku_file.write(chunk)
#     pprint.pformat(youku_file)
# youku_file.close()
# 现在我们使用本地文件来进行测试
