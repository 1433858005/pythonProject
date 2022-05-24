# import bs4
from urllib import response

from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3


def main():
    baseurl = "https://movie.douban.com/top250?start="
    # 1.爬取网页
    datalist = getDate(baseurl)
    # savepath = ".\\豆瓣电影.xls"
    # 保存数据
    # saveData(savepath)


# 创建正则表达式，表示规则（字符串） 获取链接地址
# re.S 让换行符包含在字符中
findLink = re.compile(r'<a href="(.*?)">')
findImgSrc = re.compile(r'<img.*src="(.*?)"', re.S)
findTitle = re.compile(r'<span class="title">(.*?)</span>', re.S)


# 爬取网页
def getDate(baseurl):
    datalist = []
    # 调用获取页面信息10页
    for i in range(0, 1):
        url = baseurl + str(i * 25)
        # 保存获取到的网页源码
        html = askURL(url)
        # 2.逐一解析数据
        soup = BeautifulSoup(html, "html.parser")
        for j in soup.find_all("div", class_="item"):
            # print(j)  # 测试电影item全部信息
            data = []  # 保存一部电影信息
            j = str(j)
            # 找到第一个符合正则表达式的链接
            # 获取影片链接
            # replace("要替换的内容","替换的内容")
            link = re.findall(findLink, j)[0]
            data.append(link)
            img = re.findall(findImgSrc, j)[0]
            data.append(img)
            name = re.findall(findTitle, j)[0]
            data.append(name)
            datalist.append(data)
    print(datalist)
    return datalist


# 保存数据
def saveData(savepath):
    print("5555")


# 得到一个网页内容
def askURL(url):
    # 用户代理。表示告诉豆瓣服务器我们是什么类型的浏览器
    # 模拟头部
    head = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53"
    }
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        # print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)
    return html


if __name__ == "__main__":
    main()
