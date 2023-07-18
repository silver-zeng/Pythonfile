import os
import time

# print(open(r"D:\数据列表.txt"))
# with open(r"C:\Users\59872\Desktop\数据清单.txt","a+",encoding = "UTF-8") as f:
#     re=f.read()
#     f.write("\n~~~~~~~~~~~~测试下Python自动化写入~~~~~~~~~~~~~~")
#     print(re)

for i in range(10):
    print(i)
time=time.localtime()
print(time.strftime("%y-%m-%d %H:%M:%S",time.localtime()))#以time.strftime()格式化时间
print(time.strftime("%Y-%m-%d %H:%M:%S",time.localtime()))