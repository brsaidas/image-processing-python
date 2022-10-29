import cv2

img = cv2.imread("img.jpeg")

for i in range(img.shape[0]):
    for j in range(img.shape[1]):
        img.itemset((i,j,0), 255-img.item(i, j, 0))
        img.itemset((i,j,1), 255-img.item(i, j, 1))
        img.itemset((i,j,2), 255-img.item(i, j, 2))

cv2.imshow("Imagem", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite("img2.jpg", img)
