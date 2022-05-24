#https://web. shanbay.com/web/account/login/
from selenium import webdriver
import time
from selenium.webdriver.common.by import By
# from PW.mm import USER, PASSWORD
if __name__ == "__main__":
    driver_url = r"C:\Users\Administrator\PycharmProjects\pythonProject\venv\Scripts\MicrosoftWebDriver.exe"
    driver = webdriver.Edge(executable_path=driver_url)
    # d.get("https://web.shanbay.com/web/account/login/")
    # driver=webdriver.Chrome ()
    driver.implicitly_wait(10)#隐式等待,最长10s
    url = 'https://web.shanbay.com/web/account/login/'
    driver.get(url)
    driver.maximize_window()#窗口最大化time.sleep (2)#输入账号
    driver. find_element (By. ID, 'input-account'). send_keys ('18628699912')#输入密码
    driver. find_element(By. ID, 'input-password'). send_keys ('+Jp15149622693')
    driver. find_element(By.CSS_SELECTOR, '#button-login').click()
    time.sleep (1)
