# SearchPOIWithBaiduMapAPI_Python_Grasshopper

The project written in Python searches POI with Baidu Map API, and saves the results as .csv file. Grasshopper script transforms the csv data into model with points and texts.

## 任务目标

在地图上标出城市范围内的商业、文化、酒店、学校建筑，并挑选重点建筑研究其规模、业态。

## 思路

1. **数据爬取：**利用百度地图 API 爬取该城市中某一类别的所有建筑；
2. **数据整理：**把需要的信息整理成字典，写入`csv`文件；
3. **模型生成：**用 **Grasshopper** 读取`csv`文件，处理数据，生成点；
4. **模型调整：**把经纬度转换成**地图**或者已有的 **CAD** 采用的坐标系。

详情见[Python请求百度地图API爬取城市建筑属性并用Grasshopper进一步处理](https://www.zmei.moe/postshtml/01blog/00coding/2020-06-23-baidumapAPI-grasshopper.html)。

For more info please refer to [Python请求百度地图API爬取城市建筑属性并用Grasshopper进一步处理](https://www.zmei.moe/postshtml/01blog/00coding/2020-06-23-baidumapAPI-grasshopper.html).
