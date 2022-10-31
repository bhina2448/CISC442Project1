from expand import *
import cv2 as cv

original=cv.imread("lena.png")
print(original.shape)
exp=expand(original)
print(exp.shape)
cv.imwrite("expanded.png", exp)