from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  # 显示等待  WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None).until(EC.presence_of_element_located(元素xpath),message="报错信息")
from selenium.webdriver.common.keys import Keys # 处理键盘事件的类
from selenium.webdriver.support import expected_conditions as EC   #显示等待条件
from random import randint # 导入随机函数
import time
from Chaojiying_Python.chaojiying import Chaojiying_Client


def chaojiying(imag):
    chaojiying = Chaojiying_Client(username=598725443, password="zengfanyu1314..",soft_id='950569')  # 用户中心>>软件ID 生成一个替换 96001
    im = open(imag, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    resp = chaojiying.PostPic(im, 6001)
    return resp
driver=webdriver.Chrome()
url='https://test.yiscs.cn/general/login?redirect=%2Fapps'
driver.get(url)
time.sleep(1)
username='admin'
passwd='admin321'
driver.find_element(by=By.XPATH,value='//input[@placeholder="用户名"]').send_keys(username)
driver.find_element(by=By.XPATH,value='//input[@placeholder="密码"]').send_keys(passwd)
# 截图保存验证码
code_image=driver.find_element(by=By.XPATH,value="//div/img")
code_image.screenshot("./code.png")
time.sleep(2)
# 输入验证码
# 调用超级鹰识别验证码，返回结果code_result
code_result=chaojiying("D:\Pythonfile\yrt_auto\code.png")
print(code_result)
code_num=code_result.get("pic_str")
driver.find_element(by=By.XPATH,value='//input[@placeholder="验证码"]').send_keys(code_num)  #666888万能验证码
time.sleep(5)
driver.find_element(By.XPATH,"//span[@text()='登录']")
