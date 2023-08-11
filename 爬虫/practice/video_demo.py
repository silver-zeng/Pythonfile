import requests
from lxml import etree
import csv

url = r'http://www.piaofang.biz'
# 发请求，获取响应
res = requests.get(url)
# 获取响应内容
res_enconded = res.content.decode('GB2312')
# etree 对象
etree_html = etree.HTML(res_enconded)
# print(res_enconded)
video_name_list = etree_html.xpath('//tr')
print(video_name_list)
list=[]
for tr in video_name_list:
    dic = {}
    movie_name = tr.xpath('.//td[@class="title"]/text()')
    if movie_name == ['《', '》']:
        dic["movie_name"] = tr.xpath('.//td[@class="title"]/a/text()')[0]
    elif movie_name == []:
        pass
    else:
        dic["movie_name"] = movie_name[0]
    piaofang = tr.xpath('.//td[@class="piaofang"]/span/text()')
    if not piaofang == []:
        dic["piaofang"] = piaofang[0]
        list.append(dic)

    print(list)

heads = ('movie_name', 'piaofang')
with open('movie.csv', 'w', encoding='utf-8-sig', newline='') as f:
    # 1.创建csv写入对象
    w = csv.DictWriter(f, fieldnames=heads)
    # 2. 写入表头
    w.writeheader()
    # 3. 一次性写入多行数据
    w.writerows(list)
