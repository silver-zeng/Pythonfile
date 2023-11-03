import pandas as pd
import numpy
# # 第一条
# df = pd.DataFrame(numpy.random.randint(10, 20, (3, 3)),
#                   index=["a", "b", "c"],
#                   columns=["A列", "B列", "C列"]
#                   )
# df['age'] = ["22岁", "25岁", "27岁"]
# print(df)
# print("___________________________________")
#
# # 第二条,按照age降序排列
# df2 = df.sort_values(by="age", ascending=False)
# print(df2)
# print("_________________________________________")
# # 第三条，将C行,age列改为2
# df2.loc["c", "age"]=2
# print(df2)
# print("_________________________________________")
# # 第四条，增加priority，数据只有yes ，no，然后替换成布尔值
# df2["priority"] = ["yes", "no", "yes"]
# df3 = df2["priority"].isin(["yes"])
# df2["priority"]=df3
# print(df2)

# 根据名称分组统计不同颜色数量总和
# df = pd.DataFrame({"名称": ["A", "B", "A", "A", "B", "A"],
#                    "颜色": ["红色", "蓝色", "蓝色", "红色", "蓝色", "红色"],
#                    "尺寸": ["大", "大", "小", "小", "大", "大"],
#                    "数量": [10, 20, 15, 30, 10, 20]})
# print(df,"\n"+"______________源数据_______________")
# df_sum = df.groupby(["名称", "颜色"]).sum("数量")
# print(df_sum)
# print("_________________________________________")
# # 根据名称分组，统计不同颜色的数量平均值
# df_mean = df.groupby(["名称", "颜色"]).mean("数量")
# print(df_mean)
# print("_________________________________________")
# # 根据名称分组，统计不同颜色和尺寸的数量总和
# df_agg = df.groupby(["名称", "颜色", "尺寸"]).agg({
#     "颜色": "value_counts",
#     "尺寸": "value_counts",
#     "数量": sum
# })
# print(df_agg)


