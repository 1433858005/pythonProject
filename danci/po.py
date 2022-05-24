# 获取一个post请求
import urllib.parse
import urllib.request
if __name__ == "__main__":

    data = bytes(urllib.parse.urlencode({"username":"中考单词_copy1,未,额"}),encoding="utf-8")
    response = urllib.request.urlopen("https://qpanpan.com/engs/b", data=data)
    print(response.read().decode('utf-8'))

    # import urllib.parse
    # data = bytes(urllib.parse.urlencode({"qqq": "6666"}), encoding="utf-8")
    # response = urllib.request.urlopen("http://httpbin.org/post", data=data)
    # print(response.read().decode('utf-8'))
