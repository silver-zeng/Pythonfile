import requests,csv
import time
from tqdm import tqdm
url = 'https://crm.zhaomei.com/crm/zmpriceindex/list-hisotry-app?pkValue=0&rows=200&startTime=2023-01-31&endTime=2023-09-26'
heard = {
    'Referer': 'https://www.zhaomei.com/',
    'Content-Type': 'application/x-www-form-urlencoded;charset=utf-8',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36'
}
res = requests.get(url, headers=heard)
res_list = res.json()['body']
csv_head = ['数据更新时间', '4500k动力煤价格', '4500k涨幅', '5000k动力煤价格', '5000k涨幅', '5500k动力煤价格',
            '5500k涨幅']
with open('./找煤网动力煤111111.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(csv_head)
    lines = range(200)
    for i in res_list:
        updatedTime = i.get('updatedTime')
        m1Price = i.get('m1Price')  # 4500K 煤炭价格
        m1Wave = i.get('m1Wave')  # 4500K 煤炭涨幅
        m2Price = i.get('m2Price')  # 5000K
        m2Wave = i.get('m2Wave')
        m3Price = i.get('m3Price')  # 5500K
        m3Wave = i.get('m3Wave')
        data = [updatedTime, m1Price, m1Wave, m2Price, m2Wave, m3Price, m3Wave]
        writer.writerow(data)
       # 添加进度条
    for t in tqdm(lines):
        time.sleep(0.1)
