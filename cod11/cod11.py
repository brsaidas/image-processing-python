import cv2 as cv

def pixelColor(event, x, y, flag, param):
    if event == cv.EVENT_LBUTTONDBLCLK:
        print(x, y, img[y, x, :])

img = cv.imread('img2.png')
#img = cv.cvtColor(img, cv.COLOR_BGR2HSV)
cv.namedWindow('imagem')
cv.imshow('imagem', img)
cv.setMouseCallback('imagem', pixelColor)

cv.waitKey(0)
cv.destroyAllWindows()
