import cv2 as cv
import numpy as np


# Write a function Convolve (I, H). I is the FILENAME of an image of varying size, 
# H is a kernel of varying size.
# The output of the function should be the convolution result that is displayed.
#output will be saved as "convolveResult.png"

def convolve(I, H):
    #read image, add padding and convert to grescale
    img= cv.imread(I)
    image= cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    image=np.pad(image, 1, mode='constant')
    rsize= len(H) #length of the rows of the kernel
    csize= len(H[0])#length of the columns of the kernel
    x=0
    y=0
    xend=0
    yend=0
    output=np.ones((len(image)-rsize+1,len(image[0])-csize+1))
    for x in range(0, len(image)-rsize+1): 
        for y in range(0,len(image[0])-csize+1):
            xend=x+rsize
            yend=y+csize
            curr=(image[x:xend, y:yend])#portion of image currently working with
            mul_curr_h= curr*H
            val= np.sum(mul_curr_h)
            #update image values
            for i in range(x,xend):
                for j in range (y, yend):
                    if((i<len(image)-rsize+1)and (j<len(image[0])-csize+1)):
                        output[i,j]=val
    cv.imwrite('convolveResults.png',output)

