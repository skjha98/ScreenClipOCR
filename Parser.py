#Python 3

# Imports
import os, time
import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
import pyscreenshot
from Xlib import display

# Text Parser
def TextParser(x1,y1,x2,y2):
	boxSize = (x1,y1,x2,y2)
	
	# Infinite While Loop
	while 1:
		
		# Grab Image
		img = pyscreenshot.grab(boxSize)
		
		# PreProcess Image
		newSize = tuple(3*x for x in img.size)
		img = img.resize(newSize, Image.ANTIALIAS)
		#img = img.convert("LA")
		#img= img.point(lambda x: 0 if x < 200 else 255)
		
		## ProvidingFilters
		img = img.filter(ImageFilter.SHARPEN)
		img = img.filter(ImageFilter.EDGE_ENHANCE_MORE)
		img = img.filter(ImageFilter.MinFilter(size=3))
		img.show()
		# Parse using Tesseract
		text = pytesseract.image_to_string(img)
		
		# Appending Text
		print(text)
		break

# Taking Coordinates of screen
input("Press Enter for 1st Coordinates")
data1 = display.Display().screen().root.query_pointer()._data
print(data1["root_x"],data1["root_y"])
input("Press Enter for 2nd Coordinates")
data2 = display.Display().screen().root.query_pointer()._data
print(data2["root_x"],data2["root_y"])
TextParser(data1["root_x"],data1["root_y"],data2["root_x"],data2["root_y"])






		




