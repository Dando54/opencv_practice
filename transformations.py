import cv2 as cv
import numpy as np
from numpy.core.fromnumeric import resize

img = cv.imread('Photos/park.jpg')
cv.imshow('Boston', img)

# Translation


def translate(img, x, y):
    transMat = np.float32([[1, 0, x], [0, 1, y]])
    print(transMat)
    dimensions = (img.shape[1], img.shape[0])
    print(dimensions)
    return cv.warpAffine(img, transMat, dimensions)


translated = translate(img, 200, 100)
cv.imshow('Translated', translated)

# Rotation


def rotate(img, angle, rotPoint=None):
    (height, width) = img.shape[:2]  # first two values of img.shape

    if rotPoint is None:
        rotPoint = (width//2, height//2)

    rotMat = cv.getRotationMatrix2D(rotPoint, angle, 1.0)
    dimensions = (width, height)

    return cv.warpAffine(img, rotMat, dimensions)


rotated = rotate(img, -45)
cv.imshow('Rotated', rotated)

rotated_2 = rotate(rotated, -45)
cv.imshow('Rotated 2', rotated_2)

# Resizing
resized = cv.resize(img, (500, 500), interpolation=cv.INTER_CUBIC)
cv.imshow('Resized', resized)

# Flipping
flip = cv.flip(img, 1)
cv.imshow('Flipped', flip)

# Cropping
cropped = img[200:400, 300:400]
cv.imshow('Cropped', cropped)


cv.waitKey(0)
