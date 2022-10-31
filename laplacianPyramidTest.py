from laplacianPyramid import *

image=cv.imread("lena.png")
size=4
L=laplacianPyramid(image,size)

ct=0
while(ct<size):
    cv.imwrite(str(ct)+'-lvl-LaplacianPry.png',L[ct])
    ct=ct+1