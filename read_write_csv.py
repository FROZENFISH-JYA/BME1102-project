import pandas as pd
import csv

# 本文件为I/O模块

"""
从数据库读取记录,保存在dataframe中
"""
def ReadCsv():
    dataframe = pd.read_csv('./CSVtest.csv')
    return dataframe

"""
将dataframe中的记录写到数据库的最后
"""
def addCsv(dataframe):
    #add data line by line, without header or index
    dataframe.to_csv('./CSVtest.csv',mode='a',header=False,index=None)

"""
data = ['cat1', 'area5', '2023.1.4', 11, 21]
addCsv(pd.DataFrame([data]))
"""