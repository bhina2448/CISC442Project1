import cv2 as cv
import numpy as np
from convolve import *

#Used to test the convolve function. Not meant to be run in main.py
x_dir_kernel=np.array([[-1,-2,1],[0,0,0],[1,2,1]])

convolve('lena.png',x_dir_kernel)

# Reading the image
#image = cv.imread('lena.png')
  
# Applying the filter2D() function
#img = cv.filter2D(src=image, ddepth=-1, kernel=x_dir_kernel)
  
# Shoeing the original and output image
#cv.imshow('Original', image)
#cv.imshow('Kernel Blur', img)
  
#cv.waitKey()
#cv.destroyAllWindows()