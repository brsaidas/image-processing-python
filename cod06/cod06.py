import cv2

img = cv2.imread("img.jpeg")

for i in range(75, 150):
    for j in range(75, 150):
        img.itemset((i,j,0), 0)
        img.itemset((i,j,1), 0)
        img.itemset((i,j,2), 255)

cv2.imshow("Imagem", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
