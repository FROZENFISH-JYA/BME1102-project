import pandas as pd
import csv
#read csv to dataframe
def ReadCsv(path):
    dataframe = pd.read_csv(path)
    return dataframe
#write data form dataframe to csv
def addCsv(path,dataframe):
    #add data line by line, without header or indexRe
    dataframe.to_csv(path,mode='a',header=False,index=None)