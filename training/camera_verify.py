import cv2
import time
from PIL import Image
import matplotlib.pyplot as plt
import sys
import os
import pandas as pd

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

import torch,torchvision
import torch.nn as nn
import torchvision.transforms as transforms
import numpy as np
from PIL import Image #读取图片用
import torch.nn.functional as F
import read_write_csv as io
 
#定义模型
class CNNCifar(nn.Module):
		def __init__(self):
				super(CNNCifar,self).__init__()
				self.feature = nn.Sequential(
						nn.Conv2d(3,64,3,padding=2),   nn.BatchNorm2d(64),  nn.ReLU(), nn.MaxPool2d(2,2),
						nn.Conv2d(64,128,3,padding=2), nn.BatchNorm2d(128), nn.ReLU(), nn.MaxPool2d(2,2),
						nn.Conv2d(128,256,3,padding=1),nn.BatchNorm2d(256), nn.ReLU(), nn.MaxPool2d(2,2),
						nn.Conv2d(256,512,3,padding=1),nn.BatchNorm2d(512), nn.ReLU(), nn.MaxPool2d(2,2)
				)
				self.classifier=nn.Sequential(
						nn.Flatten(),
						nn.Linear(2048, 4096),nn.ReLU(),nn.Dropout(0.5),
						nn.Linear(4096,4096), nn.ReLU(),nn.Dropout(0.5),
						nn.Linear(4096,10)
				)
				
		def forward(self, x):
 
				x = self.feature(x)
				output = self.classifier(x)
				return output


# 新分类器
class NewClassifier(nn.Module):
		def __init__(self):
				super(NewClassifier, self).__init__()
				self.fc1 = nn.Linear(2048, 512)
				self.fc2 = nn.Linear(512, 2)
				
				self._init_weights()

		def forward(self, x):
				x = self.fc1(x)
				x = F.relu(x)
				x = self.fc2(x)
				return x

		def _init_weights(self):
			for m in self.modules():
					if isinstance(m, nn.Linear) and m.out_features != 10:
							nn.init.kaiming_normal_(m.weight)
							if m.bias is not None:
									nn.init.constant_(m.bias, 0)
		
# 迁移模型
class CNNtransfer(nn.Module):
		def __init__(self):
				super(CNNtransfer,self).__init__()
				self.feature = nn.Sequential(
						nn.Conv2d(3,64,3,padding=2),   nn.BatchNorm2d(64),  nn.ReLU(), nn.MaxPool2d(2,2),
						nn.Conv2d(64,128,3,padding=2), nn.BatchNorm2d(128), nn.ReLU(), nn.MaxPool2d(2,2),
						nn.Conv2d(128,256,3,padding=1),nn.BatchNorm2d(256), nn.ReLU(), nn.MaxPool2d(2,2),
						nn.Conv2d(256,512,3,padding=1),nn.BatchNorm2d(512), nn.ReLU(), nn.MaxPool2d(2,2)
				)
				self.classifier=NewClassifier()

		def forward(self, x):
				with torch.no_grad():
						x = self.feature(x)
				x = x.view(x.size(0), -1)  
				x = self.classifier(x)     
				return x

#加载模型
net = CNNtransfer()
checkpoint = torch.load('./transfer_CNN_Origi.pth')
net.load_state_dict(checkpoint)

#如果有gpu就使用gpu，否则使用cpu
device = torch.device('cuda'if torch.cuda.is_available() else 'cpu')
net = net.cuda()
net.eval()

size_m = 32
size_n = 32

to_tensor = transforms.Compose([
									transforms.ToTensor(),
									transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])

# 创建摄像头对象
cap = cv2.VideoCapture(0)
start_time = time.time()



while True:
		# 从摄像头读取一帧图像
		ret, frame = cap.read()
		if not ret:
				continue

		# 使用PIL库将图像调整为指定大小
		image = Image.fromarray(frame)
		image_size = image.resize((size_m, size_n), Image.ANTIALIAS)

		# 每十秒读取一次，设置为10秒是为了同步
		if time.time() - start_time >= 10:
				print("start checking current frame")
				start_time = time.time()
				input = image_size
				input = to_tensor(input)
				input = torch.unsqueeze(input, 0) 

				input_=input.cuda()
				outputs =net(input_)
				class_names = ['cat1', 'cat2']
				_, indices = torch.max(outputs,1)
				print(class_names[indices])
			
				current_time = time.localtime(start_time)

				year = current_time.tm_year
				month = current_time.tm_mon
				day = current_time.tm_mday
				hour = current_time.tm_hour
				minute = current_time.tm_min

				date = f"{year}.{month:02d}.{day:02d}"
				hour = f"{hour:02d}"
				minute = f"{minute:02d}"

				# 将读取结果写入数据库
				list = [class_names[indices], f"area3", date, hour, minute]
				io.addCsv(pd.DataFrame([list]))

		# 显示图像
		plt.imshow(frame)
		plt.show(block=False)
		plt.pause(0.01)
		plt.clf()

# 释放摄像头资源
cap.release()
