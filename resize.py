import os
from PIL import Image

directory = r'C:\Users\alexi\Desktop\python\Wallpapers\General'
for filename in os.listdir(directory):
    file = directory + "\\" + filename
    image = Image.open(file)
    new_image = image.resize((1920, 1080))
    new_image.save(file)
