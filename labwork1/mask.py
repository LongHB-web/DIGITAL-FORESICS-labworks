import cv2 as cv
import numpy as np

img = cv.imread(cv.samples.findFile(r"C:\Users\MY PC\Downloads\opencv\sources\samples\data\logo-usth.png"))

rgb = cv.cvtColor(img, cv.COLOR_BGR2HSV)

lower_red = np.array([161, 155, 84])
upper_red = np.array([179, 255, 255])
red_mask = cv.inRange(rgb, lower_red, upper_red)
red = cv.bitwise_and(img, img, mask=red_mask)

lower_blue = np.array([94, 80, 2])
upper_blue = np.array([126, 255, 255])
blue_mask = cv.inRange(rgb, lower_blue, upper_blue)
blue = cv.bitwise_and(img, img, mask=blue_mask)

cv.imshow("Red", red)
cv.imshow("Blue", blue)
cv.waitKey(0)