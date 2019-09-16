#!/usr/bin/python

from PIL import Image
from pytesseract import image_to_string

img =Image.open('../png/page0.png')
text = image_to_string(img, lang='eng')
print(text)