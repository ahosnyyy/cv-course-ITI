import cv2
import numpy as np

img = cv2.imread('../resources/images/cat.jpg')
cv2.imshow('Cat', img)
cv2.waitKey(0)

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey(0)

blur = cv2.GaussianBlur(gray, (5, 5), cv2.BORDER_DEFAULT)
cv2.imshow('Blur', blur)
cv2.waitKey(0)

canny = cv2.Canny(blur, 50, 100)
cv2.imshow('Canny Edges', canny)
cv2.waitKey(0)

# ret, thresh = cv2.threshold(gray, 125, 255, cv2.THRESH_BINARY)
# cv2.imshow('Thresh', thresh)
# cv2.waitKey(0)

contours, hierarchies = cv2.findContours(canny, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)
print(f'{len(contours)} contour(s) found!')

blank = np.zeros(img.shape, dtype='uint8')
cv2.drawContours(blank, contours, -1, (0, 0, 255), 1)
cv2.imshow('Contours Drawn', blank)
cv2.waitKey(0)
