from gaussianPyramid import *
import cv2 as cv

image=cv.imread("lena.png")
size=4
G=gaussianPyramid(image,size)

ct=0
while(ct<size):
    cv.imwrite(str(ct)+'-lvl-GaussianPry.png',G[ct])
    ct=ct+1