import pandas as pd
import functools
import csv

#order the dataset by Name
def order_Name(dataframe,flag):
        df_data_order0 = dataframe.sort_values(by=['name'],ascending=[flag])
        return df_data_order0

#order the dataset by Place
def order_Place(dataframe,flag):
        df_data_order0 = dataframe.sort_values(by=['place'],ascending=[flag])
        return df_data_order0

#order the dataset by Hour and Minute
def order_Time(dataframe,flag):
        df_data_order0 = dataframe.sort_values(by=['hour','minute'],ascending=[flag,flag])
        return df_data_order0

#order the dataset by Date
def order_Date(dataframe,flag):
        df_data_order0 = dataframe.sort_values(by=['date'],ascending=[flag])
        return df_data_order0
