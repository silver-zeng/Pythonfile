import pandas as pd
import plotly as plt
import plotly.offline
import plotly.express as px
from plotly import tools

gapminder = px.data.gapminder()
fig =px.choropleth(
    gapminder,
    locations="iso_alpha",
    color="lifeExp",
    color_continuous_scale=px.colors.diverging.RdBu,
    projection="natural earth",
    animation_frame="year"

)
# fig.show() # 运行了一次之后，数据就会失效，保存不到数据
plotly.offline.plot(fig, filename='./gapminder.html')