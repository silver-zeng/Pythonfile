import time
from appium import webdriver
from appium.webdriver.extensions.android.nativekey import AndroidKey
from selenium.webdriver.common.by import By

desired_caps={
    'platformName': 'Android',   # 手机系统类型
    'platformVersion': '7.1.2',  # 操作系统版本号
    "deviceName": "samsung",   # 设备名
    'appPackage': 'tv.danmaku.bili',   # 包名   包名及入口，在运行app时，使用 dumpsys activity | grep "mFocusedActivity" 查看
    'appActivity': 'MainActivityV2',  # 入口
    'unicodeKeyboard': True,   # 使用自带输入法
    'resetKeyboard': True,
    'noReset': True,   # 操作完后要不要关闭重置app,如果要重置，那么设置为False
    "automationName": "UiAutomator2"
}
# 连接Appium-Server，初始化自动化环境·建立连接-根据参数建立连接安装
driver = webdriver.Remote("http://localhost:4723/wd/hub", desired_caps)
# 隐式等待
driver.implicitly_wait(15)
# 点击同意并继续
driver.find_element(By.ID, "tv.danmaku.bili:id/agree").click()
time.sleep(2)
driver.find_element(By.ID, "tv.danmaku.bili:id/expand_search").send_keys("跳舞视频")
time.sleep(2)
# 按下回车键
driver.press_keycode(AndroidKey.ENTER)
