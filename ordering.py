import pandas as pd
import functools
#参考 https://zhuanlan.zhihu.com/p/456535807


#order the dataset by Date
'''
your job:sort dataframe with .sort_values()
Hint: sort by month and minute

'''
def order_Date(dataframe,flag):
		frame = pd.DataFrame(columns=['Name','Place','Month', 'Date', 'Hour', 'Minute']) #initiate the return frame
		
		return frame

#order the dataset by Time
'''
your job:your job:sort dataframe with .sort_values()
Hint: sort by hour and minute

'''
def order_Time(dataframe,flag):
		frame = pd.DataFrame(columns=['Name', 'Place', 'Month', 'Date', 'Hour', 'Minute']) #initiate the return frame


		return frame

#order the dataset by Date
'''
your job:your job:sort dataframe with .sort_values()
Hint: sort by name(alphabetical order)

'''
def order_Place(dataframe,flag):
		frame = pd.DataFrame(columns=['Name', 'Place', 'Month', 'Date', 'Hour', 'Minute']) #initiate the return frame


		return frame

#order the dataset by Date
'''
your job:sort dataframe with .sort_values()
Hint: sort by name(alphabetical order)

'''
def order_Name(dataframe,flag):
		frame = pd.DataFrame(columns=['Name', 'Place', 'Month', 'Date', 'Hour', 'Minute']) #initiate the return frame


		return frame