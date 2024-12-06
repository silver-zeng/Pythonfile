
import pytest
from datetime import datetime
import os
import logging

@pytest.fixture(autouse=True, scope="session")
def setup_logging():
    # 日志配置
    log_directory = "../TestLogs/"
    current_date = datetime.now().strftime("%Y-%m-%d")
    log_file_path = os.path.join(log_directory, f"log_{current_date}.log")

    # 确保日志目录存在
    if not os.path.exists(log_directory):
        os.makedirs(log_directory)
        print(f"Created directory: {log_directory}")

    # 打印日志文件路径
    print(f"Log file path: {log_file_path}")

    # 配置日志
    logging.basicConfig(
        level=logging.INFO,
        format='%(asctime)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(log_file_path),
            logging.StreamHandler()  # 输出到控制台
        ]
    )
