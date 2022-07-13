import cv2
import numpy as np

img = cv2.imread('../resources/images/cats.jpg')
cv2.imshow('Cats', img)
cv2.waitKey(0)

blank = np.zeros(img.shape[:2], dtype='uint8')
circle = cv2.circle(blank.copy(), (img.shape[1] // 2 + 45, img.shape[0] // 2), 100, 255, -1)

masked = cv2.bitwise_and(img, img, mask=circle)
cv2.imshow('Circle Masked Image', masked)
cv2.waitKey(0)
