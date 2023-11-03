import pandas as pd
import numpy
import matplotlib.pyplot as plt
# 读取csv文件
# pd_csv = pd.read_csv(r"D:\python_file\Pythonfile\找煤网.csv", encoding="GBK", chunksize=100)
# for i in pd_csv:
#     df =pd.DataFrame(i)
#     i["数据更新日期"], i["更新时间"] = zip(*i["数据更新日期"].str.split(" "))
#     # i["数据更新时间"] = i["数据更新日期"].str.split(" ")[1]
#     # columns 指定字段顺序保存
#     i.to_csv('output.csv', index=False, columns=["数据更新日期", "更新时间", "标题", "煤炭种类", "当日价格", "当日涨幅"])
#     print(i)


# 读取excel文件
path = 'exa10.xlsx'
readexcel1 = pd.read_excel(path, sheet_name="股票")
print(readexcel1)
df =pd.DataFrame(readexcel1)
# 绘制柱状图
# 将DataFrame中的数据绘制成柱状图
df.plot(kind='line', x='日期', y=['股票0', '股票1'], legend=None)
plt.xlabel('日期')
plt.ylabel('股票')
plt.show()