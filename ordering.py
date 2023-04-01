import pandas as pd
import functools
import csv

# 本文件为排序模块

"""
根据名称进行排序
输入参数: dataframe, flag(升序或降序)
"""
def order_Name(dataframe,flag):
        df_data_order0 = dataframe.sort_values(by=['name'],ascending=[flag])
        return df_data_order0

"""
根据地点进行排序
输入参数: dataframe, flag(升序或降序)
"""
#order the dataset by Place
def order_Place(dataframe,flag):
        df_data_order0 = dataframe.sort_values(by=['place'],ascending=[flag])
        return df_data_order0

"""
根据时间进行排序
输入参数: dataframe, flag(升序或降序)
"""
#order the dataset by Hour and Minute
def order_Time(dataframe,flag):
        df_data_order0 = dataframe.sort_values(by=['hour','minute'],ascending=[flag,flag])
        return df_data_order0

"""
根据日期进行排序
输入参数: dataframe, flag(升序或降序)
"""
#order the dataset by Date
def order_Date(dataframe,flag):
        df_data_order0 = dataframe.sort_values(by=['date'],ascending=[flag])
        return df_data_order0
