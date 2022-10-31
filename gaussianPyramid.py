import cv2 as cv
from reduce import *

#Uses the reduce() function to create a gaussian pyramid of n levels
#I is the original image (must be opened with cv.imread())
#n is the number of levels
#returns an array of images where each image is a level of the pyramid
def gaussianPyramid(I, n):
    G=[]
    ct=1
    current=I
    G.append(current)
    while(ct<n):
        reduced=reduce(current)
        G.append(reduced)
        current=reduced
        ct=ct+1
    return G