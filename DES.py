#pip install pyDes

from pyDes import *
import base64
import numpy as np
%pylab inline
import matplotlib.pyplot as plt
%matplotlib inline
import matplotlib.image as mpimg
from skimage import io

def splitfilename(filename):
    sname=""
    sext=""
    i=filename.rfind(".")
    if(i!=0):
        n=len(filename)
        j=n-i-1
        sname=filename[0:i]
        sext=filename[-j:]    
    return sname, sext
    
print("****DES(Data Encryption Standard) Laboratory - smahechap@unal.edu.co****\n")
im = input("Introduzca el nombre del archivo con su extensión: ")
ext = splitfilename(im)#Split file extension from filename
with open(im, "rb") as image:
  image_format = image.read()#Read image file
key = des("KEYSANTI", CBC, "\0\0\0\0\0\0\0\0", pad=None, padmode=PAD_PKCS5)#Using DES key = "KEYSANTI"
data_encrypted = key.encrypt(image_format)#Encrypt image text
b_64 = base64.b64encode(data_encrypted)#Convert data_encrypted into base64
print("Mensaje cifrado en Base64:",b_64)
not_b_64 = base64.b64decode(b_64)
data_descrypted = key.decrypt(not_b_64)#Descrypt notbase64 string
with open("descrypted_image.%s" % ext[1], "wb") as image:#Open & create descrypted image file
  o = image.write(data_descrypted)#Fill it with data_descrypted
print("Imagen final: \n")
new_image=io.imread("descrypted_image.%s" % ext[1])
plt.imshow(new_image)#Show new image
