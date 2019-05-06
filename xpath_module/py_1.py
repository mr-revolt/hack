from lxml import etree

"""
Xpath的使用方法:
- // 对全文进行扫描,在文档中选取所有符合条件的内容,以列表的形式返回.
- / 寻找当前标签路径的下一层路径标签,或对当前层标签的内容进行操作
- /text() 获取当前路径下的文本内容
- /@xxx 提取当前路径下标签的属性值
- | 可选值,使用 | 可以选取若干个路径,如 //p|//div 即在当前路径下选取所有符合条件的p标签和div标签
- . 用来选取当前节点
- .. 选取当前节点的父亲节点
"""

html="""
<!DOCTYPE html>
<html>
<head lang="en">
<title>测试</title>
<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
</head>
<body>
<div id="content">
<ul id="ul">
<li>NO.1</li>
<li>NO.2</li>
<li>NO.3</li>
</ul>
<ul id="ul2">
<li>one</li>
<li>two</li>
</ul>
</div>
<div id="url">
<a href="http:www.58.com" title="58">58</a>
<a href="http:www.csdn.net" title="CSDN">CSDN</a>
</div>
</body>
</html>
"""
# TODO:将源码转化为能被XPath匹配的格式
selector = etree.HTML(html)
content=selector.xpath('//div[@id="content"]/ul[@id="ul"]/li/text()')
link = selector.xpath('//a/@href')
abs_title = selector.xpath('/html/body/div/a/@title')
print(content,link,abs_title)