import cv2
import numpy as np

img = cv2.imread('../resources/images/burano.jpg')
cv2.imshow('Burano', img)
cv2.waitKey(0)

img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
cv2.imshow('Burano RGB', img_rgb)
cv2.waitKey(0)

b, g, r = cv2.split(img)

cv2.imshow('Blue', b)
cv2.imshow('Green', g)
cv2.imshow('Red', r)
cv2.waitKey(0)

print(img_rgb.shape)
print(b.shape)
print(g.shape)
print(r.shape)

blank = np.zeros(img.shape[:2], dtype='uint8')

blue = cv2.merge([b, blank, blank])
green = cv2.merge([blank, g, blank])
red = cv2.merge([blank, blank, r])

cv2.imshow('Blue', blue)
cv2.imshow('Green', green)
cv2.imshow('Red', red)
cv2.waitKey(0)

merged = cv2.merge([r, g, b])
cv2.imshow('Merged Image', merged)
cv2.waitKey(0)
