import pandas as pd
import csv
import read_write_csv
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
        #创建一个csv文件接受查询结果
        f= open('search_name_result.csv', 'w')
        csv_writer=csv.writer(f)
        csv_writer.writerow(["Name", "Place", "Month","Date","Hour","Minute"])
        a=0
        #按行读取查询
        with open(path, 'r', encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            for row in reader:
                if row['name'] == name:
                    csv_writer.writerow(row.values())
                    a+=1
            f.close()
            #判断是否输入了一个错误的名字
            try:
                b=1/a
            except:
                raise WrongNameError

#按地点查询
def search_Place(path, place):##需要路径和需要查询的地点
    # 创建一个csv文件接受查询结果
    f = open('search_place_result.csv', 'w')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["Name", "Place", "Month", "Date", "Hour", "Minute"])
    a = 0
    # 按行读取查询
    with open(path, 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['place'] == place:
                csv_writer.writerow(row.values())
                a += 1
        f.close()
        # 判断是否输入了一个错误的地点
        try:
            b = 1 / a
        except:
            raise WrongPlaceError
#按时间查询
def search_Hour(path, hour):##需要路径和需要查询的时间点
    # 创建一个csv文件接受查询结果
    f = open('search_hour_result.csv', 'w')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["Name", "Place", "Month", "Date", "Hour", "Minute"])
    a = 0
    # 按行读取查询
    with open(path, 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if row['hour'] == str(hour):
                csv_writer.writerow(row.values())
                a += 1
        f.close()
        # 判断是否输入了一个没有猫出现的时间
        try:
            b = 1 / a
        except:
            raise WrongTimeError
#按时间段查询
def search_Period(path, t1,t2):##需要路径和需要查询的时间段
    # 创建一个csv文件接受查询结果
    f = open('search_period_result.csv', 'w')
    csv_writer = csv.writer(f)
    csv_writer.writerow(["Name", "Place", "Month", "Date", "Hour", "Minute"])
    a = 0
    # 按行读取查询
    with open(path, 'r', encoding="utf-8") as csvfile:
        reader = csv.DictReader(csvfile)
        hour=int(t1)
        for row in reader:
            while hour<=t2:
                if row['hour'] == str(hour):
                    csv_writer.writerow(row.values())
                    a += 1
                hour+=1
            hour = int(t1)
        f.close()
        # 判断是否输入了一个没有猫出现的时间
        try:
            b = 1 / a
        except:
            raise WrongTimeError

#测试模块
if __name__=='__main__':
    search_name('./CSVtest.csv','cat1')
    search_Place('./CSVtest.csv', 'area3')
    search_Hour('./CSVtest.csv', 9)
    search_Period('./CSVtest.csv', 2,10)
