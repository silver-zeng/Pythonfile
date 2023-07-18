import time

from selenium import webdriver
from selenium.webdriver.common.by import By
from Chaojiying_Python.chaojiying import Chaojiying_Client
from Chaojiying_Python import userinfo
from selenium.webdriver.common.action_chains  import ActionChains

wb = webdriver.Chrome()
wb.get("https://aq.yy.com/")

# 选择iframe
fr = wb.find_element(by=By.XPATH,value='//iframe[@frameborder="0"]')
wb.switch_to.frame(fr)

# 选择登录注册
wb.find_element(by=By.XPATH,value='//a[@class="lnRegister"]').click()

# 切换焦点
wb.switch_to.window(wb.window_handles[1])
print(wb.title)

# 选择iframe
ifr = wb.find_element(by=By.XPATH,value='//iframe[@frameborder="no"]')
wb.switch_to.frame(ifr)

# 数据输入框进行输入
wb.find_element(by=By.XPATH, value='//input[@placeholder="输入你的手机号"]').send_keys("17688888888")
wb.find_element(by=By.XPATH, value='//input[@placeholder="设置你帐号的登录密码"]').send_keys("qwe123456")
wb.find_element(by=By.XPATH, value='//input[@placeholder="再次输入密码"]').send_keys("qwe123456")

time.sleep(2)
#-----------------------------------------------------------

def get_code():
    code_img = 'yy_register.png'
    wb.find_element(by=By.ID, value="interActiveWrap").screenshot(code_img)
    return code_img

get_code()

time.sleep(2)


# 超级鹰识别
def img_identify(img_path):
    chaojiying = Chaojiying_Client(username=userinfo.user, password=userinfo.password,
                                   soft_id='931146')  # 用户中心>>软件ID 生成一个替换 96001
    im = open(img_path, 'rb').read()  # 本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    resp = chaojiying.PostPic(im, 9103)
    # {'err_no': 0, 'err_str': 'OK', 'pic_id': '2219320570832210076', 'pic_str': '80,110|146,95|222,109', 'md5': '6896edf2ee6d75a59c81b24ce73967f6'}
    # '80,110|146,95|222,109'
    pic_str = resp.get('pic_str')  # '80,110|146,95|222,109'
    pic_list = pic_str.split("|")  # ['80,110','146,95','222,109']
    return pic_list


img_list = img_identify('yy_register.png')

# 点击图片
def img_click(my_list):
    img_element = wb.find_element(by=By.ID, value="interActiveWrap")
    for i in my_list:
        data = i.split(',')  #['80','110']
        x = int(data[0])  # 80
        y = int(data[1])  # 110
        # 将鼠标移动到距某个元素多少距离的位置
        ActionChains(wb).move_to_element_with_offset(img_element, xoffset=x, yoffset=y).click().perform()
        time.sleep(2)
    wb.find_element(by=By.XPATH, value='//span[@class="pw_submit"]').click()

img_click(img_list)


wb.find_element(by=By.XPATH, value='//span[@node-name="JCheck"]').click()
wb.find_element(by=By.XPATH, value='//a[@class="btn_blue_v3"]').click()








