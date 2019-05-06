import requests

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
print(type(res))

print(len(res.text))
print(res.status_code == requests.codes.ok)
print(res.text[:1000])

# 检查Error
# 我们可以改写上面的程序
# raise_for_status() 方法,可以确保程序在下载失败的时候停止.
try:
    res = requests.get('http://inventwithpython.com/page_that_does_not_exit')
    res.raise_for_status()  # 404 client error
except Exception as exc:
    print("There was a problem: %s" % (exc))

# 将下载的文件保存到硬盘
# 通过标准的open()函数和write()方法，可以将web页面保存到硬盘中的一个文件
# 1.必须用“写二进制”模式打开该文件，即向函数传入字符串“wb".作为open()的第二参数.

res = requests.get('http://www.gutenberg.org/cache/epub/1112/pg1112.txt')
res.raise_for_status()
playFile = open('RomeAndJuliet.txt', 'wb')  # 用'wb' 调用open(),以写二进制的方式打开一个新文件.
for chunk in res.iter_content(100000):  # 对response对象的iter)content()方法做循环.
    playFile.write(chunk)  # 在每次迭代中调用write(),将内容写入文件.
playFile.close()
