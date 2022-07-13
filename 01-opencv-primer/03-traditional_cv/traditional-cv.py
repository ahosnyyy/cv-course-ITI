import cv2

img_bgr = cv2.imread('../resources/images/cat.jpg')
img_rgb = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
cv2.imshow('Cat', img_rgb)
cv2.waitKey(0)

gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey(0)

thresh = cv2.adaptiveThreshold(gray,
                               255.0,
                               cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
                               cv2.THRESH_BINARY_INV, 19, 20)
cv2.imshow('Threshold', thresh)
cv2.waitKey(0)

edges = cv2.Canny(thresh, 100, 200)
cv2.imshow('Edges', edges)
cv2.waitKey(0)

structuringElement = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilated = cv2.dilate(edges, structuringElement, iterations=1)
cv2.imshow('Dilated', dilated)
cv2.waitKey(0)

contours, hierarchy = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
print(len(contours))

cv2.drawContours(img_rgb, contours, -1, (0, 255, 0), 3)
cv2.imshow('Contours', img_rgb)
cv2.waitKey(0)

