import cv2

# Read in an image
img = cv2.imread('../resources/images/cat.jpg')
cv2.imshow('Cat', img)
cv2.waitKey(0)

# Converting to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('Gray', gray)
cv2.waitKey(0)

# Blur 
blur = cv2.GaussianBlur(img, (3, 3), cv2.BORDER_DEFAULT)  # (7, 7)
cv2.imshow('Blur', blur)
cv2.waitKey(0)

# Edge Cascade
canny = cv2.Canny(blur, 25, 100)
cv2.imshow('Canny Edges', canny)
cv2.waitKey(0)

# Dilating the image
dilated = cv2.dilate(canny, (7, 7), iterations=1)  # iterations=3
cv2.imshow('Dilated', dilated)
cv2.waitKey(0)

# Eroding
eroded = cv2.erode(dilated, (7, 7), iterations=3)
cv2.imshow('Eroded', eroded)
cv2.waitKey(0)

# Resize
resized = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized', resized)
cv2.waitKey(0)

# Cropping
cropped = img[50:200, 200:400]
cv2.imshow('Cropped', cropped)
cv2.waitKey(0)
