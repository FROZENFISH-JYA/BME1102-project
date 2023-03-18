import pandas as pd
import functools
import csv



#order the dataset by Name
def order_Time(dataframe,path):
        dataframe=[]
        df = pd.read_csv(path) 
        df_data_order0 = df.sort_values(by=['Name'],ascending=[True])
        return df

#order the dataset by Place
def order_Time(dataframe,flag,path):
        
        frame = pd.DataFrame(dataframe,columns=['Name', 'Place', 'Date', 'Hour', 'Minute']) #initiate the return frame
        for i in frame['Place']:
            i=i.lower()
        df_data_order0 = frame.sort_values(by=['Place'],ascending=[True])
        return frame

#order the dataset by Date
def order_Name(dataframe,flag,path):
        frame = pd.DataFrame(dataframe,columns=['Name', 'Place', 'Date', 'Hour', 'Minute']) #initiate the return frame
        df_data_order0 = frame.sort_values(by=['Place'],ascending=[True])
        return frame

#order the dataset by Hour and Minute
def order_Place(dataframe,flag,path):
        frame = pd.DataFrame(dataframe,columns=['Name', 'Place', 'Date', 'Hour', 'Minute']) #initiate the return frame

        df_data_order0 = frame.sort_values(by=['Hour','Minute'],ascending=[True,True])
        return frame

#order the dataset by Date
def order_Name(dataframe,flag,path):
        frame = pd.DataFrame(dataframe,columns=['Name', 'Place', 'Date', 'Hour', 'Minute']) #initiate the return frame
        return frame
