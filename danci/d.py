#https://web.shanbay.com/web/account/login/
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from danci.mm import USER, PASSWORD
from selenium.webdriver import ActionChains
if __name__ == '__main__':
    driver_url = r"C:\Users\Administrator\PycharmProjects\pythonProject\venv\Scripts\MicrosoftWebDriver.exe"
    driver= webdriver.Edge(executable_path=driver_url)
    # driver=webdriver.Chrome()
    # 反屏蔽
    driver.execute_cdp_cmd('Page.addScriptToEvaluateOnNewDocument', {
        'source': 'Object.defineProperty(navigator, "webdriver", {get: () => undefined})'
    })
    driver.implicitly_wait(10) #隐式等待，最长10s
    url = 'https://web.shanbay.com/web/account/login/'
    driver.get(url)
    # driver.maximize_window()#窗口最大化
    # time.sleep(2)
    # 输入账号
    driver.find_element(By.ID,'input-account').send_keys(USER)
    #输入密码
    driver.find_element(By.ID,'input-password').send_keys(PASSWORD)
    driver.find_element(By.ID, 'button-login').click()
    time.sleep(2)
    errors=driver.find_elements(By.CLASS_NAME,'error-msg')
    print(errors[0].text)
    if errors:
        if '请进行二次验证' in errors[0].text:
            def slidermove():
                # 获取滑块位置
                slider = driver.find_element_by_css_selector('#nc_1_n1z')
                # 获取滑条
                Slidebar = driver.find_element_by_css_selector("#nc_1__scale_text > span")
                # 拖动滑块滑条末尾
                ActionChains(driver).drag_and_drop_by_offset(slider, Slidebar.size['width'],-slider.size['height']).perform()
            slidermove()
        elif '验证失败，请重试～'in errors[0].text:
            driver.find_element(By.ID, 'button-login').click()







