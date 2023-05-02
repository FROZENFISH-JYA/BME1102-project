import read_write_csv as rw
import search as se
import datetime
import data_generate as dg
'''先定义一些基础的对日期变换的函数为后面服务'''
#定义函数来获取当日日期
def current_date():
    return datetime.datetime.now().strftime('%Y.%m.%d')

#定义函数获取近3天日期（一个列表）
def three_days_before(date):
    date = datetime.datetime.strptime(date, '%Y.%m.%d')
    before_date1 = date
    before_date2 = date - datetime.timedelta(days=1)
    before_date3 = date - datetime.timedelta(days=2)
    return [before_date1.strftime("%Y.%m.%d"), before_date2.strftime("%Y.%m.%d"),before_date3.strftime("%Y.%m.%d")]

#定义函数获取近5天日期
def five_days_before(date):
    date = datetime.datetime.strptime(date, '%Y.%m.%d')
    before_date1 = date
    before_date2 = date - datetime.timedelta(days=1)
    before_date3 = date - datetime.timedelta(days=2)
    before_date4 = date - datetime.timedelta(days=3)
    before_date5 = date - datetime.timedelta(days=4)

    return [before_date1.strftime("%Y.%m.%d"), before_date2.strftime("%Y.%m.%d"),
        before_date3.strftime("%Y.%m.%d"), before_date4.strftime("%Y.%m.%d"), before_date5.strftime("%Y.%m.%d")]

#定义函数获取30天前的日期
def date_before_30days(given_date):
  given_date = datetime.datetime.strptime(given_date,"%Y.%m.%d")
  before_30_days = given_date - datetime.timedelta(days=30)
  return before_30_days.strftime("%Y.%m.%d")

df_all=rw.ReadCsv()#读取总数据
date_now=current_date()#获取当天日期
'''以下预警的时间均出于准确性和及时性的均衡考量'''
#对一只猫的失踪预警：（3天不出现）
def cat_miss(name):
    date_now = current_date()  # 获取当天日期
    three_dates=three_days_before(date_now)
    k= date_now.split('.')
    three_days_list=[]
    for i in three_dates:#对每天的出现次数查询
        n=se.search_1_date(i)
        three_days_list.append(n)
    if sum(three_days_list)==0:
        return 'missing warning'

#对一只猫的死亡预警：（5天不出现）
def cat_death(name):
    date_now = current_date()  # 获取当天日期
    five_dates=five_days_before(date_now)
    k= date_now.split('.')
    three_days_list=[]
    for i in five_dates:#对每天的出现次数查询
        n=se.search_1_date(i)
        three_days_list.append(n)
    if sum(three_days_list)==0:
        return 'death warning'

#生病预警(出现次数衰减30%以上）
def cat_ill(name):
    date_now = current_date()  # 获取当天日期
    three_dates=three_days_before(date_now)
    k= date_now.split('.')
    three_days_list=[]
    for i in three_dates:
        n=se.search_1_date(i)
        three_days_list.append(n)
    mean_recent=sum(three_days_list)/3#获取3天内猫活动次数的平均值
    date_30days_ago=date_before_30days(date_now)
    last_month=dg.data_generate2(date_30days_ago[:7],name)
    mean_normal=sum(last_month)/len(last_month)
    if (mean_normal-mean_recent)/mean_normal>0.3:#如果活动次数减少30%以上认定为生病预警
        return 'ill warning'

#对小区域而言的危险预警
def area_danger(area):
    date_now = current_date()  # 获取当天日期
    five_dates=five_days_before(date_now)
    k= date_now.split('.')
    five_days_list=[]
    for i in five_dates:
        n=sum(dg.data_generate4(i,area))
        five_days_list.append(n)
    mean_recent=sum(five_days_list)/5#获取5天内该区域猫活动次数的平均值作为近期指标
    date_30days_ago = date_before_30days(date_now)
    last_month = dg.data_generate5(date_30days_ago[:7], area)#获取上个月该区域猫活动次数的平均值作为正常指标
    mean_normal=sum(last_month)/len(last_month)
    if (mean_normal-mean_recent)/mean_normal>0.3:#如果该地点猫活动次数减少30%以上认定为区域危险
       return 'area warning'

