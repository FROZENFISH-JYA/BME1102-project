import pandas as pd
#创建三种错误类，在查询不到信息时返回
class WrongNameError(Exception):
    def __str__(self):
        return "There's no such cat appeared"
class WrongPlaceError(Exception):
    def __str__(self):
        return "There's no cat appeared in this pace"
class WrongTimeError(Exception):
    def __str__(self):
        return "There's no cat appeared during this period"

#以下是函数
'''按要求输入参数,会生成一个名为search_result.csv的文件'''
#按名字查询
def search_Name(dataframe,name):#需要路径和需要查询的猫的名字
    #创建一个dataframe接受查询结果
    df = pd.DataFrame(columns=['name', 'place', 'date', 'hour', 'minute'])
    a = 0
    #按行读取查询
    for index,row in dataframe.iterrows():
        if row['name'] == name:
            df.loc[len(df)] = row
            a+=1
    #判断是否输入了一个错误的名字
    try:
        b=1/a
    except:
        raise WrongNameError
    return df


#按地点查询
def search_Place(dataframe, place):##需要路径和需要查询的地点
    df = pd.DataFrame(columns=['name', 'place', 'date', 'hour', 'minute'])
    a = 0
    # 按行读取查询
    for index,row in dataframe.iterrows():
        if row['place'] == place:
            df.loc[len(df)] = row
            a += 1
    # 判断是否输入了一个错误的地点
    try:
        b = 1 / a
    except:
        raise WrongPlaceError
    return df

#按时间段查询
def search_Period(dataframe, h1, m1, h2, m2 ):##需要路径和需要查询的时间段, h1、m1是下限,h2、m2是上限
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
    # 判断是否输入了一个没有猫出现的时间
    try:
        b = 1 / a
    except:
        raise WrongTimeError
    return df

#按日期区间查询
def search_Date(dataframe, d1, d2):##需要路径和需要查询的时间段, d1是下限,d2是上限
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
        if index == 0:
            continue
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
    # 判断是否输入了一个没有猫出现的时间
    try:
        b = 1 / a
    except:
        raise WrongTimeError
    return df


