from ctypes import WinDLL, create_unicode_buffer, windll
import random
import os


os.chdir("C:/SwitchBackgrounds/Pictures/")
pictureList = os.listdir()

SPI_GETDESKWALLPAPER = 0x0073
dll = WinDLL('user32')
ubuf = create_unicode_buffer(200)
dll.SystemParametersInfoW(SPI_GETDESKWALLPAPER,200,ubuf,0)

newBackground = "C:/SwitchBackgrounds/Pictures/" + random.choice(pictureList)

while (newBackground == ubuf.value):
    newBackground = "C:/SwitchBackgrounds/Pictures/" + random.choice(pictureList)

windll.user32.SystemParametersInfoW(20, 0, newBackground, 0)