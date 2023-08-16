# 正则
"""
re.findall re模块中提供的一个函数 用于在文本中查找所有匹配某个正则表达式的字串
并返回一个包含所有匹配结果的一个列表
"""
import re

# text = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta http-equiv="X-UA-Compatible" content="IE=edge">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>表格</title>
# </head>
# <body>
#     <table>
#         <!-- <colgroup> 标签用于对表格中的列进行组合，以便对其进行格式化 -->
#         <colgroup>
#             <col bgcolor="#f79d03"></col>
#             <col bgcolor="#ffd4f5"></col>
#             <col bgcolor="#e80063"></col>
#             <col bgcolor="#24ff45"></col>
#         </colgroup>
#         <tr>
#             <th>排名</th><th>公司</th>
#             <th>营收（单位：百万美元）</th>
#             <th>利润（单位：百万美元）</th>
#         </tr>
#         <tr>
#             <td>1</td>
#             <td>公司A</td>
#             <td>323、139.0</td>
#             <td>12、284.0</td>
#         </tr>
#         <tr>
#             <td>2</td>
#             <td>公司B</td>
#             <td>234、369.0</td>
#             <td>35、235.0</td>
#         </tr>
#         <tr>
#             <td>3</td>
#             <td>公司C</td>
#             <td>396、486.0</td>
#             <td>58、758.0</td>
#         </tr>
#     </table>
# </body>
# </html>
# """
# a = re.findall('\d+', text)  # 第一个参数是正则表达式 第二个参数是文本内容
# print(a)

# result = re.sub('<th>', '<p>', text)  # 替换 在一个文本中 把第一参数替换成第二个
# print(result)


# test1 = re.findall(r'<th>(.*?)</th>',text)
# print(test1)
import time


"""
贪婪匹配 (.*) 在贪婪匹配中 正则表达式会尽可能的匹配最长的字串  意味着它会从文本的起始位置开启 尝试匹配
最长的满足条件的子串 直到无法匹配为止
非贪婪匹配 (.*?): 在非贪婪匹配中 正则表达式会尽可能的匹配最短的字串
"""
# a = re.findall('<.*>', '<tag1>text<tag2>')  # 贪婪匹配
# print(a)
# b = re.findall('<.*?>', '<tag1>text<tag2>')  # 非贪婪匹配
# print(b)


# 案例一：爬取情话实现微信轰炸
import requests
import keyboard
import pyautogui

# for j in range(40,200):
#     response = requests.get(f'https://www.ainicr.cn/qh/{j}.html') 发送请求
#     a = re.findall('<p>(.*?)<p>',response.text) 匹配内容
#     time.sleep(3)  等待三秒
#     for i in a:
#         keyboard.write(i) 输入文本
#         keyboard.press_and_release('enter') 回车


# for i in range(5):
#     pyautogui.click(1050, 820)
#     time.sleep(1)
#     keyboard.write('你好')
#     time.sleep(1)
#     keyboard.press_and_release('enter')
#     time.sleep(1)


# 案例二：每日自动推送微博热搜 下面有注释
# import requests
# import re
#
# url = 'https://s.weibo.com/top/summary'
# headers = {
#     'Cookie': 'SUB=_2AkMTiP79f8NxqwFRmPAVzW_qZYRyzgnEieKl1A8mJRMxHRl-yT9kqkI_tRB6OAjQEbJj6OQhexByvD5Vg8ZIoz_6B5jP; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WF4O_pp6ecrXxj_4WjG0Mhi; SINAGLOBAL=1838828417801.6345.1691644389295; _s_tentry=-; Apache=6865466752999.341.1691757937186; ULV=1691757937207:2:2:2:6865466752999.341.1691757937186:1691644389327',
# }
# response = requests.get(url, headers=headers)
# a = re.findall('<a href="(.*?)" target="_blank">(.*?)</a>', response.text)
# a.pop()
# a.pop()
# for i in a:
#     with open('./test1.txt', 'a', encoding='utf-8') as f:
#         f.write('https://s.weibo.com/' + i[0]+'\n')
#         f.write(i[1]+'\n')
#         f.write('-----------------------------------------'+'\n')


# 完整发送邮件案例
import schedule
import time
import smtplib
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
    msg['Subject'] = Header('Test Email', 'utf-8')
    msg['From'] = '598725443@qq.com'  # 发件人
    msg['To'] = '598725443@qq.com'  # 收件人

    # 发送邮件
    with smtplib.SMTP_SSL('smtp.qq.com', 465) as server:
        server.login('598725443@qq.com', 'mbbmxsrwdeblbeea')  # 登录SMTP服务器
        server.send_message(msg)  # 发送邮件


def parch():
    url = 'https://s.weibo.com/top/summary'
    headers = {
        'Cookie': 'SUB=_2AkMTiP79f8NxqwFRmPAVzW_qZYRyzgnEieKl1A8mJRMxHRl-yT9kqkI_tRB6OAjQEbJj6OQhexByvD5Vg8ZIoz_6B5jP; SUBP=0033WrSXqPxfM72-Ws9jqgMF55529P9D9WF4O_pp6ecrXxj_4WjG0Mhi; SINAGLOBAL=1838828417801.6345.1691644389295; _s_tentry=-; Apache=6865466752999.341.1691757937186; ULV=1691757937207:2:2:2:6865466752999.341.1691757937186:1691644389327',
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
schedule.every().day.at("12:50").do(parch)   # 定时调用parch函数
schedule.every().day.at("12:50").do(send_email)  # 设置每天的定时发送时间

# 循环执行定时任务
while True:
    schedule.run_pending()  # 运行待执行的定时任务
    time.sleep(1)  # 等待1秒，避免过于频繁的检查
    with open('./test1.txt', 'w') as f: #清空文本内容
        f.write('')


# 发邮件模板
# import schedule
# import time
# import smtplib
# from email.mime.text import MIMEText
# from email.header import Header
#
#
# def send_email():
#     # 创建邮件内容
#     msg = MIMEText('自动推送内容')
#     msg['Subject'] = Header('Test Email', 'utf-8')
#     msg['From'] = '598725443@qq.com'  # 发件人
#     msg['To'] = '2470064952@qq.com'  # 收件人
#
#     # 发送邮件
#     with smtplib.SMTP_SSL('smtp.qq.com', 465) as server:
#         server.login('598725443@qq.com', 'mbbmxsrwdeblbeea')  # 登录SMTP服务器
#         server.send_message(msg)  # 发送邮件
#
#
# # 定义定时任务
# schedule.every().day.at("19:13").do(send_email)  # 设置每天的定时发送时间
#
# # 循环执行定时任务
# while True:
#     schedule.run_pending()  # 运行待执行的定时任务
#     time.sleep(1)  # 等待1秒，避免过于频繁的检查
