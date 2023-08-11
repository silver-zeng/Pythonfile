import requests
# 利用xpath解析
from lxml import etree
import csv
head = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36'
}
lst = []
for page in range(1, 11):
    url = f'https://movie.douban.com/top250?start={(page-1)*25}&filter='
    # 发请求，获取响应
    res = requests.get(url, headers=head)
    # 打印响应  不查看响应内容，直接做解析
    # 解析数据数据最终是以你响应内容为主。不能直接上来解析
    html = res.text
    # 实例化对象
    tree = etree.HTML(html)
    # 数据解析
    divs = tree.xpath('//div[@class="info"]')  # 返回是列表类型的数据。
    # print(len(divs))  # 查看数据的数量  25
    # 具体电影数据的提取
    for div in divs:
        dic = {}
        # 精确提取数据 .当前节点下获取对应的数据
        # 标题  a//text() 获取a标签下的所有文本内容
        title = div.xpath('./div[@class="hd"]/a//text()')
        dic['titles'] = ''.join(title).replace(' ', '').replace('\n', '')
        # 电影类型
        types = div.xpath('./div[@class="bd"]/p/text()')
        dic['types'] = types[1].strip().split('/')[-1]
        # 电影评分
        dic['star'] = div.xpath('./div[@class="bd"]/div[@class="star"]/span[2]/text()')[0]
        # 引言 没有获取到对应的数据，应该是空列表
        quote = div.xpath('./div[@class="bd"]/p[@class="quote"]/span/text()')
        if quote:
            dic['quote'] = quote[0]
        else:
            # 没有引言，赋值为空字符串
            dic['quote'] = ''
        print(dic)  # 每一组字典的数据添加到列表
        lst.append(dic)

# 文件的写入 如果是字典 表头必须要跟字典的key保持一致
heads = ('titles', 'types', 'star', 'quote')
with open('douban.csv', 'w', encoding='utf-8-sig', newline='') as f:
    # 1.创建csv写入对象
    w = csv.DictWriter(f, fieldnames=heads)
    # 2. 写入表头
    w.writeheader()
    # 3. 一次性写入多行数据
    w.writerows(lst)
'''
list index out of range
'''