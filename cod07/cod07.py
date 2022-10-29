import cv2
from matplotlib import pyplot as plt

img = cv2.imread("img.tif")

plt.hist(img.ravel(), 256, [0, 256])

cv2.imshow("Imagem", img)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
