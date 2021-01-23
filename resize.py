import os
from PIL import Image

directory = r'C:\Users\[USER]\Desktop\python\Wallpapers\Day'
for filename in os.listdir(directory):
    file = directory + "\\" + filename
    image = Image.open(file)
    new_image = image.resize((1920, 1080))
    new_image.save(file)

directory = r'C:\Users\[USER]\Desktop\python\Wallpapers\Night'
for filename in os.listdir(directory):
    file = directory + "\\" + filename
    image = Image.open(file)
    new_image = image.resize((1920, 1080))
    new_image.save(file)
