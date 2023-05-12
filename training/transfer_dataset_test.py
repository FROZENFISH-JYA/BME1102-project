import torch
import torchvision.transforms as transforms
from torchvision.datasets import ImageFolder
from matplotlib import pyplot as plt


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


# # 打印并检验数据是否正确导入
# for data, target in train_loader:
#     for i in range(len(data)):
#         print(target[i])
#         plt.imshow(data[i].permute(1, 2, 0))
#         plt.show()



