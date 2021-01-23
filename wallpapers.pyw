import ctypes
import os
import time
import datetime as dt

SPI_SETDESKWALLPAPER = 20
directory = r'C:\Users\alexi\Desktop\python\Wallpapers\Day'
while 1:
    time_now = int(dt.datetime.now().strftime("%H"))
    if time_now >= 17 or time_now < 5:
        directory = r'C:\Users\alexi\Desktop\python\Wallpapers\Night'
    if time_now >= 5 and time_now < 17:
        directory = r'C:\Users\alexi\Desktop\python\Wallpapers\Day'


    for filename in os.listdir(directory):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, directory + '\\' + filename , 0)
        time.sleep(1800)
