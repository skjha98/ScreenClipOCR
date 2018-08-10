import os
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import pyscreenshot as ImageGrab

#Getting Image Snap

#Windows
#import pyautogui
#print(pyautogui.displayMousePosition())

#Linux
from Xlib import display
## 1st Pointer
input("Press Enter for 1st Coordinate:")
data = display.Display().screen().root.query_pointer()._data
x1,y1 = data["root_x"], data["root_y"]
## 2nd Pointer
input("Press Enter for 2nd Coordinate:")
data = display.Display().screen().root.query_pointer()._data
x2,y2 = data["root_x"], data["root_y"]

img = ImageGrab.grab(bbox=(x1,y1,x2,y2))


#Preprocessing
new_size = tuple(3*x for x in img.size)
img = img.resize(new_size, Image.ANTIALIAS)
## Providing Filters
img = img.filter(ImageFilter.SHARPEN)
img = img.filter(ImageFilter.MinFilter(size=3))


#img = img.convert('L')
#img = img.filter(ImageFilter.EDGE_ENHANCE_MORE())
#img= img.point(lambda x: 0 if x < 140 else 255)

#img.show()


#Showing Text
text = pytesseract.image_to_string(img)
os.system("clear")
print(text)
