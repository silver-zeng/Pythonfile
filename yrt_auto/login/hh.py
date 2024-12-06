from datetime import datetime
import os
from selenium import webdriver
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait  # 显示等待
from selenium.webdriver.support import expected_conditions as EC
import time
import pytest
import logging


# 日志配置
log_directory = "../TestLogs/"
current_date = datetime.now().strftime("%Y-%m-%d")
log_file_path = os.path.join(log_directory, f"log_{current_date}.log")

# 确保日志目录存在
if not os.path.exists(log_directory):
    os.makedirs(log_directory)

# 配置日志
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(log_file_path),
        logging.StreamHandler()  # 输出到控制台
    ]
)
logging.info("Starting test execution...")
# # 获取当前日期并格式化为字符串
# current_date = datetime.datetime.now().strftime('%Y-%m-%d')
# LOGGING = {
#     'version': 1,
#     # 包含一个或多个处理程序（handlers），用于将日志记录输出到不同目的地
#     'handlers': {
#         'file': {
#             'level': 'DEBUG',
#             'class': 'logging.handlers.TimedRotatingFileHandler',   # 输出到文件，且有滚动策略
#             'filename': os.path.join(BASE_DIR, f'logs/debug-{current_date}.log'),
#             'formatter': 'verbose_more',  # 指定输出格式的模板
#             'filters': ['require_debug_true'],  # 注册下面定义的过滤器
#             # 'maxBytes': 1 * 1024 * 1024,  # 定义文件最大为多少  这个只有RotatingFileHandler类能使用
#             'backupCount': 10,  # 定义保留的文件数量，若超过后会覆盖前面的文件
#             'when': 'D',  # 按日期滚动，每天一个日志文件
#         },
#         'console': {
#             'level': 'INFO',
#             'class': 'logging.StreamHandler',  # 输出到控制台
#             'formatter': 'simple',  # 指定简单的输出模板，formatter需要自己定义，simple 为当中不同的模板，与控制器平级
#         },
#     },
#     # 定义模板formatters为固定的key
#     'formatters': {
#         'verbose': {
#             'format': '{levelname}-{asctime}-{module}-{lineno:d}:==={message}',
#             'style': '{',
#         },
#         'simple': {
#             'format': '{levelname}-{module}-{lineno:d}:==={message}',
#             'style': '{',
#         },
#         'verbose_more': {
#             'format': '{levelname}-{asctime}-【{filename} {lineno:d}】-{process:d}-{thread:d}:==={message}',
#             'style': '{',
#         },
#     },
#     # 定义过滤器
#     'filters': {
#         # 只有DEBUG为True的时候才会输出日志
#         'require_debug_true': {
#           '()': 'django.utils.log.RequireDebugTrue',
#         },
#     },
#     # 指定日志记录器的根记录器
#     'loggers': {
#         'django': {
#             'handlers': ['file', 'console'],  # 添加上面定义的处理器
#             'level': 'DEBUG',
#             'propagate': True,
#         },
#     },
# }