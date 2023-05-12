import os
from PIL import Image
 
filename = os.listdir("./custom_dataset/val/class2/")
base_dir = "./custom_dataset/val/class2/"
new_dir  = "./transfer_dataset/val/class2/"
size_m = 32
size_n = 32
 
for img in filename:
    image = Image.open(base_dir + img)
    image_size = image.resize((size_m, size_n),Image.ANTIALIAS)
    image_size.save(new_dir+ img)