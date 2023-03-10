import pandas as pd
import csv
#读取csv文件内容到dataframe
def ReadCsv(path):
    dataframe = pd.read_csv(path)
    return dataframe
#从dataframe追加写入csv
def addCsv(path,dataframe):
    #向csv追加数据
    dataframe.to_csv(path,mode='a',header=False,index=None)









