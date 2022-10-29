import cv2

img1 = cv2.imread("img.jpg", 1)
img2 = cv2.imread("img.jpg", 0)

contador = 1
while contador <= 10:
    if contador%2 == 0:
        cv2.imshow("Imagem do while " + str(contador), img1)
    else:
        cv2.imshow("Imagem do while " + str(contador), img2)   
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    contador+=1

for x in range(10):
    if (x+1)%2 == 0:
        cv2.imshow("Imagem do for " + str(x+1), img2)
    else:
        cv2.imshow("Imagem do for " + str(x+1), img1)
    cv2.waitKey(0)
    cv2.destroyAllWindows()
    


