import cv2
import numpy as np


def origin_LBP(img):
    dst = np.zeros(img.shape, dtype=img.dtype)
    h, w = img.shape
    for i in range(1, h - 1):
        for j in range(1, w - 1):
            center = img[i][j]
            code = 0

            code |= (img[i - 1][j - 1] >= center) << (np.uint8)(7)
            code |= (img[i - 1][j] >= center) << (np.uint8)(6)
            code |= (img[i - 1][j + 1] >= center) << (np.uint8)(5)
            code |= (img[i][j + 1] >= center) << (np.uint8)(4)
            code |= (img[i + 1][j + 1] >= center) << (np.uint8)(3)
            code |= (img[i + 1][j] >= center) << (np.uint8)(2)
            code |= (img[i + 1][j - 1] >= center) << (np.uint8)(1)
            code |= (img[i][j - 1] >= center) << (np.uint8)(0)

            dst[i - 1][j - 1] = code
    return dst


gray = cv2.imread('F:/Python/a.jpg', cv2.IMREAD_GRAYSCALE)
cv2.imshow('img', gray)
org_lbp = origin_LBP(gray)
cv2.imshow('org_lbp', org_lbp)
cv2.waitKey(0)
