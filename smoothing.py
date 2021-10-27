import cv2 as cv

img = cv.imread('Photos/cats.jpg')
cv.imshow('Cats', img)

# Averaging
average = cv.blur(img, (7, 7))
cv.imshow('Average blur', average)

# Gaussian blur
gauss = cv.GaussianBlur(img, (7, 7), 0)
cv.imshow('Gaussian blur', gauss)

# Median blur
median = cv.medianBlur(img, 7)
cv.imshow('Median blur', median)

# Bilateral blur - retains the edges even when the blur is applied
bilat = cv.bilateralFilter(img, 10, 35, 25)
cv.imshow('Bilateral blur', bilat)

cv.waitKey(0)
