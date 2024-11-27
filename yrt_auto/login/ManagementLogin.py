from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  # 显示等待  WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None).until(EC.presence_of_element_located(元素xpath),message="报错信息")
from selenium.webdriver.common.keys import Keys # 处理键盘事件的类
from selenium.webdriver.support import expected_conditions as EC   #显示等待条件
from random import randint  # 导入随机函数
import time
from datetime import datetime
import os
from Chaojiying_Python.chaojiying import Chaojiying_Client

class Login():
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://test.yiscs.cn/general/login")
        time.sleep(randint(1, 3))
    def makedir_current_save_image(self,image_name):
        # 获取当前日期，并格式化为字符串（例如：2023-04-01）
        current_date = datetime.now().strftime("%Y-%m-%d")
        # 构建目标目录路径
        directory_path = "../TestImage/" + current_date
        if not os.path.exists(directory_path):
            os.mkdir(directory_path)
        # 构建截图文件的完整路径
        screenshot_path = os.path.join(directory_path, image_name)
        # 保存截图到指定路径
        self.driver.save_screenshot(screenshot_path)

    def login(self, username, password):

        user = self.driver.find_element(By.XPATH, "//input[@placeholder='用户名']")
        pwd = self.driver.find_element(By.XPATH, "//input[@placeholder='密码']")
        tuling = self.driver.find_element(By.XPATH, "//input[@placeholder='验证码']")
        LoginButton = self.driver.find_element(By.XPATH, "//*[@id='app']/div/form/div/button/span")
        user.send_keys(username)
        pwd.send_keys(password)
        tuling.send_keys('666888')
        LoginButton.click()
        time.sleep(3)
        Login.makedir_current_save_image(self, "login_screenshot.png")
        # driver.save_screenshot("../TestImage/screenshot.png")  # 保存整个网页的截图

Login().login("zengfanyu", "qwe123")
