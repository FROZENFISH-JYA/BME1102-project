import search as s
import datetime as dt
import numpy as np
from matplotlib import pyplot as plt
import read_write_csv as r
import data_generate as dg

'''先定义两个对数据预处理的函数'''
#通过调用data_gen1,计算一段日期内每天活动次数的分布
def data_gen2(date1, date2, name):#输入起始日期date1,结束日期date2
		date1=dt.datetime.strptime(date1,"%Y.%m.%d").date()
		date2=dt.datetime.strptime(date2,"%Y.%m.%d").date()
		#日期上限
		date2=date2+dt.timedelta(days = 1)
		distribution_sum = np.zeros(24)
		#计算这段时间的天数
		days=(date2-date1).days
		dataframe = r.ReadCsv()
		#遍历时间区间内的每一天
		while date1 != date2:
				str = date1.strftime('%Y.%m.%d')
				distribution = dg.data_generate1(str, name)
				distribution_sum += np.array(distribution)
				#日期加一
				date1=date1+dt.timedelta(days = 1)
		distribution_mean = distribution_sum / days
		return distribution_mean 
#获取某日期前多少天的日期
def date_before(date,days):#date为起始日期，days为多少天前
	date_list = date.split('.')
	year = int(date_list[0])
	month = int(date_list[1])
	day = int(date_list[2])
	date_days_ago = dt.datetime(year, month, day) - dt.timedelta(days=days)#日期减法
	date_days_ago = date_days_ago.strftime('%Y.%m.%d')
	return date_days_ago

'''以下为画图的函数'''
def plot_day_distribution(date,name):#Y0为平均值，Y为所查值
		X = list(range(1, 25))#一天24小时
		#获取前30天的起始和终止日期
		start_date=date_before(date,30)
		end_date=date_before(date,1)
		Y0 = data_gen2(start_date, end_date, name)#一段时间内的平均情况
		Y1 = dg.data_generate1(date, name)#所查日期情况
		fig = plt.figure(figsize=(20,8),dpi=80)
		a,=plt.plot(X, Y0)#画平均情况
		b,=plt.plot(X,Y1)#画所查情况
		plt.legend(handles=[a, b], labels=["average", "date you search"], loc='best')#画图例
		plt.ylim((0,10))
		plt.xlabel('hour')
		plt.ylabel('num')
		plt.title(f'mean distribution during " {start_date} and  {end_date}')
		plt.show()

#某个月每天折线图
def plot_month_distribution(month,name):#输入月份（如“2023.1“），和猫的名字
	Y = dg.data_generate2(month, name)  # 获取所查日期数据
	X = list(range(1, len(Y)+1))
	plt.plot(X, Y)  # 画
	plt.xlabel('day')
	plt.ylabel('num')
	plt.title(f'month distribution of {name} ')
	plt.show()
#某年每月折线图
def plot_year_distribution(year,name):#输入年份（如“2023”），和猫的名字
	Y = dg.data_generate3(year, name)  # 获取所查日期数据
	X = list(range(1, len(Y)+1))
	plt.plot(X, Y)  # 画
	plt.xlabel('month')
	plt.ylabel('num')
	plt.title(f'year distribution of {name} ')
	plt.show()

if __name__=='__main__':
	plot_year_distribution('2023', 'cat1')