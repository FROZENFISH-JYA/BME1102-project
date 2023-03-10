import pandas as pd
'''
data.csv格式:第一行为标签
Name, Place, Month, Date, Hour, Minute
cat1, sist, 11, 2, 12, 30
'''
#参考https://www.cnblogs.com/bonelee/p/9732761.html

#search by name, name is a str
#读取dataframe,返回一个只包含Name标签是name的dataframe
def search_name(dataframe,name):
    '''
    dataframe包含了整个csv的数据
		your job: 1.用df.iterrows()按行读取dataframe
              2.判断row的Name标签值是不是name
              3.将这一行添加到新的frame中 可以通过标签名获取对应的值
              用frame.loc[len(frame.index)] = [value1, value2, value3, ...]向frame新写入一行数据
							4.返回frame
    '''
    frame = pd.DataFrame(columns=['Name', 'Place', 'Month', 'Date', 'Hour', 'Minute']) #initiate the return frame

    
    return frame

#search by Date, Date is a str
def search_Date(dataframe,date):
    frame = pd.DataFrame(columns=['Name', 'Place', 'Month', 'Date', 'Hour', 'Minute'])#initiate the return frame


    return frame

#search by Place, Place is a str
def search_Place(dataframe,place):
    frame = pd.DataFrame(columns=['Name', 'Place', 'Month', 'Date', 'Hour', 'Minute'])#initiate the return frame


    return frame