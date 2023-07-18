import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


wb = webdriver.Chrome()
wb.maximize_window() # 全屏的意思
wb.get("https://test.yiscs.cn/index")
wb.find_element(by=By.CLASS_NAME, value='justify-center').click()
wb.find_element(by=By.XPATH, value='//input[@placeholder="请输入手机号"]').send_keys("18707994417")
wb.find_element(by=By.XPATH, value='//input[@placeholder="请输入验证码"]').send_keys("1")
wb.find_element(by=By.CLASS_NAME, value='el-button').click()
time.sleep(1)
wb.find_element(by=By.XPATH, value='//div[text()=" 产品中心 "]').click()
time.sleep(3)
wb.find_element(by=By.XPATH, value='//div/span[text()=" 煤炭业务 "]').click()
wb.find_elements(by=By.XPATH, value='//button/span[text()="立即申请"]')[0].click()
time.sleep(2)
wb.find_element(by=By.XPATH, value='//*[@id="app"]/div/div/section/div/div[1]/div/div[2]/div[2]/form/div[2]/div[1]/div/div/div[1]/input').send_keys("一个人的寂寞")
wb.find_element(by=By.XPATH, value='//*[@id="app"]/div/div/section/div/div[1]/div/div[2]/div[2]/form/div[2]/div[2]/div/div/div/div[1]/div[1]/input').send_keys("两个人的错")
wb.find_element(by=By.XPATH, value='//*[@id="app"]/div/div/section/div/div[1]/div/div[2]/div[2]/form/div[2]/div[3]/div/div/div[1]/input').send_keys("120")
wb.find_element(by=By.XPATH, value='//*[@id="app"]/div/div/section/div/div[1]/div/div[2]/div[2]/form/div[2]/div[4]/div/div/div/div/input').send_keys("汽车-直达")
wb.find_element(by=By.XPATH, value='//*[@id="app"]/div/div/section/div/div[1]/div/div[2]/div[2]/form/div[2]/div[4]/div/div/div/div/span/span/i').click()
# 选择交货方式
time.sleep(1)
wb.find_element(by=By.XPATH, value='/html/body/div[3]/div[1]/div[1]/ul/li[1]').click()
time.sleep(5)

