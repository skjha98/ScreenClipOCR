# ScreenClipOCR
This is just an implementtion of Tesseract-OCR with Screen Clipping
This is an Python file made just to clip the image containing the code in the image on the web (Usually for the online C program MCQ).

## Objectives
### 1. Parser.py : 
This file prints the text and parses the image using 5 preprocessing ideas. First, scales the size by 3x. Second, Antilias the image, Sharpens the image, Enhances the edges of the text in the image, and then applying the minfilter of size 3. After the preprocessing the image, it will pass it to Tesseract-OCR. Accuracy depends upon the size and the background of the text.

### 2. Tesseract.py:
This file prints the text and parses the image using 4 preprocessing ideas. First, scales the size by 3x. Second, Antilias the image, Sharpens the image, and then Applying the minfilter of size 3. After the preprocessing the image, it will pass it to Tesseract-OCR. Accuracy depends upon the size and the background of the text.


## Accuracy
Parser.py > Tesseract.py


## Requirements
pytesseract
PIL
pyscreenshot


## Method
1. Install all the requirements:
    pip install pytesseract PILLOW pyscreenshot
2. Run your required program (Parser.py / Tesseract.py) using python3
3. Move the mouse for the left top corner of the required region on the screen and press ENTER
4. Move the mouse to the right bottom corner of the required region on the screen and press ENTER
5. You'll get your output.
