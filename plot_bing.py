import read_write_csv as rw
import search as s
import ordering as o
import pandas as pd
import matplotlib.pyplot as plt
def search_by_data():
    df=rw.ReadCsv("./CSVtest.csv")
    print("original:")
    print(df)

    data1=input('search_data1:')
    data2=input('search_data2:')
    df=s.search_Date(df,data1,data2)
    list=[]
    for a in range(1,11):
        name='cat'+str(a)
        df1=s.search_Name(df,name)
        list.append(df1.shape[0])
    print(list)
    plt.pie(x=list,labels=['cat1','cat2','cat3','cat4','cat5','cat6','cat7','cat8','cat9','cat10'],shadow=True,autopct='%1.1f%%')
    plt.title('Netflix_show TV/Moive percentage')
    plt.axis('equal')
    plt.show()
    return
search_by_data()