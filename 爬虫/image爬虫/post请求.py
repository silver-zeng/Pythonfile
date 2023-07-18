# 360翻译
import requests

url = 'https://fanyi.so.com/index/search'


data_dict ={
    'eng': '0',
    'validate': '',
    'ignore_trans': '0',
    'query': '美国',
}
headers = {
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Pro':'fanyi',
}

res = requests.post(url, params=data_dict, headers=headers)
print(res.json().get("data").get("fanyi"))
