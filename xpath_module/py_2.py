from lxml import etree

html = '''
<body>
        <div id="aa">aa</div>
        <div id="ab">ab</div>
        <div id="ac">ac</div>
</body>
'''
selector = etree.HTML(html)
# starts-with 解决标签属性值以相同字符串开头的情况
content = selector.xpath('//div[starts-with(@id,"a")]/text()')
print(content)