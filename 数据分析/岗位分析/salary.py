import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

file = pd.read_csv("salary.csv", encoding="ANSI")
df = pd.DataFrame(file)
# 缺失值替换为“无数据”
df = df.fillna("无数据")
print(df.isnull().sum())
# 替换工资中的K
df['salary'] = df['salary'].str.replace("k","")
# 使用正则表达式提取
df[['最低薪资','最高薪资']] = df['salary'].str.extract(r'(\d+)-(\d+)')
df.to_csv(".salary_end.csv",index=False)

city_jobs_num = df.groupby('city').size()
print(city_jobs_num)
# 绘制饼状图
plt.figure(figsize=[6.5, 6.5], dpi=150)
city_jobs_num.plot.pie(y='city', autopct="%.1f%%", labeldistance=1.2, pctdistance=0.9)
# 表头不能显示中文，得设置字体
plt.title('职位分布')
plt.rcParams['font.sans-serif'] = 'SimHei' # 设置字体为黑体
plt.rcParams['font.size'] = 10
plt.xticks(rotation=60)  # 这里的45是旋转的角度，可以根据需要进行调整
plt.show()
# 绘制折线图
# plt.plot()