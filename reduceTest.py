from reduce import *

img=cv.imread("lena.png")
print(img.shape)
reduced=reduce(img)
print(reduced.shape)
cv.imwrite('reduced.png',reduced)