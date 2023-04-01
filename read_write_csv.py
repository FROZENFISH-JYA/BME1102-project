import pandas as pd
import csv

# 本文件为I/O模块

"""
从数据库读取记录,保存在dataframe中
"""
def ReadCsv(path):
    dataframe = pd.read_csv(path)
    return dataframe

"""
将dataframe中的记录写到数据库的最后
"""
def addCsv(path,dataframe):
    #add data line by line, without header or index
    dataframe.to_csv(path,mode='a',header=False,index=None)