import requests
import csv
import time
import codecs


# 搜索某地区某种属性（商业/文化/酒店/学校）建筑的数据，返回一个处理后的字典列表
def searchBaidumap(keyword, region, pageIndex):
    url = 'http://api.map.baidu.com/place/v2/search'
    ak = '*****************'# 自己创建的项目 ak 参数

    finalData = []

    params = {
        "query": keyword,# 建筑属性
        "output": "json",
        "ak": ak,
        "region": region,
        "page_size": 20,# 检索每页结果数（最大20）
        "page_num": pageIndex,# 检索页码编号
        "scope": 2,
        "coord_type": 4# 目标的CAD坐标不明，尝试了多种坐标系均不符合
    }

    response = requests.get(url, params)
    result = response.json()
    status = result.get("status")
    message = result.get("message")# 服务状态码见 SDK 文档

    if status != 0 and status != 2:
        raise Exception(message)

    data = result['results']

    # 我只需要经纬度、名称、地址
    for adr in data:
        singleDict = {'name': '', 'lng': '', 'lat': '', 'address': ''}
        singleDict['name'] = adr['name']
        location = adr['location']
        singleDict['lng'] = float(location['lng'])
        singleDict['lat'] = float(location['lat'])
        singleDict['address'] = adr['address']
        finalData.append(singleDict)

    return finalData


# 将结果输出为以相应属性命名的本地 csv 文件
def saveCSV(data, fileName):
    csv_columns = data[0].keys()
    csv_file = '%s.csv' % fileName
    try:
        with codecs.open(csv_file, 'w', 'utf_8_sig') as csvfileopened:# codecs 模块防止保存到本地的文件显示乱码
            writer = csv.DictWriter(csvfileopened, fieldnames=csv_columns)# csv 模块直接写入 csv 表头和之后的每一行
            writer.writeheader()
            for singleDataSet in data:
                writer.writerow(singleDataSet)
    except IOError:
        print('I/O error')
    print('%s抓取结果已保存到%s' % (fileName, csv_file))


data = []
pageIndex = 0
keyword = '文化'# 依次为商业/文化/酒店/学校

# 爬取每一页的20个结果，直到最后一页结果数小于20
while (True):
    singlePageData = searchBaidumap(keyword, '**', pageIndex)# 相关城市名称
    data.extend(singlePageData)# list.append() 和 list.extend() 的区别
    print('第%d页已抓取' % (pageIndex + 1))
    if (len(singlePageData) < 20):
        break
    pageIndex += 1
    time.sleep(0.5)

print('%s类别下共抓取到%d条信息' % (keyword, len(data)))

saveCSV(data, keyword)
