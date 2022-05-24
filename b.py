import urllib.request
# 获取一个get请求
# try:  except 异常处理
# try:
#   response = urllib.request.urlopen("http://httpbin.org/get",timeout=1)
#   print(response.read().decode('utf-8'))
# except urllib.error.URLError as e:
#     print("233")

# 获取一个post请求
# import urllib.parse
# data = bytes(urllib.parse.urlencode({"qqq":"6666"}),encoding="utf-8")
# response = urllib.request.urlopen("http://httpbin.org/post",data=data)
# print(response.read().decode('utf-8'))
h={
"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53"
}
# req=urllib.request.Request("https://www.douban.com/",headers=h)
req=urllib.request.Request("https://movie.douban.com/top250",headers=h)
response = urllib.request.urlopen(req)
print(response.read().decode('utf-8'))
