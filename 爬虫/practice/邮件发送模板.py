import schedule
import time
import smtplib
from 自动发邮件案例.mime.text import MIMEText
from 自动发邮件案例.header import Header


def send_email():
    # 创建邮件内容
    msg = MIMEText('自动推送内容')
    msg['Subject'] = Header('Test Email', 'utf-8')
    msg['From'] = '598725443@qq.com'  # 发件人
    msg['To'] = '2470064952@qq.com'  # 收件人

    # 发送邮件
    with smtplib.SMTP_SSL('smtp.qq.com', 465) as server:
        server.login('598725443@qq.com', 'mbbmxsrwdeblbeea')  # 登录SMTP服务器
        server.send_message(msg)  # 发送邮件


# 定义定时任务
schedule.every().day.at("19:13").do(send_email)  # 设置每天的定时发送时间

# 循环执行定时任务
while True:
    schedule.run_pending()  # 运行待执行的定时任务
    time.sleep(1)  # 等待1秒，避免过于频繁的检查
