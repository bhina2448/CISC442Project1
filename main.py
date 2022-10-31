from convolve import *
from expand import *
from gaussianPyramid import*
from laplacianPyramid import*
from mosaic import *
from reconstruct import *
from reduce import *

filename="lena.png"
img=cv.imread(filename)

#question 1
x_dir_kernel=np.array([[-1,-2,1],[0,0,0],[1,2,1]])
convolve(filename,x_dir_kernel)

#question 2
reduced=reduce(img)
cv.imwrite("reducedResults.png", reduced)

#question 3
expanded=expand(img)
cv.imwrite("expandResults.png",expanded)

#question 4
G=gaussianPyramid(img,4)
ct=0
for image in G:
    cv.imwrite(str(ct)+"-lvl-GaussianPy.png",image)
    ct=ct+1

#question 5
L=laplacianPyramid(img,4)
ct=0
for image in L:
    cv.imwrite(str(ct)+"-lvl-LaplacianPy.png",image)
    ct=ct+1

#question 6
reconstructed=reconstruct(L,4)
cv.imwrite("reconstructResults.png", reconstructed)