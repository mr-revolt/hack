from lxml import etree
html = '''
    <div id="a">
    left
        <span id="b">
        right
            <ul>
            up
                <li>down</li>
            </ul>
        east
        </span>
        west
    </div>
'''
selector = etree.HTML(html)
content = selector.xpath('//div[@id="a"]/text()')
print(content) # ['\n    left\n        ', '\n        west\n    ']

data = selector.xpath('//div[@id="a"]')[0]
info = data.xpath('string(.)')
content = info.replace('\n','').replace('','')
print(content)
