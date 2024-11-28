from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains  # 导入动作链
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait  # 显示等待  WebDriverWait(driver,timeout,poll_frequency=0.5,ignored_exceptions=None).until(EC.presence_of_element_located(元素xpath),message="报错信息")
from selenium.webdriver.common.keys import Keys # 处理键盘事件的类
from selenium.webdriver.support import expected_conditions as EC   #显示等待条件
from random import randint  # 导入随机函数
import pandas as pd # 解析excel
import time
from datetime import datetime
import os

class CoalSettlement():
    timenow = datetime.now().strftime("%Y%m%d%H%M%S")
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://test.yiscs.cn/general/login")
        self.driver.maximize_window()  # 最大化窗口
        time.sleep(randint(1, 3))

    def login(self, username, password):
        user = self.driver.find_element(By.XPATH, "//input[@placeholder='用户名']")
        pwd = self.driver.find_element(By.XPATH, "//input[@placeholder='密码']")
        tuling = self.driver.find_element(By.XPATH, "//input[@placeholder='验证码']")
        LoginButton = self.driver.find_element(By.XPATH, "//*[@id='app']/div/form/div/button/span")
        user.send_keys(username)
        pwd.send_keys(password)
        tuling.send_keys('666888')
        LoginButton.click()
        time.sleep(1)
    # 截图保存
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

    # 结算数据文件解析
    def open_file(file_path):
        data = pd.read_excel(file_path)
        print(data['项目编号'].values[0], data['结算单编号'].values[0])
        return data
    def create_settlement(self):
        data = CoalSettlement.open_file(file_path="../煤炭结算自动化数据.xlsx")
        CoalSettlement.login(self, username='admin', password='qwe123')
        time.sleep(5)
        # wd是webdriver对象，20是最长等待时间，0.5是每0.5秒去查询对应的元素。until后面跟的等待具体条件，EC是判断条件，检查元素是否存在于页面的 DOM 上。
        jsgl_xpath = (By.XPATH, "//div[@class='el-submenu__title']/span[text()='结算管理']")
        WebDriverWait(self.driver, 20, 0.5).until(EC.presence_of_element_located(jsgl_xpath), message="结算管理元素没有定位到")
        # 点击结算管理展开页签
        self.driver.find_element(By.XPATH, "//div[@class='el-submenu__title']/span[text()='结算管理']").click()
        time.sleep(2)
        # 点击结算管理-煤炭结算
        self.driver.find_element(By.XPATH, "//div[@class='el-submenu__title']/span[text()='煤炭结算']").click()
        time.sleep(2)
        # 点击结算管理-煤炭结算-收付款核销
        self.driver.find_element(By.XPATH, "//div[@class='nest-menu']/a/li/span[text()='收付款核销']").click()
        time.sleep(3)
        # 点击批量核销按钮
        self.driver.find_element(By.XPATH, "//button/span[text()=' 批量核销 ']").click()
        time.sleep(3)
        # 批量核销截图
        CoalSettlement.makedir_current_save_image(self, f"点击批量核销{CoalSettlement.timenow}.png")
        time.sleep(2)
        self.driver.find_element(By.XPATH, "//div/input[@placeholder='查找项目']").click()
        time.sleep(2)
        # 输入查询项目编号
        ProjectNo = data['项目编号'].values[0]
        self.driver.find_element(By.XPATH, "//div/input[@placeholder='项目']").send_keys(ProjectNo)
        time.sleep(4)
        try:
            # 定位项目输入框，输入项目编号，选择项目
            ProjectElement = self.driver.find_element(By.XPATH, f"//tbody/tr[1]/td[1]/div/span/span[text()=' "+f"{ProjectNo}" + " ']")
            if ProjectElement:
                self.driver.find_element(By.XPATH, "//tbody/tr[1]/td[5]/div/button/span[text()='选择']").click()
                time.sleep(2)
                CoalSettlement.makedir_current_save_image(self, f"批量核销选择项目{CoalSettlement.timenow}.png")  # 保存截图
        except NoSuchElementException as e:
            print(f"项目编号不存在,未定位到元素{e}")
        # 显式等待
        # 结算单搜索按钮触发元素xpath
        Settlement_search_xpath = "//div/span[@class='el-input__suffix']/span[@class='el-input__suffix-inner']/i[@class='el-icon-search cursor-pointer']"
        WebDriverWait(self.driver, 10, 0.5).until(EC.presence_of_element_located((By.XPATH, Settlement_search_xpath)))
        self.driver.find_element(By.XPATH, Settlement_search_xpath).click()
        time.sleep(2)
        SettlementNo = data['结算单编号'].values[0]
        self.driver.find_element(By.XPATH, "//div[@class='el-input el-input--medium']/input[@placeholder='云星空结算单']").send_keys(SettlementNo)
        try:
            # 定位云星空结算单编号输入框，输入结算单编号，选择结算单
            SettlementElement = WebDriverWait(self.driver, 10, 0.5).until(
                EC.presence_of_element_located((By.XPATH, f"//tbody/tr[1]/td[1]/div/span/span[text()=' "+f"{SettlementNo}" + " ']")))
            # SettlementElement = self.driver.find_element(By.XPATH, f"//tbody/tr[1]/td[1]/div/span/span[text()=' "+f"{SettlementNo}" + " ']")
            if SettlementElement:
                # 创建 ActionChains 对象
                actions = ActionChains(self.driver)
                actions.double_click(SettlementElement).perform()
            time.sleep(2)
            # 保存截图
            CoalSettlement.makedir_current_save_image(self, f"选择金蝶结算单{CoalSettlement.timenow}.png")
        except NoSuchElementException as e:
            print(f"云星空结算单编号不存在,未定位到元素{e}")


CoalSettlement().create_settlement()