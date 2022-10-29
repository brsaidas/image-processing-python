import cv2
#import numpy as np

img = cv2.imread("img.jpeg")

img2 = img[20:180, 30:200]

cv2.imwrite("img2.jpg", img2)

img[0:160, 0:170] = img2

cv2.imwrite("img3.jpg", img)
