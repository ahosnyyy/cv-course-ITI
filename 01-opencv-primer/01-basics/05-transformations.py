import cv2
import numpy as np

img = cv2.imread('../resources/images/cat.jpg')
cv2.imshow('Cat', img)
cv2.waitKey(0)


# Translation
def translate(in_img, x, y):
    trans_mat = np.float32([[1, 0, x], [0, 1, y]])
    dimensions = (in_img.shape[1], in_img.shape[0])
    return cv2.warpAffine(in_img, trans_mat, dimensions)

# -x --> Left
# -y --> Up
# x --> Right
# y --> Down


translated = translate(img, -100, 100)
cv2.imshow('Translated', translated)
cv2.waitKey(0)


# Rotation
def rotate(in_img, angle, rot_point=None):
    (height, width) = in_img.shape[:2]

    if rot_point is None:
        rot_point = (width // 2, height // 2)

    rot_mat = cv2.getRotationMatrix2D(rot_point, angle, 1.0)
    dimensions = (width, height)

    return cv2.warpAffine(in_img, rot_mat, dimensions)


rotated = rotate(img, -45)
cv2.imshow('Rotated', rotated)
cv2.waitKey(0)

rotated_rotated = rotate(img, -90)
cv2.imshow('Rotated Rotated', rotated_rotated)
cv2.waitKey(0)

# Resizing
resized = cv2.resize(img, (500, 500), interpolation=cv2.INTER_CUBIC)
cv2.imshow('Resized', resized)
cv2.waitKey(0)

# Flipping
flip = cv2.flip(img, -1)
cv2.imshow('Flip', flip)
cv2.waitKey(0)

# Cropping
cropped = img[200:400, 300:400]
cv2.imshow('Cropped', cropped)
cv2.waitKey(0)


