import seaborn as sns
import matplotlib.cm
import matplotlib.image as mpimg
import numpy as np
import search as s
import read_write_csv as rw

def Normalize(data):
    m = np.mean(data)
    mx = max(data)
    mn = min(data)
    return [(float(i) - m) / (mx - mn) for i in data]

"""
从数据库中检索指定日期区间内的记录,并统计每个区域的热度
返回一个矩阵
"""
def get_matrix(date1,date2):
		matrix = np.zeros((30,30))
		masks = []
		# 载入每个区域的mask
		masks.append(np.genfromtxt("./masks/mask1.csv", delimiter=','))
		masks.append(np.genfromtxt("./masks/mask2.csv", delimiter=','))
		masks.append(np.genfromtxt("./masks/mask3.csv", delimiter=','))
		masks.append(np.genfromtxt("./masks/mask4.csv", delimiter=','))
		masks.append(np.genfromtxt("./masks/mask5.csv", delimiter=','))
		masks.append(np.genfromtxt("./masks/mask6.csv", delimiter=','))
		masks.append(np.genfromtxt("./masks/mask7.csv", delimiter=','))
		 # 读取原始数据
		df = rw.ReadCsv()
		# 截取date1和date2间的记录
		df = s.search_Date(df,date1,date2)
		# 对每个地点做名称检索，统计其出现次数
		list = []
		for a in range(1,8):
			place = 'area' + str(a)
			df1 = s.search_Place(df, place)
			matrix += df1.shape[0] * masks[a-1]
		# 做归一化处理并返回
		return (matrix-np.min(matrix))/(np.max(matrix)-np.min(matrix))

"""
绘制热力图
输入参数: matrix(30*30)
"""
def heat_map(matrix):
		map_img = mpimg.imread('map_shanghaitech.jpg') 
		heatmap_data = matrix
		sns.set_context({"figure.figsize":(30,30)}) 	
		hmax = sns.heatmap(heatmap_data,
								alpha = 0.5, # 透明度
								annot = False,
								zorder = 2,
								cmap="OrRd"
								)

		hmax.imshow(map_img,
							aspect = hmax.get_aspect(),
							extent = hmax.get_xlim() + hmax.get_ylim(),
							zorder = 1) # 将背景叠放在热力图下方

		from matplotlib.pyplot import show 
		show()


# matrix = get_matrix('2023.1.1','2023.1.2')
# heat_map(matrix)