import cv2

img = cv2.imread('1.jpg')
# img = cv2.GaussianBlur(img, (9, 9), 0)
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('result', img)

cv2.waitKey(0)
