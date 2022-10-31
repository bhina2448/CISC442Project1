import cv2 as cv
import numpy as np
from PIL import Image, ImageFilter

#write a function to reduce an image by half of its width and height
#uses nearest neightbor interpolation
#I- input image (opened with cv.imread())
#returns reduced image
def reduce(I):
    image=cv.GaussianBlur(I,(5,5),0)
    #get image dimenstions
    width,height,dim= image.shape
    reducedWidth= (int)(width/2)
    reducedHeight= (int)(height/2)
    newshape=(reducedWidth,reducedHeight,dim)

    scaled=np.ones(newshape)

    for y in range(reducedHeight):
        for x in range(reducedWidth):
            xest=int(np.round(x/0.5))
            yest=int(np.round(y/0.5))
            p=image[xest,yest]
            scaled[x,y]=p
    return scaled


