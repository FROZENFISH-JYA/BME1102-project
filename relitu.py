import pandas as pd

import seaborn as sns

import matplotlib.pyplot as plt

#导入数据并分组

df=pd.read_csv('CSVtest.csv')

#df.columns=['week','hours','counts']

#做成数据透视表

df=pd.pivot_table(df,index='name',columns='place')

print(df)

#画热力图

plt.figure(figsize=(16,8))#画布

ax=sns.heatmap(df,annot=True,fmt='a',cmap='Blues')#annot是显示每个数据，fmt是显示方式
ax.set_xlabel('小时',size=14)#X轴标签
ax.set_ylabel('星期',size=14)#Y轴标签
ax.set_title('客户购买频数图',size=18)#标题

plt.savefig('customers_.png',dpi=1000,bbox_inches='tight')#保存图片
sns.heatmap(df.corr(),cmap="BuGn")
plt.title('Heatmap of Correlation Matrix')