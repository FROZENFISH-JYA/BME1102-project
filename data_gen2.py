import search as s
import datetime as dt
import numpy as np
from matplotlib import pyplot as plt
import read_write_csv as r
import data_generate as dg

#通过调用data_gen1,计算一段日期内每天活动次数的分布
def data_gen2(date1, date2, name):
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

def plot_distribution(X,Y0,Y1):#Y0为平均值，Y为所查值
		fig = plt.figure(figsize=(20,8),dpi=80)
		a,=plt.plot(X, Y0)
		b,=plt.plot(X,Y1)
		plt.legend(handles=[a, b], labels=["average", "date you search"], loc='best')
		plt.ylim((0,10))
		plt.xlabel('hour')
		plt.ylabel('num')
		plt.title('mean distribution during ' + '2023.1.1' + ' and ' + '2023.1.3')
		plt.show()
if __name__=='__main__':
	X = list(range(1,25))
	Y0= data_gen2('2023.1.1','2023.1.3','cat1')
	Y1=dg.data_generate1('2023.1.2','cat1')
	plot_distribution(X,Y0,Y1)
	plt.legend()