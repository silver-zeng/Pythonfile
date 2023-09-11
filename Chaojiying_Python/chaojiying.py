#!/usr/bin/env python
# coding:utf-8

import requests
from hashlib import md5
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

class Chaojiying_Client(object):

    def __init__(self, username, password, soft_id):
        self.username = username
        password =  password.encode('utf8')
        self.password = md5(password).hexdigest()
        self.soft_id = soft_id
        self.base_params = {
            'user': self.username,
            'pass2': self.password,
            'softid': self.soft_id,
        }
        self.headers = {
            'Connection': 'Keep-Alive',
            'User-Agent': 'Mozilla/4.0 (compatible; MSIE 8.0; Windows NT 5.1; Trident/4.0)',
        }

    def PostPic(self, im, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
        }
        params.update(self.base_params)
        files = {'userfile': ('ccc.jpg', im)}
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, files=files, headers=self.headers)
        return r.json()

    def PostPic_base64(self, base64_str, codetype):
        """
        im: 图片字节
        codetype: 题目类型 参考 http://www.chaojiying.com/price.html
        """
        params = {
            'codetype': codetype,
            'file_base64':base64_str
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/Processing.php', data=params, headers=self.headers)
        return r.json()

    def ReportError(self, im_id):
        """
        im_id:报错题目的图片ID
        """
        params = {
            'id': im_id,
        }
        params.update(self.base_params)
        r = requests.post('http://upload.chaojiying.net/Upload/ReportError.php', data=params, headers=self.headers)
        return r.json()

    #  自定义方法————————————————点触验证码方法,返回坐标index，xpath为验证码图片对象
    def img_click(self, xpath, index):
        img_element = driver.find_element(By.XPATH,xpath)
        for i in index:
            data = i.split(",")
            x = int(data[0])
            y = int(data[1])
            # 执行动作链，move_to_element_with_offset（对象【参照物】，点击的坐标）
            ActionChains(driver).move_to_element_with_offset(img_element, x, y).click().perform()

if __name__ == '__main__':
    chaojiying = Chaojiying_Client('silver', 'zengfanyu1314', '96001')	#用户中心>>软件ID 生成一个替换 96001
    im = open('a.jpg', 'rb').read()													#本地图片文件路径 来替换 a.jpg 有时WIN系统须要//
    print(chaojiying.PostPic(im, 1902))										#1902 验证码类型  官方网站>>价格体系 3.4+版 print 后要加()
    #print chaojiying.PostPic(base64_str, 1902)  #此处为传入 base64代码
