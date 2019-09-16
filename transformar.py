#!/usr/bin/python

from PIL import Image
from pytesseract import image_to_string

img =Image.open('../png/page0.png')
text = image_to_string(img, lang='eng')
print(text)
















#--------------------------------------------------------------------------#
"""from PIL import Image
import pytesseract
import cv2
import os
import time

# Argument
imagePath = "../png/page0.png"
prerocess = "threst"

# Cargar el Ejemplo y convetir a escala de grises
image = cv2.imread(imagePath)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Cheeck to see if we should apply thresholding to preprocess the image
if(prerocess=="threst"):
    gray = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Make a cheeck to see if media blurring should be done to remove noise
elif(prerocess=="blur"):
    gray = cv2.medianBlur(gray, 3)

# write the grayscale image to disk as a temporary file so we can apply OCR to it
filename = "{}.png".format( os.getpid())
cv2.imwrite(filename, gray) # Create temporary file

# load the image as a PIL / pillow image, apply ORC, and then delete the temporary file
try:
    img = image.open(filename)
    pytesseract.pytesseract.tesseract_cmd = r"C:/Tesseract-OCR/tesseract.exe"
    text = pytesseract.image_to_string( img )
    print("---------------------------------------------------------------------")
    print("     *       *           T E X T   D E T E C T E D   *       *       ")
    print("---------------------------------------------------------------------")
    print(text)
    print("-----------------------------------------------------------------")

    #Show the Output
    cv2.imwrite("Image",Image)
    cv2.imwrite("Output", gray)
    print("Press <ESC> to close windows")

    while(1):
        if ( cv2.waitKey(20) & 0xFF==27):#Detecta la Tecla <ESC>
            break
    cv2.destroyAllWindows()
except IOError as e:
    print("I/O ERROR : " + str(e))
except:
    print("Ooops!.. Error to read Image.")

os.remove(filename)"""