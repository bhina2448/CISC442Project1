import cv2 as cv
from laplacianPyramid import *
from reconstruct import *
#creates a mosaic of two images using Laplacian plane based reconstruction 
#R- right image (opened with cv.imread())
#L- left image (opened with cv.imwrite())
#returns mosaic
def mosaic(R,L):
    imgL=L
    imgR=R
    lw,lh,ld=L.shape
    rw,rh,rd=R.shape
    if L.shape != R.shape:
        if lw>rw:
            width=lw
        else:
            width=rw
        if lh>rh:
            height=lh
        else:
            height=rh
        imgL=cv.resize(imgL,(width,height))
        imgR=cv.resize(imgR,(width,height))

    #get laplacian pyramids for left and right
    LR=laplacianPyramid(imgR,4)
    LL=laplacianPyramid(imgL,4)

    #add the halves together on each level
    LS=[]
    for right,left in zip(LR,LL):
        rows,cols,dim=right.shape
        ls=np.hstack((right[:,0:cols//2], left[:,cols//2:]))
        LS.append(ls)
    
    #reconstruct
    reconstructed=reconstruct(LS,4)
    return reconstructed