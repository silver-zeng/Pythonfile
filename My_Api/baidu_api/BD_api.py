
# encoding:utf-8

import requests
import base64
import json

# 获取鉴权码
client_id = 'LBXbYmW9iqaB7HjMUcs1MDUe'   # 百度账号中应用的api key
lient_secret = 'VvvOCEAuOLCaipPeGcmQoKBAdWukmZGs'  # 百度账号中应用的Secret Key
def main():
    url = f"https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id={client_id}&client_secret={lient_secret}"

    payload = ""
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json'
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    access_token = response.json().get("access_token")
    print(response.json().get("access_token"))
    return access_token

'''
通用文字识别（高精度版）
'''
def accurate_basic():
    request_url = "https://aip.baidubce.com/rest/2.0/ocr/v1/accurate_basic"
    # 二进制方式打开图片文件
    f = open('a.jpg', 'rb')
    img = base64.b64encode(f.read())

    params = {"image":img}
    # 调用鉴权接口获取的token
    access_token = main()
    request_url = request_url + "?access_token=" + access_token
    headers = {'content-type': 'application/x-www-form-urlencoded'}
    response = requests.post(request_url, data=params, headers=headers)
    if response:
        print (response.json())


if __name__ == '__main__':
    accurate_basic()

