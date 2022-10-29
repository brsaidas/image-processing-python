import cv2
import numpy as np

img = cv2.imread("img.jpeg")

print(img.shape)
print("R: ", img.item(0, 0, 2), " | G:", img.item(0,0, 1), " | B:", img.item(0,0,0))

img.itemset((0,0,2), 255)
img.itemset((0,0,1), 0)
img.itemset((0,0,0), 0)

print("R: ", img.item(0, 0, 2), " | G:", img.item(0,0, 1), " | B:", img.item(0,0,0))

cv2.imwrite("img2.jpg", img)


