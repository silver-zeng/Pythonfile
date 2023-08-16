import schedule
import time
from smtplib import SMTP_SSL
from email.mime.text import MIMEText
from email.header import Header
import requests
import re


def send_email():
    # 创建邮件内容
    time.sleep(5)
    with open('./test1.txt', 'r', encoding='utf-8') as f:
        x = f.read()  # 读取文本内容
    msg = MIMEText(x)  # 发送邮件内容
    msg['Subject'] = Header('Test Email:微博热搜50', 'utf-8')
    msg['From'] = '598725443@qq.com'  # 发件人
    msg['To'] = '1224900587@qq.com'  # 收件人

    # 发送邮件
    with SMTP_SSL('smtp.qq.com', 465) as server:
        server.login('598725443@qq.com', 'mbbmxsrwdeblbeea')  # 登录SMTP服务器
        server.send_message(msg)  # 发送邮件


def parch():
    url = 'https://s.weibo.com/top/summary'
    headers = {
        'Cookie': 'SUB=_2AkMThTpNf8NxqwJRmfgcymnhZYlyzg_EieKl2cuWJRMxHRl-yT9kqk0GtRB6OAUUosPwcTF4eF2sG41vi9Df3QHV6aO2; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9Whqdq0cFH.UdDj_OOacf862',
    }
    response = requests.get(url, headers=headers)
    a = re.findall('<a href="(.*?)" target="_blank">(.*?)</a>', response.text)   # 从网页源代码提取数据
    a.pop() # 删除最后一个
    a.pop()
    for i in a:
        with open('./test1.txt', 'a', encoding='utf-8') as f:  # 写入内容 i[0]是网址 i[1]为热点的名称
            f.write('https://s.weibo.com/' + i[0] + '\n')
            f.write(i[1] + '\n')
            f.write('-----------------------------------------' + '\n')


# 定义定时任务
schedule.every().day.at("10:14").do(parch)   # 定时调用parch函数
schedule.every().day.at("10:14").do(send_email)  # 设置每天的定时发送时间

# 循环执行定时任务
while True:
    schedule.run_pending()  # 运行待执行的定时任务
    time.sleep(1)  # 等待1秒，避免过于频繁的检查
    with open('./test1.txt', 'w', encoding='utf-8') as f: #清空文本内容
        f.write('热搜TOP50\n')
