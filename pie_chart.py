import read_write_csv as rw
import search as s
import ordering as o
import pandas as pd
import matplotlib.pyplot as plt


# 设置中文字体
plt.rcParams['font.sans-serif']=['Microsoft JhengHei']

'''
绘制饼图
功能: 从数据库中检索指定日期区间内的记录,并统计每只猫的活跃度(出现次数占比),绘制饼图
输入参数: 日期下限,日期上限
'''
def pie_chart(date1,date2):
    # 读取原始数据
    df = rw.ReadCsv()
    # 截取date1和date2间的记录
    df = s.search_Date(df,date1,date2)
    # 对每只猫做名称检索，统计其出现次数
    list = []
    for a in range(1,11):
      name = 'cat' + str(a)
      df1 = s.search_Name(df,name)
      list.append(df1.shape[0])
      colors = ["#55efc4", "#81ecec", "#74b9ff", "#a29bfe", "#dfe6e9", "#ffeaa7", "#fab1a0", "#fd79a8", "#e17055", "#fdcb6e"]
    plt.pie(x = list, 
            labels = ['cat1','cat2','cat3','cat4','cat5','cat6','cat7','cat8','cat9','cat10'], 
            shadow = False, 
            autopct = '%1.1f%%', 
            startangle = 90,
            colors = colors)
    title = f"{date1}至{date2}的活跃度统计"
    plt.title(title)
    plt.axis('equal')
    plt.legend(loc='upper right')
    plt.show()
    return