import cv2
import numpy as np


def maximize_contrast(gray):
    structuring_element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

    img_top_hat = cv2.morphologyEx(gray, cv2.MORPH_TOPHAT, structuring_element)
    img_black_hat = cv2.morphologyEx(gray, cv2.MORPH_BLACKHAT, structuring_element)

    img_gray_scale_plus_top_hat = cv2.add(gray, img_top_hat)
    img_gray_scale_minus_top_hat = cv2.subtract(img_gray_scale_plus_top_hat, img_black_hat)

    return img_gray_scale_minus_top_hat


def preprocess(img):
    b, g, r = cv2.split(img)
    gray = maximize_contrast(r)
    blurred = cv2.GaussianBlur(gray, (5, 5), 0)
    thresh = cv2.adaptiveThreshold(blurred, 255.0, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV,
                                   19, 40)
    return thresh


def detect_lp_morpho(img, l_min=0, l_max=1000, w_min=0, w_max=1000):
    thresh = preprocess(img)
    edges = cv2.Canny(thresh, 100, 200)
    kernel_sz = 3
    iterations = 2
    structuring_element = cv2.getStructuringElement(cv2.MORPH_RECT, (kernel_sz, kernel_sz))
    dilated = cv2.dilate(edges, structuring_element, iterations=iterations)
    contours, hierarchy = cv2.findContours(dilated, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)

    candidates = []
    for c in contours:
        rot_rect = cv2.minAreaRect(c)
        center, size, theta = rot_rect
        length, width = min(size), max(size)

        if l_min <= length <= l_max and w_min <= width <= w_max:
            candidates.append(rot_rect)
            box = cv2.boxPoints(rot_rect)
            box = np.int0(box)
            cv2.drawContours(img, [box], 0, (0.0, 255.0, 0.0), 2)

    return img, candidates


def detect_lp(img):
    sz = (img.shape[1], img.shape[0])
    car_lp, lps = detect_lp_morpho(cv2.resize(img, (500, 500)), l_min=35, l_max=60, w_min=55, w_max=120)
    car_lp = cv2.resize(car_lp, sz)
    return car_lp, lps
