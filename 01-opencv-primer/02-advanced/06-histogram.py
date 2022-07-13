import cv2
import matplotlib.pyplot as plt
import numpy as np

img = cv2.imread('../resources/images/cats.jpg')
cv2.imshow('Cats', img)

blank = np.zeros(img.shape[:2], dtype='uint8')

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Grayscale histogram
gray_hist = cv2.calcHist([gray], [0], None, [256], [0, 256])

plt.figure()
plt.title('Grayscale Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
plt.plot(gray_hist)
plt.xlim([0, 256])
plt.show()

# Colour Histogram
plt.figure()
plt.title('Colour Histogram')
plt.xlabel('Bins')
plt.ylabel('# of pixels')
colors = ('b', 'g', 'r')
for i, col in enumerate(colors):
    hist = cv2.calcHist([img], [i], None, [256], [0, 256])
    plt.plot(hist, color=col)
    plt.xlim([0, 256])

plt.show()
cv2.waitKey(0)
