from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains # 动作链
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()
driver.get('https://www.example.com')

# 找到目标元素
target_element = driver.find_element(by=By.XPATH,value='element_id')

# 创建ActionChains对象
actions = ActionChains(driver)

# 将鼠标指针移动到目标元素的指定偏移量位置
actions.move_to_element_with_offset(target_element, 100, 200)

# 单击鼠标
actions.click()

# 执行操作
actions.perform()
# 点触验证码
def img_click(xpath, index_list):
    img_element = driver.find_element(By.XPATH,xpath)
    for i in index_list:
        data = i.split(",")
        x = int(data[0])
        y = int(data[1])
        # 执行动作链，move_to_element_with_offset（对象【参照物】，点击的坐标）
        ActionChains(driver).move_to_element_with_offset(img_element, x, y).click().perform()

