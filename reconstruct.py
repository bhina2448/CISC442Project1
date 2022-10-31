import cv2 as cv
from expand import*

#collapses the Laplacian pyramid LI of n levels to generate the original image
#LI is an array of images in the pyramid
#n is the number of levels
#returns the reconstructed image
def reconstruct(LI, n):
    current=LI[n-1]
    ct=n-1
    while ct>0:
        next=LI[ct-1]
        currentex=expand(current)
        if(currentex.shape != next.shape):
            currentex.resize((next.shape))
        current=cv.add(currentex,next)
        ct=ct-1
    return current