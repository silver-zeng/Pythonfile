import requests
words = input("请输入要翻译的中文：")
header ={
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36',
    'Referer': 'https://www.youdao.com/',
    'Host': 'dict.youdao.com',
    'Origin': 'https://www.youdao.com',
    'Pragma': 'no-cache',
    'Accept': 'application/json, text/plain, */*'
}
url = f'https://dict.youdao.com/suggest?num=5&ver=3.0&doctype=json&cache=false&le=en&q={words}'
res = requests.get(url,headers=header)
trans_res = res.json()['data']['entries'][0]['explain']
print(trans_res)