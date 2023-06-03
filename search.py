import pandas as pd
import read_write_csv as rw
# 本文件为查找模块

# 创建三种错误类，在查询不到信息时返回
class WrongNameError(Exception):
    def __str__(self):
        return "There's no such cat appeared"
class WrongPlaceError(Exception):
    def __str__(self):
        return "There's no cat appeared in this pace"
class WrongTimeError(Exception):
    def __str__(self):
        return "There's no cat appeared during this period"

"""
按名称查询
功能: 读取dataframe, 查询名称等于name的记录, 返回一个只包含符合条件的记录的dataframe
输入参数: dataframe, 名称
"""
def search_Name(dataframe,name):
    #创建一个dataframe接受查询结果
    df = pd.DataFrame(columns=['name', 'place', 'date', 'hour', 'minute'])
    a = 0
    #按行读取查询
    for index,row in dataframe.iterrows():
        if row['name'] == name:
            df.loc[len(df)] = row
            a+=1

    return df
"""
按日期查询
功能: 读取dataframe, 查询名称等于name的记录, 返回一个只包含符合条件的记录的dataframe
输入参数: dataframe, 名称
"""
def search_date(dataframe,date):
    #创建一个dataframe接受查询结果
    df = pd.DataFrame(columns=['name', 'place', 'date', 'hour', 'minute'])
    a = 0
    #按行读取查询
    for index,row in dataframe.iterrows():
        if row['date'] == date:
            df.loc[len(df)] = row
            a+=1
    return df

"""
按地点查询
功能: 读取dataframe, 查询地点等于place的记录, 返回一个只包含符合条件的记录的dataframe
输入参数: dataframe, 地点
"""
def search_Place(dataframe, place):
    df = pd.DataFrame(columns=['name', 'place', 'date', 'hour', 'minute'])
    a = 0
    # 按行读取查询
    for index,row in dataframe.iterrows():
        if row['place'] == place:
            df.loc[len(df)] = row
            a += 1

    return df
"""查询某个特定日期猫出现的次数"""
def search_1_date(date):
    df = rw.ReadCsv()
    # 按行读取查询
    n=0
    for index, row in df.iterrows():
        if row['date']==date:
            n+=1
    return n
"""查询某个特定地点猫出现的次数"""
def search_1_area(area):
    df = rw.ReadCsv()
    # 按行读取查询
    n=0
    for index, row in df.iterrows():
        if row['place']==area:
            n+=1
    return n
"""
按时间查询
功能: 读取dataframe, 查询时间处于指定时间段中的记录, 返回一个只包含符合条件的记录的dataframe
输入参数: dataframe, h1(小时下限), m1(分钟下限), h2(小时上限), m2(分钟上限)
使用本函数前应当先查询日期
"""
def search_Period(dataframe, h1, m1, h2, m2 ):
    df = pd.DataFrame(columns=['name', 'place', 'date', 'hour', 'minute'])
    a = 0
    # 按行读取查询
    for index,row in dataframe.iterrows():
        h = int(row['hour'])
        m = int(row['minute'])
        if h >= h1 and h <= h2:
            if h == h1 and m < m1:
                continue
            if h == h2 and m > m2:
                continue
            df.loc[len(df)] = row
            a += 1

    return df

"""
按日期查询
功能: 读取dataframe, 查询日期处于指定日期区间内的记录, 返回一个只包含符合条件的记录的dataframe
输入参数: dataframe, d1(日期下限), d2(日期限)
使用本函数前应当先查询日期
"""
def search_Date(dataframe, d1, d2):
    df = pd.DataFrame(columns=['name', 'place', 'date', 'hour', 'minute'])
    a = 0
    d1 = d1.split(".")
    year1 = int(d1[0])
    month1 = int(d1[1])
    date1 = int(d1[2])
    d2 = d2.split(".")
    year2 = int(d2[0])
    month2 = int(d2[1])
    date2 = int(d2[2])
    # 按行读取查询
    for index,row in dataframe.iterrows():
        #分割日期，准备比较
        d = row['date'].split(".")
        year = int(d[0])
        month = int(d[1])
        date = int(d[2])
        #判断年份范围
        if year >= year1 and year <= year2:
            #若年份与下限相同，判断月份
            if year == year1:
                if month < month1:
                    continue
                #若月份与下限还相同，判断日期
                elif month == month1 and date < date1:
                    continue
                else:
                    pass
            else:
                pass
            #若年份与上限相同，判断月份
            if year == year2:
                if month > month2:
                    continue
                #若月份与上限还相同，判断日期
                elif month == month2 and date > date2:
                    continue
                else:
                    pass
            else:
                pass
        #将此行数据写入dataframe
        df.loc[len(df)] = row
        a += 1
    return df


