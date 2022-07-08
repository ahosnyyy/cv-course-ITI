import cv2 as cv2

img = cv2.imread('../resources/images/cat.jpg')
cv2.imshow('Cat', img)
cv2.waitKey(0)

# BGR to Grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey(0)

# BGR to HSV
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
cv2.imshow('HSV', hsv)
cv2.waitKey(0)

# BGR to L*a*b
lab = cv2.cvtColor(img, cv2.COLOR_BGR2LAB)
cv2.imshow('LAB', lab)
cv2.waitKey(0)

# BGR to RGB
rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('RGB', rgb)
cv2.waitKey(0)

