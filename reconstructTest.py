from reconstruct import *
from laplacianPyramid import *

img=cv.imread('lena.png')
L=laplacianPyramid(img,4)
reconstruct(L,4)