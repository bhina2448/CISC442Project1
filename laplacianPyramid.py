from cv2 import CV_64F, CV_8U
from gaussianPyramid import *
from expand import *
import cv2 as cv

#uses gaussianPyramid() and expand() to create a Laplacian Pyramid of n levels
#I is the original image (opened with cv.imread())
#n is the number of levels
#returns an array of the images in the pyramid
def laplacianPyramid(I,n):
    G=gaussianPyramid(I, n+1)
    ct=0
    L=[]
    while(ct<n):
        current=G[ct]
        lvlUp=G[ct+1]
        lvlUpExp=expand(lvlUp)
        if(current.shape != lvlUpExp.shape):
            lvlUpExp.resize((current.shape))
        lap=cv.subtract(current,lvlUpExp, dtype=CV_64F)
        L.append(lap)
        ct=ct+1
    return L
