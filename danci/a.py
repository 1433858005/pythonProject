import threading
import time

from selenium import webdriver
from selenium.webdriver import ActionChains

def mainmm(p):
    print(p)
    shujuku = '六级'
    global urllib
    aa = []
    for i in range(int(aq)):
        time.sleep(0.2)
        try:
            for j in range(10):
                a = d.find_elements_by_class_name("index_wordName__1lkbV")[j].text
                b = d.find_elements_by_class_name("index_bottom__XLoPQ")[j].text
                if len(b) > 100:
                    b = b[0:100]
                mp = "return document.querySelectorAll('.index_top__1grCv')[" + str(
                    j) + "].children[1]." + p + ".children.props.url"
                c = d.execute_script(mp)
                if c != "":
                    print(c)

                    data = bytes(
                        urllib.parse.urlencode({"username": shujuku + ",panpan" + a + ",panpan" + b + ",panpan" + c}),
                        encoding="utf-8")
                    response = urllib.request.urlopen("http://localhost:8080//nb", data=data)
                    print(response.read().decode('utf-8'))
                    time.sleep(0.1)
                else:
                    print(b + 'mp3有空')
                    c = '没有MP3'
                    data = bytes(
                        urllib.parse.urlencode({"username": shujuku + ",panpan" + a + ",panpan" + b + ",panpan" + c}),
                        encoding="utf-8")
                    response = urllib.request.urlopen("http://localhost:8080//nb", data=data)
                    print(response.read().decode('utf-8'))
                    time.sleep(0.1)
            time.sleep(0.1)
            print(aa)
            aa.clear()
            d.execute_script(xia)
        except:
            print("出现异常")
            # pp = input('是否重新运行')
            # if pp == 1:
            #     mainmm(p)

    mp = "return document.querySelectorAll('.index_top__1grCv')[0].children[1]." + p + ".children.props.url"
    pp = d.execute_script(mp)
    print(pp)


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
    name = 'return Object.keys(document.querySelectorAll(".index_top__1grCv")[0].children[1])[1]'
    q = d.execute_script(name)
    print(q)
    p = input('请输入密码:')
    # 总页数
    aq = d.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div/div[2]/div[2]/div[11]/div/ul/li[8]').text
    # 下一页
    xia = 'document.querySelectorAll(".index_pageContainer__2l7E1")[0].children[document.querySelectorAll(".index_pageContainer__2l7E1")[0].children.length-1].click()'
    t1 = threading.Thread(target=mainmm)
    mainmm(q)
