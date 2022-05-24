# import bs4
from urllib import response

import requests
from bs4 import BeautifulSoup
import re
import urllib.request, urllib.error
import xlwt
import sqlite3


def a():
    print(66)
    data = {"account": "18628699912", "password": "+Jp15149622693", "code_2fa": ""}
    head = {
        "user-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.64 Safari/537.36 Edg/101.0.1210.53',
        # "cookie": '_ga=GA1.2.1400652002.1652930294; study_order_tip=known; auth_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjM3NjY0NzYwLCJleHAiOjE2NTQwNzY5MDEsImV4cF92MiI6MTY1NDA3NjkwMSwiZGV2aWNlIjoiIiwidXNlcm5hbWUiOiJQaG9uZV85ZTMyMDJhYjdiN2JmMmE2IiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiI2YjgwZTUyOGQ3MjIxMWVjYTFkOTVhMTY2ZmY0MWM5NSJ9.RzN4w90PPyvWMcANAA1aQjwgnt2MsHX-igA1_q2tPEI; csrftoken=1fc90f08dfd55a2caeb6cec6a2ee84b1; _gat=1; sensorsdata2015jssdkcross={"distinct_id":"dioxmp","first_id":"180da52b02cb46-0c8000b2573dda-4c647e56-2073600-180da52b02dd2b","props":{"$latest_traffic_source_type":"引荐流量","$latest_search_keyword":"未取到值","$latest_referrer":"http://127.0.0.1:5500/"},"$device_id":"180da52b02cb46-0c8000b2573dda-4c647e56-2073600-180da52b02dd2b"}'
        # "cookie": '_ga=GA1.2.1400652002.1652930294; study_order_tip=known; sensorsdata2015jssdkcross={"distinct_id":"dioxmp","first_id":"180da52b02cb46-0c8000b2573dda-4c647e56-2073600-180da52b02dd2b","props":{"$latest_traffic_source_type":"直接流量","$latest_search_keyword":"未取到值_直接打开","$latest_referrer":""},"$device_id":"180da52b02cb46-0c8000b2573dda-4c647e56-2073600-180da52b02dd2b"}; auth_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6MjM3NjY0NzYwLCJleHAiOjE2NTQwNzY5MDEsImV4cF92MiI6MTY1NDA3NjkwMSwiZGV2aWNlIjoiIiwidXNlcm5hbWUiOiJQaG9uZV85ZTMyMDJhYjdiN2JmMmE2IiwiaXNfc3RhZmYiOjAsInNlc3Npb25faWQiOiI2YjgwZTUyOGQ3MjIxMWVjYTFkOTVhMTY2ZmY0MWM5NSJ9.RzN4w90PPyvWMcANAA1aQjwgnt2MsHX-igA1_q2tPEI; csrftoken=1fc90f08dfd55a2caeb6cec6a2ee84b1; _gat=1'
    }
    url = "https://apiv3.shanbay.com/bayuser/login"
    # request = urllib.request.Request(url, headers=head, data=data)
    request = urllib.request.Request(url, headers=head)
    html = ""
    try:
        response = urllib.request.urlopen(request)
        html = response.read().decode("utf-8")
        print(html)
    except urllib.error.URLError as e:
        if hasattr(e, "code"):
            print(e.code)
        if hasattr(e, "reason"):
            print(e.reason)


def b():
    import urllib.parse
    data = bytes(urllib.parse.urlencode({"account": "18628699912", "password": "+Jp15149622693", "code_2fa": ""}),
                 encoding="utf-8")
    response = urllib.request.urlopen("https://apiv3.shanbay.com/bayuser/login", data=data)
    print(response.read().decode('utf-8'))
    import urllib.request


def c():
    import requests
    session = requests.session()
    # data = {"account": "18628699912", "password": "+Jp15149622693", "code_2fa": ""}
    data = {"account": "18628699912", "password": "+Jp15149622693"}
    url = "https://apiv3.shanbay.com/bayuser/login"
    resp2 = session.OPTIONS(url)
    # resp = session.post(url, data=data)
    print(resp2)


if __name__ == "__main__":
    c()
