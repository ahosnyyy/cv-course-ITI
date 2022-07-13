import cv2

img = cv2.imread('../resources/images/cats.jpg')
cv2.imshow('Cats', img)

# Averaging
average = cv2.blur(img, (3, 3))  # 7, 7
cv2.imshow('Average Blur', average)
cv2.waitKey(0)

# Gaussian Blur
gauss = cv2.GaussianBlur(img, (3, 3), 0)
cv2.imshow('Gaussian Blur', gauss)
cv2.waitKey(0)

# Median Blur
median = cv2.medianBlur(img, 3)
cv2.imshow('Median Blur', median)
cv2.waitKey(0)

# Bilateral
bilateral = cv2.bilateralFilter(img, 10, 35, 25)
cv2.imshow('Bilateral', bilateral)
cv2.waitKey(0)
