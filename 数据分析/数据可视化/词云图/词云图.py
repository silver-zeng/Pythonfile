import time
import requests
import json
import random
import pandas as pd
import jieba # 分词工具包
import numpy as np
from PIL import Image
import wordcloud
from wordcloud import WordCloud

now_time =int(time.time())
timestamp = now_time*1000
keyword = input('请输入你要搜索的关键词:')
pageIndex = int(input('请输入要抓取的数据的页数-整数:'))
base_url_list = []
for page in range(1,pageIndex+1):
    base_url = f"https://careers.tencent.com/tencentcareer/api/post/Query?timestamp={timestamp}&countryld=&cityld=&bgIds=&productId=&categoryId=&parentCategoryld=&attrId=&keyword={keyword}&pageIndex={page}&pageSize=10&language=zh-cn&area=cn"
    base_url_list.append(base_url)
print(base_url_list)
# 抓取招聘信息
lis = []
# 抓取腾讯招聘数据
def database():
    global DD
    for i in range(pageIndex):
        response = requests.get(base_url_list[i])
        result = response.content.decode("utf-8")
        time.sleep(random.randint(1, 5))
        # 解析成python对象
        content_dict = json.loads(result)
        # 提取信息
        post_list = content_dict["Data"]["Posts"]
        for value_dic in post_list:
            dic = {}
            dic["RecruitPostName"] = value_dic["RecruitPostName"]
            dic["Responsibility"] = value_dic["Responsibility"]
            dic["LastUpdateTime"] = value_dic["LastUpdateTime"]
            lis.append(dic)
    DD = pd.DataFrame(lis)
    DD.to_csv("./腾讯招聘.csv", index=False)
    return DD
# 分词
def chinese_jieba():
    res_list=[]
    for i in DD["Responsibility"]:
        res_list.append(str(i))  # 列标
        st = ''.join(res_list)  # 列表变成字符串
        wordlist_jieba = jieba.lcut(st)
        txt_jieba = ' '.join(wordlist_jieba)  # 分词字符串，用空格分开
        return txt_jieba
# 生成词云图
def wordcloud_generate():
    stopwords = ['腾讯', '的', '好']  # 过滤掉不用的词
    txt = chinese_jieba()
    # 获取背景图
    background_img = np.array(Image.open(r'爱心模板.jpg'))
    wordcloud = WordCloud(
        font_path=r'C:\Windows\Font\STZHONGS.TTF',
        # background_color='pink',
        background_color='rgba(255, 255, 255, 0)',  # 设置背景透明度为0（完全透明）
        max_words=200,
        max_font_size=400,
        stopwords=stopwords,
        contour_color='white',
        contour_width=1,
        mask=background_img
    ).generate(txt)
    image = wordcloud.to_image()
    wordcloud.to_file('词云图.jpg')
    image.show()
if __name__ == '__main__':
    data= database()
    wordcloud_generate()