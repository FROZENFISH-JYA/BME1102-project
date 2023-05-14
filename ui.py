import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QScrollArea, QLabel, QWidget, QVBoxLayout, QFrame, QGraphicsScene, QGraphicsView, QSizePolicy
import csv
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from PyQt5.uic import loadUi
from PyQt5.QtCore import QDateTime, QTimer
from PyQt5.QtCore import Qt

import heatmap
import pie_chart
import read_write_csv as io
import search

class MyMainWindow(QMainWindow):
		def __init__(self):
				super().__init__()
				# 加载UI文件
				loadUi("a.ui", self)
				# 获取QPushButton对象
				self.push_button = self.findChild(QPushButton, "push")
				# 连接信号和槽函数
				self.push_button.clicked.connect(self.on_push_button_clicked)
				scrollArea = self.findChild(QScrollArea, 'scrollArea')
				self.scroll_area = scrollArea
				
				# data = io.ReadCsv()
				# searched_data = search.search_date(dataframe = data, date = '2023.01.01')
						
				# # 找到带滚动条的区域并设置其背景颜色为白色
				# scrollAreaWidgetContents = self.findChild(QWidget, 'scrollAreaWidgetContents')
				# self.scrollAreaWidgetContents = scrollAreaWidgetContents
				# scrollAreaWidgetContents.setStyleSheet("background-color: white;")
						
				# # 创建 QVBoxLayout 用于放置 QLabel
				# layout = QVBoxLayout(scrollAreaWidgetContents)
				# self.layout = layout
				

				# # 在第一行添加列名
				# label = QLabel(', '.join(searched_data.columns.tolist()))
				# layout.addWidget(label)

				# # 添加分割线
				# line = QFrame()
				# line.setFrameShape(QFrame.HLine)
				# line.setFrameShadow(QFrame.Sunken)
				# layout.addWidget(line)

				# for index, row in searched_data.iterrows():
				# 	# 创建一个 QLabel 来展示 DataFrame 中的一行数据
				# 	label = QLabel(', '.join([row['name'], row['place'], row['date'], str(row['hour']), str(row['minute'])]))
							
				# 	# 添加分割线
				# 	line = QFrame()
				# 	line.setFrameShape(QFrame.HLine)
				# 	line.setFrameShadow(QFrame.Sunken)

				# 	# 将 QLabel 添加到 QVBoxLayout 中
				# 	layout.addWidget(label)
				# 	layout.addWidget(line)

				# # 将 QVBoxLayout 设置为带滚动条的区域的布局
				# scrollAreaWidgetContents.setLayout(layout)

				# # 在 QGraphicsView 中展示 matplotlib 绘制的图形
				# matrix = heatmap.get_matrix('2023.1.1','2023.1.2')
				# fig, (ax1, ax2) = plt.subplots(2,1) 	
				# fig.set_size_inches(7.5, 12) # 设置图像尺寸
				# heatmap.heat_map_for_ui(matrix, fig, ax1)
				# pie_chart.pie_chart_for_ui('2023.1.1', fig, ax2)
				
				# canvas = FigureCanvas(fig) # 将subplot转换成FigureCanvas
				# canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
				# canvas.updateGeometry()
				# scene = QGraphicsScene()
				# scene.addWidget(canvas)
				# graphics_view = self.findChild(QGraphicsView, 'graphicsView')
				# self.graphics_view = graphics_view
				# graphics_view.setScene(scene)
				  # 添加一个时间标签

				frame =  self.findChild(QFrame, "frame")
				frame.setStyleSheet("background-color: white; border: 1px solid gray;")

				self.time_label = self.findChild(QLabel, "time_label")
				self.time_label.setStyleSheet("border: none;")
				self.time_label.setAlignment(Qt.AlignCenter)
				frame_layout = QVBoxLayout(frame)
				frame_layout.addWidget(self.time_label)

				# 创建一个定时器，每秒钟更新一次时间标签的文本
				self.timer = QTimer(self)
				self.timer.timeout.connect(self.update_time_label)
				self.timer.start(1000)

		def on_push_button_clicked(self):
				# 在这里编写按钮点击后的行为
				print("按钮被点击了！")
				# 刷新图像
				self.refresh_image()

				# 刷新QScrollArea
				self.scroll_area.viewport().update()
				
				# 刷新QGraphicsView
				self.graphics_view.viewport().update()
		
		def update_time_label(self):
			# 获取当前时间并设置为时间标签的文本
			current_time = QDateTime.currentDateTime().toString("yyyy-MM-dd hh:mm:ss")
			self.time_label.setText(current_time)
		
		def refresh_image(self):
				with open('CSVtest.csv') as csvfile:
						reader = csv.reader(csvfile)
						
						# 找到带滚动条的区域并设置其背景颜色为白色
						self.scrollAreaWidgetContents.setStyleSheet("background-color: white;")
						
						# 创建 QVBoxLayout 用于放置 QLabel
						layout = self.layout
						
						
						for row in reader:
								# 创建一个 QLabel 来展示 CSV 文件中的一行数据
								label = QLabel(', '.join(row))
								
								# 添加分割线
								line = QFrame()
								line.setFrameShape(QFrame.HLine)
								line.setFrameShadow(QFrame.Sunken)

								# 将 QLabel 添加到 QVBoxLayout 中
								layout.addWidget(label)
								layout.addWidget(line)

						# 将 QVBoxLayout 设置为带滚动条的区域的布局
						self.scrollAreaWidgetContents.setLayout(layout)

				# 在 QGraphicsView 中展示 matplotlib 绘制的图形
				matrix = heatmap.get_matrix('2023.1.1','2023.1.2')
				fig, (ax1, ax2) = plt.subplots(2,1) 	
				fig.set_size_inches(7.5, 12) # 设置图像尺寸
				heatmap.heat_map_for_ui(matrix, fig, ax1)
				pie_chart.pie_chart_for_ui('2023.1.1', fig, ax2)
				
				canvas = FigureCanvas(fig) # 将subplot转换成FigureCanvas
				canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
				canvas.updateGeometry()
				scene = QGraphicsScene()
				scene.addWidget(canvas)
				graphics_view = self.findChild(QGraphicsView, 'graphicsView')
				graphics_view.setScene(scene)

if __name__ == '__main__':
		app = QApplication(sys.argv)
		mainWindow = MyMainWindow()
		mainWindow.show()
		sys.exit(app.exec_())
