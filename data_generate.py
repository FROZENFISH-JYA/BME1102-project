import pandas as pd
import search as s
import read_write_csv as r
import numpy as np
import calendar

#查询某一天某只猫的作息时间，返回每个小时所查猫的出现次数
def data_generate1(date,name):
    df=r.ReadCsv()
    t_list=list(np.zeros(24,dtype='int'))#创建一个0—24小时的全零列表
    da_se=s.search_Date(df,date,date)#先按日期过滤
    na_se=s.search_Name(da_se,name)#再按名称过滤
    hour_list=list(na_se['hour'])
    for i in hour_list:#依次记录每个小时的出现次数
        n=hour_list.count(i)
        hour_list.remove(i)#减少计算量
        t_list[i-1]=n
    return t_list

#查询某只猫在某个月内的出没情况，返回每天出现次数
def data_generate2(month,name):#month的输入格式为“年.月“，如”2023.01“
    df = r.ReadCsv()
    k=month.split('.')#分割年月
    year=int(k[0])
    month_=int(k[1])
    #判断所查月份天数
    a=calendar.monthrange(year, month_)[1]
    t_list = list(np.zeros(a, dtype='int'))#创建一个长度为所查月天数的全零列表
    #创建长度为那个月天数的列表
    da_se=s.search_Date(df,month+'.01',month+f'.{a}')#先按日期过滤
    na_se=s.search_Name(da_se,name)#再按名称过滤
    date_list=list(na_se['date'])#每出现一次就会多一次出现的日期
    for i in date_list:#依次记录每个小时的出现次数
        n=date_list.count(i)
        p=i.split('.')
        day=int(i[8:])
        t_list[day-2]=n
        day+=1
    return t_list

#查询某只猫在某年内的出没情况，返回每天出现次数
def data_generate3(year,name):#month的输入格式为“年“，如”2023“
    df = r.ReadCsv()
    t_list = list(np.zeros(12, dtype='int'))#创建一个长度为12的全零列表
    da_se=s.search_Date(df,year+'.1.1',year+'.12.31')#先按日期过滤
    na_se=s.search_Name(da_se,name)#再按名称过滤
    month_list=[]
    for i in na_se['date']:
        m=i.split('.')
        month_list.append(m[1])
    for i in month_list:#依次记录每个小时的出现次数
        n=month_list.count(i)
        p=i.split('.')
        month=int(i)
        month_list.remove(i)
        t_list[month-1]=n
    return t_list

#查询某天某个地点猫的出没情况，返回每个小时的所查地猫的出现次数
def data_generate4(date,area):
    df = r.ReadCsv()
    t_list=list(np.zeros(24,dtype='int'))#创建一个0—24小时的全零列表
    da_se=s.search_date(df,date)#先按日期过滤
    na_se=s.search_Place(da_se,area)#再按地点过滤
    hour_list=list(na_se['hour'])
    for i in hour_list:#依次记录每个小时的出现次数
        n=hour_list.count(i)
        t_list[i-1]=n
    return t_list

##查询某月某个地点猫的出没情况，返回每天的所查地猫的出现次数
def data_generate5(month,area):#month的输入格式为“年.月“，如”2023.01“
    df = r.ReadCsv()
    k=month.split('.')#分割年月
    year=int(k[0])
    month_=int(k[1])
    #判断所查月份天数
    a=calendar.monthrange(year, month_)[1]
    t_list = list(np.zeros(a, dtype='int'))#创建一个长度为所查月天数的全零列表
    #创建长度为那个月天数的列表
    da_se=s.search_Date(df,month+'.01',month+f'.{a}')#先按日期过滤
    na_se=s.search_Place(da_se,area)#再按地点过滤
    date_list=list(na_se['date'])#每出现一次就会多一次出现的日期
    for i in date_list:#依次记录每个小时的出现次数
        n=date_list.count(i)
        p=i.split('.')
        day=int(i[8:])
        t_list[day-2]=n
        day+=1
    return t_list
