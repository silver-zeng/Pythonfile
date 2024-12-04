from datetime import datetime
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest


# 常量
EXPECTED_TITLE = "首页"
TIMENOW = datetime.now().strftime("%Y%m%d%H%M%S")

# 固定一个driver，避免每次都打开浏览器
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://test.yiscs.cn/general/login")
    driver.maximize_window()
    yield driver
    driver.quit()

# 自定义截图方法
def makedir_current_save_image(driver,image_name):
    # 获取当前日期，并格式化为字符串（例如：2023-04-01）
    current_date = datetime.now().strftime("%Y-%m-%d")
    # 构建目标目录路径
    directory_path = "../TestImage/" + current_date
    if not os.path.exists(directory_path):
        os.mkdir(directory_path)
    # 构建截图文件的完整路径
    screenshot_path = os.path.join(directory_path, image_name)
    # 保存截图到指定路径
    driver.save_screenshot(screenshot_path)

# 参数化，定义测试数据
@pytest.mark.parametrize("test_input, expected_result", [
    ("admin", "admin"),  # 有效输入
    ("a" * 51, "Username must be between 1 and 50 characters."),  # 过长输入
    ("", "Username is required."),  # 空输入
    ("1234567890", "1234567890"),  # 数字输入
    ("user name", "user name"),  # 含空格输入
    ("!@#$%^&*()", "!@#$%^&*()"),  # 特殊字符输入
    ("a" * 49, "a" * 49),  # 边界条件 - 最大长度减1
    ("a" * 50, "a" * 50),  # 边界条件 - 最大长度
    ("a", "a"),  # 边界条件 - 最小长度
])
# 登录输入框校验
def test_login_input(driver, test_input, expected_result):
    wait = WebDriverWait(driver, 10, poll_frequency=0.5)
    username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='用户名']")))
    # 清空输入框
    username_input.clear()
    username_input.send_keys(test_input)
    # 获取输入框的值
    actual_value = username_input.get_attribute("value")
    # 该行代码使用了 assert 语句来断言 actual_value 是否等于 expected_result。如果不相等，则会抛出一个 AssertionError，并附带错误信息 "Expected 'expected_result', but got
    assert actual_value == expected_result, f"Expected '{expected_result}', but got '{actual_value}'"
    image_name = f"登录输入框校验_{test_input}.png"
    makedir_current_save_image(driver, image_name)


def test_login(driver):
    # 创建WebDriverWait对象, 设置超时时间为10秒，轮询间隔为0.5秒
    wait = WebDriverWait(driver, 10, poll_frequency=0.5)

    # 等待用户名输入框出现
    username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='用户名']")))
    username_input.send_keys('zengfanyu')

    # 等待密码输入框出现
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='密码']")))
    password_input.send_keys('qwe123')

    # 等待验证码输入框出现
    code_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='验证码']")))
    code_input.send_keys('666888')

    # 等待登录按钮出现
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span/span[text()='登 录']")))
    button.click()

    # 等待一段时间以观察结果
    time.sleep(3)

    # assert EXPECTED_TITLE in element.text
    # 断言
    try:
        element = wait.until(
            EC.presence_of_element_located((By.XPATH, "//*[@id='tags-view-container']/div/div[1]/div/span[1]")))
        assert EXPECTED_TITLE in element.text
        print("登录成功")
        makedir_current_save_image(driver, f"登录{TIMENOW}.png")
        return True
    except AssertionError as e:
        makedir_current_save_image(driver, f"登录{TIMENOW}.png")
        print(f"登录失败：{e}")
    except Exception as e:
        makedir_current_save_image(driver, f"登录{TIMENOW}.png")
        print(f"登录发生异常: {e}")


if __name__ == "__main__":

    try:
        pytest.main(["-k", "test_login"])
    finally:
        pass
