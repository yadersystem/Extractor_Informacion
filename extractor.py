import base64
from PIL import Image, ImageSequence
import numpy as np
from libtiff import TIFF


#--------------------------------------------------------#
                # LiffTiff
#--------------------------------------------------------#
file = TIFF.open ('18340.bin', 'r')
for i, image in enumerate(file.iter_images()):
   Image.fromarray(image).save("png/page%d.png" % i)




#--------------------------------------------------------#
            # Trabajando con Base 64 y PILL
#--------------------------------------------------------#

#with open('18340.bin', mode='rb') as file:
#    str =base64.b64encode(file.read())

#imgdata = base64.b64decode(str)
#filename = 'some.tif'

#with open(filename, 'wb') as f:
 #  f.write(imgdata)

#from numpy import save

#im = Image.open("some.tiff")
#for i, page in enumerate(ImageSequence.Iterator(im)):
    #page.save("png/page%d.png" % i)
    #region = (0, 0, 640, 980)
    #imagen_recortada = page.crop(region)
    #imagen_recortada.show()
    #imagen_recortada.save("png/page%d.png" % i)
