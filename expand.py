import numpy as np
from PIL import Image
import cv2 as cv

#write a function to expand an image by twice its width and height
#uses nearest neightbor interpolation
#I- image to be expanded (must be opened with cv.readim())
def expand(I):
    image=I
    #get image dimenstions
    width,height,dim= image.shape
    expandedWidth= (int)(width*2)
    expandedHeight= (int)(height*2)
    newshape=(expandedWidth,expandedHeight,dim)

    scaled=np.ones(newshape)

    for y in range(expandedHeight-1):
        for x in range(expandedWidth-1):
            xest=int(np.round(x/2))
            yest=int(np.round(y/2))
            p=image[xest,yest]
            scaled[x,y]=p
    return scaled