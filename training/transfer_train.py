import torch,torchvision
import torch.nn as nn
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
import torch.nn.functional as F
from matplotlib import pyplot as plt


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
				with torch.no_grad():
						x = self.feature(x)
				output = self.classifier(x)
				return output
		

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
				

checkpoint = torch.load('./models/CNN_Origi.pth')
pretrained_dict = checkpoint['model']
net = CNNtransfer()
net_dict = net.state_dict()
pretrained_dict = {k: v for k, v in pretrained_dict.items() if k in net_dict}
net_dict.update(pretrained_dict)
net.load_state_dict(net_dict)
# net = CNNCifar()
# print(net)
# checkpoint = torch.load('./models/40/CNN_Origi.pth')
# net.load_state_dict(checkpoint)


train_dir = "./transfer_dataset/train/"
val_dir = "./transfer_dataset/val/"

# 定义对数据的预处理
train_transform = transforms.Compose([
		transforms.RandomHorizontalFlip(),
		transforms.ToTensor(),
		transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
])

val_transform = transforms.Compose([
		transforms.Resize((32, 32)),
		transforms.ToTensor(),
		transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))
])

# 导入数据集
train_dataset = ImageFolder(root=train_dir, transform=train_transform)
val_dataset = ImageFolder(root=val_dir, transform=val_transform)

# 定义数据加载器
train_loader = torch.utils.data.DataLoader(train_dataset, batch_size=4, shuffle=True)
val_loader = torch.utils.data.DataLoader(val_dataset, batch_size=4, shuffle=False)

#定义损失函数和优化器
criterion = torch.nn.CrossEntropyLoss()
optimizer = torch.optim.Adam(net.parameters(), lr=0.001,weight_decay=5e-4)
 
#如果有gpu就使用gpu，否则使用cpu
device = torch.device('cuda'if torch.cuda.is_available() else 'cpu')
net = net.to(device)


#训练模型
print('training on: ',device)
def test(test_accuracy, test_loss): 
	net.eval()
	acc = 0.0
	sum = 0.0
	loss_sum = 0
	for batch, (data, target) in enumerate(val_loader):
		data, target = data.to(device), target.to(device)
		output = net(data)
		loss = criterion(output, target)
		acc+=torch.sum(torch.argmax(output,dim=1)==target).item()
		sum+=len(target)
		loss_sum+=loss.item()
	# 记录准确率和损失
	test_accuracy.append(100*acc/sum)
	test_loss.append(loss_sum/(batch+1))
	print('test  acc: %.2f%%, loss: %.4f'%(100*acc/sum, loss_sum/(batch+1)))
 
def train(train_accuracy, train_loss): 
	net.train()
	acc = 0.0
	sum = 0.0
	loss_sum = 0
	for batch, (data, target) in enumerate(train_loader):
		data, target = data.to(device), target.to(device)
		optimizer.zero_grad()
		output = net(data)
		loss = criterion(output, target)
		loss.backward()
		optimizer.step()
		
		acc +=torch.sum(torch.argmax(output,dim=1)==target).item()
		sum+=len(target)
		loss_sum+=loss.item()
		
		if batch%10==0:
			print('\tbatch: %d, loss: %.4f'%(batch, loss.item()))
	# 记录准确率和损失
	train_accuracy.append(100*acc/sum)
	train_loss.append(loss_sum/(batch+1))
	print('train acc: %.2f%%, loss: %.4f'%(100*acc/sum, loss_sum/(batch+1)))

def save():
	torch.save(net.state_dict(),'transfer_CNN_Origi.pth')
	torch.save(net,'transfer_CNN_all.pth')
 

train_accuracy = []
train_loss = []
test_accuracy = []
test_loss = []
for epoch in range(10):
	print('epoch: %d'%epoch)
	train(train_accuracy, train_loss)
	test(test_accuracy, test_loss)
	save()

fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 5))
ax1.plot(train_accuracy)
ax1.plot(test_accuracy)
ax1.legend(['train', 'test'])
ax1.set_title('Accuracy')
ax1.set_xlabel('Epochs')
ax1.set_ylabel('Accuracy')

ax2.plot(train_loss)
ax2.plot(test_loss)
ax2.legend(['train', 'test'])
ax2.set_title('Loss')
ax2.set_xlabel('Epochs')
ax2.set_ylabel('Loss')

plt.show()