import random
import read_write_csv as io
import pandas as pd
import datetime as dt

"""
猫
"""
class cat:
		# 初始化对象
		def __init__(self, name, habitat, liveness):
				self.name = name
				self.habitat = habitat
				self.location = habitat
				self.counter = 0
				self.liveness = liveness
		# 移动到相邻的某个区域
		def move(self):
				self.location = random.sample(adjacent_list[self.habitat - 1], 1)[0]
		# 回到栖息地
		def back(self):
				self.location = self.habitat
		# 出现
		def appear(self, clock):
				# 调用i/o模块,记录这次出现
				str = clock.time.strftime('%Y.%m.%d %H %M')
				str = str.split(' ')
				list = [self.name, f"area{self.location}", str[0], str[1], str[2]]
				io.addCsv(pd.DataFrame([list]))
		def check(self):
				return self.counter < 6
		# 执行模拟过程
		def simulate(self,clock):
				if self.check() == True:
						# 10%几率会移动
						if (random.randint(1,100) <= 10):
								self.move()
						else:
								pass
						# 检查是否处于领地内,更新counter
						if self.location == self.habitat:
								self.counter = 0
						else:
								self.counter += 1
				else:
						self.back()
						self.counter = 0
				# 50%几率会出现并被记录
				if(random.randint(1,100) <= self.liveness):
						self.appear(clock)

"""
世界运行模拟时钟
"""
class clock:
		# 初始化对象
		def __init__(self, date1, date2):
				# 创建时间(同时也是开始时间),即date1 00:00
				start_time = date1
				start_time += ' 00:00'
				self.time = dt.datetime.strptime(start_time, '%Y.%m.%d %H:%M')
				# 创建结束时间,即date2 11:59
				end_time = date2
				end_time += ' 11:59'
				self.time_limit = dt.datetime.strptime(end_time, '%Y.%m.%d %H:%M')
		# 检查是否到达结束时间
		def check(self):
				return self.time <= self.time_limit
		# 模拟时间流动,默认一个时钟tick是十分钟
		def clock_tick(self):
				self.time += dt.timedelta(minutes = 10)

# 区域之间相邻关系
adjacent_list = [[2,3,4,5,6],
								[1,3,4],
								[1,2,5],
								[1,2],
								[1,3,6],
								[1,3,5,7],
								[1,6]]		

# 初始化
"""
通过更改cat类构造函数的第二个参数来设置栖息地(领地),
第三个参数设置活跃度(出现和被记录的倾向性)
"""
cat1 = cat('cat1', 4, 50)
cat2 = cat('cat2', 2, 20)
cat3 = cat('cat3', 3, 10)
cat4 = cat('cat4', 5, 20)
cat5 = cat('cat5', 2, 30)
cat6 = cat('cat6', 1, 20)
cat7 = cat('cat7', 1, 20)
cat8 = cat('cat8', 7, 10)
cat9 = cat('cat9', 6, 60)
cat10 = cat('cat10', 2, 20)
world_clock = clock('2023.1.1','2023.1.20')

while world_clock.check() == True:
		cat1.simulate(world_clock)
		cat2.simulate(world_clock)
		cat3.simulate(world_clock)
		cat4.simulate(world_clock)
		cat5.simulate(world_clock)
		cat6.simulate(world_clock)
		cat7.simulate(world_clock)
		cat8.simulate(world_clock)
		cat9.simulate(world_clock)
		cat10.simulate(world_clock)
		#print(world_clock.time)
		world_clock.clock_tick()