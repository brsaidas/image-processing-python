'''
kernel = np.ones((3, 3),np.uint8)
mask = cv2.inRange(hsv, lower_red, upper_red)
mask = cv2.erode(mask, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.dilate(mask, kernel)
mask = cv2.bilateralFilter(mask, 9, 75, 75)
mask = cv2.medianBlur(mask, 1)
'''
import cv2
import numpy as np

h, s, v = 255, 255, 255
H, S, V = 0, 0, 0
f = False

def func(event, x, y, flag, param):
    global H, S, V, h, s, v, f
    if event  == cv2.EVENT_LBUTTONDOWN:
        f = True
        
    if event == cv2.EVENT_MOUSEMOVE:
        if f:
            h = min(hsv[y, x, 0], h)
            s = min(hsv[y, x, 1], s)
            v = min(hsv[y, x, 2], v)
            H = max(hsv[y, x, 0], H)
            S = max(hsv[y, x, 1], S)
            V = max(hsv[y, x, 2], V)
            print(H, S, V, h, s, v)

    if event  == cv2.EVENT_LBUTTONUP:
        f = False
        
img = cv2.imread('img.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

lower_red = np.array([h, s, v])
upper_red = np.array([H, S, V])
mask = cv2.inRange(hsv, lower_red, upper_red)

cv2.imshow('hsv', hsv)
cv2.namedWindow('mask')
cv2.setMouseCallback('hsv', func)

while True:
    lower_red = np.array([h, s, v])
    upper_red = np.array([H, S, V])
    mask = cv2.inRange(hsv, lower_red, upper_red)
    cv2.imshow('mask', mask)
    if cv2.waitKey(1) == ord('q'):
        break

cv2.destroyAllWindows()
