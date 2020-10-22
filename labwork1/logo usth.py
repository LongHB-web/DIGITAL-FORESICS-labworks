import cv2
import cv2 as cv
import sys
import numpy as np
from matplotlib import pyplot as plt
cv.samples.addSamplesDataSearchPath("C:\\Users\\MY PC\\Downloads\\opencv\\sources\\samples\\data")
img = cv.imread(cv.samples.findFile("logo-usth.png"))
if img is None:
    sys.exit("Could not read the image.")
cv.imshow("Display window", img)
b, g, r = cv.split(img)
cv.imshow('image_blue', b)
cv.waitKey(0)
cv.imshow('image_green', g)
cv.waitKey(0)
cv.imshow('image_red', r)
cv.waitKey(0)