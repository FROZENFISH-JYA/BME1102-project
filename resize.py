import os
from PIL import Image
 
filename = os.listdir("./image/")
base_dir = "./image/"
new_dir  = "./resized_image/"
size_m = 32
size_n = 32
 
for img in filename:
    image = Image.open(base_dir + img)
    image_size = image.resize((size_m, size_n),Image.ANTIALIAS)
    image_size.save(new_dir+ img)