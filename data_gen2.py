import search as s
import datetime as dt
import numpy as np
from matplotlib import pyplot as plt


#通过调用data_gen1,计算一段日期内每天活动次数的分布
def data_gen2(date1, date2, dataframe, name):
		date1=dt.datetime.strptime(date1,"%Y.%m.%d").date()
		date2=dt.datetime.strptime(date2,"%Y.%m.%d").date()
		#日期上限
		date2=date2+dt.timedelta(days = 1)
		distribution_sum = np.zeros(24)
		#计算这段时间的天数
		days=(date2-date1).days
		#遍历时间区间内的每一天
		while date1 != date2:
				distribution = data_gen1(date, name, dataframe)
				distribution_sum += np.array(distribution)
				#日期加一
				date1=date1+dt.timedelta(days = 1)
		distribution_mean = distribution_sum / days
		return distribution_mean 

def plot_distribution(X,Y):
		fig = plt.figure(figsize=(20,8),dpi=80)
		plt.plot(X, Y)
		plt.ylim((0,10))
		plt.xlabel('hour')
		plt.ylabel('num')
		plt.title('mean distribution during ' + '2023.1.1' + ' and ' + '2023.1.3')
		plt.show()

X = list(range(1,25))
Y = [0] * 24
plot_distribution(X,Y)