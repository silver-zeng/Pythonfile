import pyecharts
from pyecharts.charts import *
import random
from pyecharts import options as opts
from pyecharts.charts import Map
from bar3d import bar_3d

province = ['广东省', '湖北省', '湖南省', '四川省', '重庆市', '黑龙江省', '浙江省', '山西省', '河北省', '安徽省', '河南省', '山东省', '西藏自治区']
def map_china():
    data = [(i, random.randint(50, 150)) for i in province]
    map = Map()
    map.add('确诊人数', data, 'china')
    # 全局配置
    map.set_global_opts(
        title_opts=opts.TitleOpts(title='全国疫情地图'),
        visualmap_opts=opts.VisualMapOpts(
            is_show=True                                          # 是否显示视觉映射配置
        )
    )
    map.render('./map.html')
    return map

def pie_yiqing():
    data = [(i, random.randint(50,150)) for i in province]
    pie1 = (
        Pie()
        .add(
            series_name="疫情分布占比情况",
            data_pair=data,
            radius=["30%", "55%"],
            min_show_label_angle=10,  # <10度不展示标签
            rosetype='area',  # 是否展示成南丁格尔图，通过半径区分数据大小，有'radius'和'area'两种模式
            # 折线（区域）图、柱状（条形）图、K线图 : {a}（系列名称），{b}（类目值），{c}（数值）, {d}（无）
            # 散点图（气泡）图 : {a}（系列名称），{b}（数据名称），{c}（数值数组）, {d}（无）
            # 地图 : {a}（系列名称），{b}（区域名称），{c}（合并数值）, {d}（无）
            # 饼图、仪表盘、漏斗图: {a}（系列名称），{b}（数据项名称），{c}（数值）, {d}（百分比）
            label_opts=opts.LabelOpts(formatter="{b}:{d}%")  # 标签内容格式器
        )
    )
    pie1.render('./pie.html')
    return pie1

# 设置可拖拽画布
page = Page(layout=Page.DraggablePageLayout, page_title="疫情传播情况")
# 在画布中添加图像
bar = bar_3d()
page.add(
    map_china(),
    pie_yiqing(),
    bar
)
page.render("数据大屏source.html")
# save_resize_html()用于  DraggablePageLayout 布局重新渲染图表
# 保存好配置文件后，注意不用再生成源数据了，只需要直接去执行page.save_resize_html，若重新生成了源文件去拖拽会改变"cid": "c5862a70d2a84e86abc7e77334ee4804",导致配置不生效
page.save_resize_html(
    source="数据大屏source.html",  # 源数据
    cfg_file='chart_config.json',  # 保存的配置文件
    dest="数据大屏v002.html"
)
