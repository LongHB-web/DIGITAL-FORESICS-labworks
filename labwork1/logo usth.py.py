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
import cv2

distinct_colors = []
a, b, c = cv2.split(img)
distinct_imgs = []


print("[] Set up colors")
for i in range(len(a)):
    for j in range(len(a[i])):
        if (a[i, j], b[i, j], c[i, j]) not in distinct_colors:
            distinct_colors.append((a[i, j], b[i, j], c[i, j]))

print("[] Appending copy...")
for color in distinct_colors:
    distinct_imgs.append(img.copy())

print("[] Seperating...")
for i in range(len(distinct_imgs)):
    for j in range(len(img)):
        for k in range(len(img[j])):
            if img[j, k, 0] != distinct_colors[i][0] or img[j, k, 1] != distinct_colors[i][1] or img[j, k, 2] != distinct_colors[i][2]:
                distinct_imgs[i][j, k] = [0, 0, 0]

print("[] Write to file...")
for i in range(len(distinct_imgs)):
    cv2.imwrite("logo-distinct" + str(i) + ".png", distinct_imgs[i])


k = cv.waitKey(0)
