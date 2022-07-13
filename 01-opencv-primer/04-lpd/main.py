import cv2
from morpho import maximize_contrast, preprocess, detect_lp_morpho, detect_lp

in_img = cv2.imread("../resources/images/char_frame_180_car_no_lp1.png")
cv2.imshow("Input Image", in_img)
cv2.waitKey(0)

gray_img = cv2.cvtColor(in_img, cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Image", gray_img)
cv2.waitKey(0)

contrast_img = maximize_contrast(gray_img)
cv2.imshow("Contrast Image", contrast_img)
cv2.waitKey(0)

pre_img = preprocess(in_img)
cv2.imshow("Preprocessed Image", pre_img)
cv2.waitKey(0)

# can_img, candidates = detect_lp_morpho(in_img)
# print(candidates)
# cv2.imshow("Candidates Image", can_img)
# cv2.waitKey(0)

lp_img, lps = detect_lp(in_img)
print(lps)
cv2.imshow("LP Image", lp_img)
cv2.waitKey(0)

