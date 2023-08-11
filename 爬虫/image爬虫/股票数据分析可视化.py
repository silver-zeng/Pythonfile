import pandas as pd
from pyecharts import options as opts
from pyecharts.charts import Bar
data_df = pd.read_csv('data2.csv')
df1 = data_df[['股票名称', '涨跌幅']]
df2 = df1.iloc[:30]
print(df2['股票名称'].values)
print(df2['涨跌幅'].values)
c = (
    Bar()
        .add_xaxis(list(df2['股票名称']))
        .add_yaxis("股票成交量情况", list(df2['涨跌幅']))
        .set_global_opts(
        title_opts=opts.TitleOpts(title="成交量图表 - Volume chart"),
        datazoom_opts=opts.DataZoomOpts(),
    )
        .render("data.html")
)

print('数据可视化结果完成,请在当前目录下查找打开 data.html 文件!')