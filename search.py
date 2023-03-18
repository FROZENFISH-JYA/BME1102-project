import pandas as pd
import csv
import read_write_csv
import ordering as o
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
'''按要求输入参数，会生成一个名为search_result.csv的文件'''
#按名字查询
def search_name(path,name):#需要路径和需要查询的猫的名字
        #创建一个dataframe接受查询结果
        f= open('search_name_result.csv', 'w')
        df = pd.DataFrame(columns=['name', 'place', 'date', 'hour', 'minute'])
        a = 0
        #按行读取查询
        with open(path, 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['name'] == name:
                    df.loc[len(df)] = row
                    a+=1
            f.close()
            #判断是否输入了一个错误的名字
            try:
                b=1/a
            except:
                raise WrongNameError
        return df


#按地点查询
def search_Place(path, place):##需要路径和需要查询的地点
    # 创建一个csv文件接受查询结果
    f = open('search_place_result.csv', 'w')
    df = pd.DataFrame(columns=['name', 'place', 'date', 'hour', 'minute'])
    a = 0
    # 按行读取查询
    with open(path, 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['place'] == place:
                df.loc[len(df)] = row
                a += 1
        f.close()
        # 判断是否输入了一个错误的地点
        try:
            b = 1 / a
        except:
            raise WrongPlaceError
    return df

#按时间段查询
def search_Period(path, h1, m1, h2, m2 ):##需要路径和需要查询的时间段, h1、m1是下限,h2、m2是上限
    # 创建一个csv文件接受查询结果
    f = open('search_period_result.csv', 'w')
    df = pd.DataFrame(columns=['name', 'place', 'date', 'hour', 'minute'])
    a = 0
    # 按行读取查询
    with open(path, 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            h = int(row['hour'])
            m = int(row['minute'])
            if h >= h1 and h <= h2:
                if h == h1 and m < m1:
                    continue
                if h == h2 and m > m2:
                    continue
                df.loc[len(df)] = row
                a += 1
        f.close()
        # 判断是否输入了一个没有猫出现的时间
        try:
            b = 1 / a
        except:
            raise WrongTimeError
    return df

#测试模块
if __name__=='__main__':

    df=search_Period('./CSVtest.csv', 2,10,9,50)
    print(df)


