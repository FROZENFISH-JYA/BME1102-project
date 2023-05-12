import torch,torchvision
import torch.nn as nn
import torchvision.transforms as transforms
import numpy as np
from PIL import Image #读取图片用
import torch.nn.functional as F
 
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



#加载模型
net = CNNCifar()
checkpoint = torch.load('./models/40/CNN_Origi.pth')
net.load_state_dict(checkpoint)

#如果有gpu就使用gpu，否则使用cpu
device = torch.device('cuda'if torch.cuda.is_available() else 'cpu')
net = net.cuda()
net.eval()


img_path = './resized_image/bailing.jpg'
img = Image.open(img_path)
img = np.array(img)


to_tensor = transforms.Compose([
                transforms.ToTensor(),
                transforms.Normalize((0.485, 0.456, 0.406), (0.229, 0.224, 0.225))])
img = to_tensor(img)
img = torch.unsqueeze(img, 0) #给最高位添加一个维度，也就是batchsize的大小

img_=img.cuda()
outputs =net(img_)


class_names = ['Airplane', 'Automobile', 'Bird', 'Cat', 'Deer', 'Dog', 'Frog', 'Horse', 'Ship', 'Truck']
_, indices = torch.max(outputs,1)
percentage = torch.nn.functional.softmax(outputs, dim=1)[0] * 100
perc = percentage[int(indices)].item()
result = class_names[indices]
print('predicted:', result)





