import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QScrollArea, QLabel, QWidget, QVBoxLayout, QFrame, QGraphicsScene, QGraphicsView, QSizePolicy, QLineEdit
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
import data_generate

class MyMainWindow(QMainWindow):
		def __init__(self):
				super().__init__()
				# 加载UI文件
				loadUi("a.ui", self)

				# 找到第一个按钮
				self.push_button1 = self.findChild(QPushButton, "push1")
				# 关联函数
				self.push_button1.clicked.connect(self.on_push_button1_clicked)

				# 找到滚动区域1
				scrollArea = self.findChild(QScrollArea, 'scrollArea')
				self.scroll_area = scrollArea

				# 找到滚动区域2
				scrollArea2 = self.findChild(QScrollArea, 'scrollArea2')
				self.scroll_area2 = scrollArea2
				scrollAreaWidgetContents2 = self.findChild(QWidget, 'scrollAreaWidgetContents2')

				# 从csv读取所有数据
				data = io.ReadCsv()
				self.update_time_label()
				time = self.time_label.text()
				date = time.split(" ")[0]
				searched_data = search.search_date(dataframe = data, date = date)
						
				# 找到滚动条区域放置内容
				scrollAreaWidgetContents = self.findChild(QWidget, 'scrollAreaWidgetContents')
				self.scrollAreaWidgetContents = scrollAreaWidgetContents
				scrollAreaWidgetContents.setStyleSheet("background-color: white;")
						
				# 创建用于放置刚才找到的滚动条区域的layout
				layout = QVBoxLayout(scrollAreaWidgetContents)
				self.layout = layout
				

				# 在所有数据之前先添加列名
				label = QLabel(', '.join(searched_data.columns.tolist()))
				layout.addWidget(label)

				# 列名后添加分割线
				line = QFrame()
				line.setFrameShape(QFrame.HLine)
				line.setFrameShadow(QFrame.Sunken)
				layout.addWidget(line)

				for index, row in searched_data.iterrows():
						# 每行都创建一个qlabel，依次放置name、place等数据
						label = QLabel(', '.join([row['name'], row['place'], row['date'], str(row['hour']), str(row['minute'])]))
								
						# 每行都添加分割线
						line = QFrame()
						line.setFrameShape(QFrame.HLine)
						line.setFrameShadow(QFrame.Sunken)

						# 将刚才创建的qlabel添加到layout显示
						layout.addWidget(label)
						layout.addWidget(line)

				# 为刚才的layout设置滚动条
				scrollAreaWidgetContents.setLayout(layout)


				# 创建第二个带滚动条的区域layout
				layout2 = QVBoxLayout(scrollAreaWidgetContents2)
				self.layout2 = layout2
				# 逐行添加内容
				with open('alarm_report.txt', 'r') as f:
						for line in f:
								label = QLabel(line.strip(), scrollAreaWidgetContents2)
								#  每行添加分割线
								line = QFrame()
								line.setFrameShape(QFrame.HLine)
								line.setFrameShadow(QFrame.Sunken)
								# 这一行添加到layout显示
								layout2.addWidget(label)
								layout2.addWidget(line)
				# 为layout设置滚动条
				scrollAreaWidgetContents2.setLayout(layout2)
								
								
		
				# 在 QGraphicsView 中展示 matplotlib 绘制的图形
				matrix = heatmap.get_matrix(date,date)
				fig, (ax1, ax2) = plt.subplots(2,1) 	
				fig.set_size_inches(7.5, 12)
				heatmap.heat_map_for_ui(matrix, fig, ax1)
				pie_chart.pie_chart_for_ui(date, fig, ax2)
				
				# 使用canvas在一块区域展示两张图像
				canvas = FigureCanvas(fig)
				canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
				canvas.updateGeometry()
				scene = QGraphicsScene()
				scene.addWidget(canvas)
				graphics_view = self.findChild(QGraphicsView, 'graphicsView')
				self.graphics_view = graphics_view
				graphics_view.setScene(scene)

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

				self.push_button2 = self.findChild(QPushButton, "push2")
				self.push_button2.clicked.connect(self.on_push_button2_clicked)

				self.push_button3 = self.findChild(QPushButton, "push3")
				self.push_button3.clicked.connect(self.on_push_button3_clicked)

		def on_push_button1_clicked(self):
				pass
		
		def on_push_button2_clicked(self):
				self.newWindow1 = NewWindow1()
				self.newWindow1.show()
		
		def on_push_button3_clicked(self):
				self.newWindow2 = NewWindow2()
				self.newWindow2.show()
		
		def update_time_label(self):
			# 获取当前时间并设置为时间标签的文本
			current_time = QDateTime.currentDateTime().toString("yyyy.MM.dd hh:mm:ss")
			self.time_label.setText(current_time)

# 子窗口的行为
class NewWindow1(QWidget):
		def __init__(self):
				super().__init__()
				loadUi("b.ui", self)

				self.line_edit1 = self.findChild(QLineEdit, "lineEdit1")
				self.line_edit2 = self.findChild(QLineEdit, "lineEdit2")

				self.label = self.findChild(QLabel, "label_4")
				self.label.setStyleSheet("background-color: white; border: 1px solid gray;")

				self.push_button4 = self.findChild(QPushButton, "push4")
				self.push_button4.clicked.connect(self.on_push_button4_clicked)

				self.scroll_area2 = self.findChild(QScrollArea, 'scrollArea3')
				
				self.graphics_view2 = self.findChild(QGraphicsView, 'graphicsView2')
				self.graphics_view3 = self.findChild(QGraphicsView, 'graphicsView3')

				self.scrollAreaWidgetContents3 = self.findChild(QWidget, 'scrollAreaWidgetContents3')
				self.scrollAreaWidgetContents3.setStyleSheet("background-color: white;")

				# 创建 QVBoxLayout 用于放置 QLabel
				self.layout = QVBoxLayout()

				# 将 QVBoxLayout 设置为带滚动条的区域的布局
				self.scrollAreaWidgetContents3.setLayout(self.layout)


		def on_push_button4_clicked(self):
				for i in reversed(range(self.layout.count())): 
						self.layout.itemAt(i).widget().setParent(None)
				text1 = self.line_edit1.text()
				text2 = self.line_edit2.text()
				raw_data = io.ReadCsv()
				data_date = search.search_date(raw_data, text2)
				data_date_name = search.search_Name(data_date, text1)
				print("done")
				
				layout = self.layout

				self.label.setText("normal_situation")

				# 在第一行添加列名
				label = QLabel(', '.join(data_date_name.columns.tolist()))
				layout.addWidget(label)

				# 添加分割线
				line = QFrame()
				line.setFrameShape(QFrame.HLine)
				line.setFrameShadow(QFrame.Sunken)
				layout.addWidget(line)

				for index, row in data_date_name.iterrows():
						# 创建一个 QLabel 来展示 DataFrame 中的一行数据
						label = QLabel(', '.join([row['name'], row['place'], row['date'], str(row['hour']), str(row['minute'])]))
								
						# 添加分割线
						line = QFrame()
						line.setFrameShape(QFrame.HLine)
						line.setFrameShadow(QFrame.Sunken)

						# 将 QLabel 添加到 QVBoxLayout 中
						layout.addWidget(label)
						layout.addWidget(line)
					
				
				

				# 在 QGraphicsView 中展示 matplotlib 绘制的图形
				fig, ax = plt.subplots(1,1) 	
				fig.set_size_inches(5.5, 4) # 设置图像尺寸
				heatmap.heatmap_cat(data_date_name, fig, ax)
				
				canvas = FigureCanvas(fig) # 将subplot转换成FigureCanvas
				canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
				canvas.updateGeometry()
				scene = QGraphicsScene()
				scene.addWidget(canvas)
				
				self.graphics_view2.setScene(scene)

				# 折线图
				fig2, ax2 = plt.subplots(1,1) 	
				fig2.set_size_inches(5.5, 4) # 设置图像尺寸

				data_generate.data_generate1_ui(data_date_name, fig2, ax2)
				canvas2 = FigureCanvas(fig2) # 将subplot转换成FigureCanvas
				canvas2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
				canvas2.updateGeometry()
				scene = QGraphicsScene()
				scene.addWidget(canvas2)
				self.graphics_view3.setScene(scene)


				return

# 第二个子窗口的行为				
class NewWindow2(QWidget):
		def __init__(self):
				super().__init__()
				loadUi("c.ui", self)
				self.line_edit1 = self.findChild(QLineEdit, "lineEdit1")
				self.line_edit2 = self.findChild(QLineEdit, "lineEdit2")
				self.push_button4 = self.findChild(QPushButton, "push4")
				self.push_button4.clicked.connect(self.on_push_button4_clicked)

				self.scroll_area2 = self.findChild(QScrollArea, 'scrollArea3')
				# 找到带滚动条的区域并设置其背景颜色为白色
				
				self.graphics_view2 = self.findChild(QGraphicsView, 'graphicsView2')
				self.graphics_view3 = self.findChild(QGraphicsView, 'graphicsView3')

				self.scrollAreaWidgetContents3 = self.findChild(QWidget, 'scrollAreaWidgetContents3')
				self.scrollAreaWidgetContents3.setStyleSheet("background-color: white;")

				# 创建 QVBoxLayout 用于放置 QLabel
				self.layout = QVBoxLayout()

				# 将 QVBoxLayout 设置为带滚动条的区域的布局
				self.scrollAreaWidgetContents3.setLayout(self.layout)

		def on_push_button4_clicked(self):
				for i in reversed(range(self.layout.count())): 
						self.layout.itemAt(i).widget().setParent(None)
				text1 = self.line_edit1.text()
				text2 = self.line_edit2.text()
				raw_data = io.ReadCsv()
				data_date = search.search_date(raw_data, text2)
				data_date_place = search.search_Place(data_date, text1)
				print("done")
				
				layout = self.layout

				# 在第一行添加列名
				label = QLabel(', '.join(data_date_place.columns.tolist()))
				layout.addWidget(label)

				# 添加分割线
				line = QFrame()
				line.setFrameShape(QFrame.HLine)
				line.setFrameShadow(QFrame.Sunken)
				layout.addWidget(line)

				for index, row in data_date_place.iterrows():
						# 创建一个 QLabel 来展示 DataFrame 中的一行数据
						label = QLabel(', '.join([row['name'], row['place'], row['date'], str(row['hour']), str(row['minute'])]))
								
						# 添加分割线
						line = QFrame()
						line.setFrameShape(QFrame.HLine)
						line.setFrameShadow(QFrame.Sunken)

						# 将 QLabel 添加到 QVBoxLayout 中
						layout.addWidget(label)
						layout.addWidget(line)
				
				
				

				# 在 QGraphicsView 中展示 matplotlib 绘制的图形
				fig, ax = plt.subplots(1,1) 	
				fig.set_size_inches(5.5, 4) # 设置图像尺寸
				pie_chart.area_bar_chart(data_date_place, fig, ax)
				
				canvas = FigureCanvas(fig) # 将subplot转换成FigureCanvas
				canvas.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
				canvas.updateGeometry()
				scene = QGraphicsScene()
				scene.addWidget(canvas)
				
				self.graphics_view2.setScene(scene)

				# 饼图
				fig2, ax2 = plt.subplots(1,1) 	
				fig2.set_size_inches(5.5, 4) # 设置图像尺寸

				pie_chart.area_pie_chart(data_date_place, fig2, ax2)
				canvas2 = FigureCanvas(fig2) # 将subplot转换成FigureCanvas
				canvas2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
				canvas2.updateGeometry()
				scene = QGraphicsScene()
				scene.addWidget(canvas2)
				self.graphics_view3.setScene(scene)


				return

if __name__ == '__main__':
		app = QApplication(sys.argv)
		mainWindow = MyMainWindow()
		mainWindow.show()
		sys.exit(app.exec_())
