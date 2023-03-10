import pandas as pd
import csv
#读取csv文件内容
def ReadCsv(path):
    con = pd.read_csv(path)
    return con
#追加写入csv
def addCsv():
    with open(input('path:'), 'a') as f:
        writer = csv.writer(f)
        writer.writerow([input('Cat_Name:'),input('Location:'),input('Date:'),input("Time:")])










