import search as s
import datetime as dt
import numpy as np
from matplotlib import pyplot as plt
import read_write_csv as r
import data_generate as dg
'''地点相关的柱状图'''
#某地一天每小时
def plot_place_day_bar(area,date):
	Y =dg.data_generate4(date,area)
	print(Y)
	X = list(range(1, len(Y)+1))
	plt.bar(X, Y)
	plt.xlabel('hour')
	plt.ylabel('num')
	plt.title(f'Bar Chart of {area}')
	plt.show()
#某地一月每天
def plot_place_month_bar(area,month):
	Y =dg.data_generate5(month,area)
	print(Y)
	X = list(range(1, len(Y)+1))
	plt.bar(X, Y)
	plt.xlabel('day')
	plt.ylabel('num')
	plt.title(f'Bar Chart of {area}')
	plt.show()

if __name__=='__main__':
	plot_place_month_bar('area1','2023.01')