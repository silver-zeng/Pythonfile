from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest

# 固定一个driver，避免每次都打开浏览器
@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.get("https://test.yiscs.cn/general/login")
    driver.maximize_window()
    yield driver
    driver.quit()


def test_button_click(driver):
    wait = WebDriverWait(driver, 10)

    # 等待用户名输入框出现
    username_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='用户名']")))
    username_input.send_keys('zengfanyu')

    # 等待密码输入框出现
    password_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@placeholder='密码']")))
    password_input.send_keys('qwe123')

    # 等待登录按钮出现
    button = wait.until(EC.element_to_be_clickable((By.XPATH, "//button/span/span[text()='登 录']")))
    button.click()

    # 等待一段时间以观察结果
    time.sleep(3)


if __name__ == "__main__":
    try:
        pytest.main(["-k", "test_button_click"])
    finally:
        pass
