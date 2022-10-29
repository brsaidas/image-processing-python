import cv2

img1 = cv2.imread("img.jpg", 1)
img2 = cv2.imread("img.jpg", 0)

cv2.imshow("Imagem 1 Carregada", img1)
cv2.imshow("Imagem 2 Carregada", img2)

cv2.waitKey(0)

cv2.destroyAllWindows()

cv2.imwrite("imagemSalva1.jpg", img1)
cv2.imwrite("imagemSalva2.jpg", img2)

