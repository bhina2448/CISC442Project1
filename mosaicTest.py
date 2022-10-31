from mosaic import *
import cv2 as cv

right=cv.imread("images/Test_A1.png")
left=cv.imread("images/Test_A2.png")
m=mosaic(right,left)
cv.imwrite("1mosaicResults.png",m)

right=cv.imread("images/Test_B1.png")
left=cv.imread("images/Test_B2.png")
m=mosaic(right,left)
cv.imwrite("2mosaicResults.png",m)

right=cv.imread("images/Test_C1.png")
left=cv.imread("images/Test_C2.png")
m=mosaic(right,left)
cv.imwrite("3mosaicResults.png",m)

right=cv.imread("images/Test_D1.png")
left=cv.imread("images/Test_D2.png")
m=mosaic(right,left)
cv.imwrite("4mosaicResults.png",m)