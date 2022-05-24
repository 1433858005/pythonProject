import re

from bs4 import BeautifulSoup

file = open("1.html", "rb")
html = file.read().decode("utf-8")
bs = BeautifulSoup(html, "html.parser")

# 1.Tag 标签及其内容：拿到它所找到的第一个内容
# 2.NavigableString 标签里的内容（字符串）
# 3.BeautifulSoup  表示整个文档
# 4.Comment 是一个特殊的NavaigableString 输出的内容不包含注释符号
# 标签里的元素
# print(bs.head.style)
# 标签里的内容
# print(bs.head.style.string)
# 标签里的属性
# print(bs.div.attrs)
# 文档的遍历
# print(bs.head.contents[7])
# print(bs.head.contents)
# 文档搜索
# 字符串过滤
# list=bs.find_all("div")
# print(list)
# 正则表达式搜索
# 把网页中包含a的都给找出来
# lis = bs.find_all(re.compile("a"))
# print(lis)
# 方法：传入一个函数（方法），根据函数的要求来搜索
# 把含有name属性的元素打印出来
# def name(tag):
#     return tag.has_attr("id")
#
# lis = bs.find_all(name)
# # print(lis)
# for i in lis:
#     print(i)
# 2.kwargs 参数 66666
# div = "class"
# lis = bs.find_all(class_="div1")
#
# for i in lis:
#     print(i)
# 3.text参数
# 把含有数字的打印出来re.compile("\d")
# limit 参数 限定要几个参数
# lis = bs.find_all(text=re.compile("\d"),limit=3)
# for i in lis:
#     print(i)

# 选择器
# 获取class=div2的内容
# lis = bs.select(".div2")
lis = bs.select("div[class='div1']")
for i in lis:
    print(i)