import threading
import time
import urllib.parse
import urllib.request

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By


def mainmm():
    global urllib
    aa = []
    for i in range(int(aq)):
        time.sleep(0.2)
        try:
            for j in range(10):
                a = d.find_elements_by_class_name("index_wordName__1lkbV")[j].text
                b = d.find_elements_by_class_name("index_bottom__XLoPQ")[j].text
                data = bytes(urllib.parse.urlencode({"username": "中考," + a + "," + b}), encoding="utf-8")
                response = urllib.request.urlopen("http://localhost:8080//b", data=data)
                print(response.read().decode('utf-8'))
                time.sleep(0.1)
            time.sleep(0.1)
            print(aa)
            aa.clear()
            d.execute_script(xia)
        except:
            print(45)
            # print(i)


if __name__ == "__main__":
    driver_url = r"C:\Users\Administrator\PycharmProjects\pythonProject\venv\Scripts\MicrosoftWebDriver.exe"
    d = webdriver.Edge(executable_path=driver_url)
    d.get("https://web.shanbay.com/web/account/login/")
    # d.maximize_window()
    script = "Object.defineProperty(navigator,'webdriver',{get: ()=> false,});"
    # 执行js代码
    time.sleep(1)
    d.execute_script(script)
    d.execute_script(
        'var a=document.querySelector("#input-account");const evt=new Event("input");a.value="18628699912";a.dispatchEvent(evt);var b=document.querySelector("#input-password");b.value="+Jp15149622693";b.dispatchEvent(evt);document.querySelector("#button-login").click();')
    time.sleep(1)
    d.find_element_by_id("button-login").click()
    time.sleep(1)
    try:
        slider = d.find_element_by_id("nc_1__bg")
        ActionChains(d).click_and_hold(on_element=slider).perform()
        ActionChains(d).move_by_offset(xoffset=258, yoffset=0).perform()
        ActionChains(d).pause(0.5).release().perform()
        time.sleep(2)
        d.find_element_by_id("button-login").click()
    except:
        print("失败")
    time.sleep(1)
    d.find_element_by_class_name("task-name").click()
    time.sleep(1)
    d.find_element_by_class_name("index_vocabularyLink__1c7FY").click()
    time.sleep(1)
    d.find_elements_by_class_name("index_navItemContent__mA21b")[3].click()
    time.sleep(1)
    p = input('请输入密码:')
    # 总页数
    aq = d.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div[2]/div[2]/div[11]/div/ul/li[8]').text
    # 下一页
    xia = 'document.querySelectorAll(".index_pageContainer__2l7E1")[0].children[document.querySelectorAll(".index_pageContainer__2l7E1")[0].children.length-1].click()'
    t1 = threading.Thread(target=mainmm)
    mainmm()

