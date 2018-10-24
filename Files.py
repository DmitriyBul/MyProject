#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import time
import os
import numpy as np
import cv
h_min = np.array((41, 24, 0), np.uint8)
h_max = np.array((240, 164, 252), np.uint8)
hsv_min = np.array((2, 28, 65), np.uint8)
hsv_max = np.array((26, 238, 255), np.uint8)

gray_low = np.array((220), np.uint8)
gray_high = np.array((250), np.uint8)

cap = cv2.VideoCapture(0)
i = 0
for i in range(0,400):
    ret, img = cap.read()
    img = cv2.GaussianBlur(img, (7,7), 0)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    im2 = cv2.equalizeHist(im)
    thresh_im2 = cv2.inRange(im2, gray_low, gray_high)
    thresh = cv2.inRange(hsv, h_min, h_max)
    contours, hierarchy = cv2.findContours(thresh_im2.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 4000:
            cv2.drawContours(im2, contour, -1, (0, 255, 0), 2)
    #cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    cv2.imshow('output2', thresh_im2)
    #cv2.imshow('output', img)
    cv2.imshow('output3', thresh)

    path = "%.4d.jpg" % i
    cv2.imwrite("image" + str(i)+ ".jpg", thresh)
    i += 1
    key = cv2.waitKey(10)




'''

b = []

for k in range(0,200):
    if k < 5:
        j = k
    else:
        j = k - 4
    a = open("{id:04d}.jpg".format(id=k), "r")
    #c = os.path.splitext(a.name)[0]
    #c = int(c)
    #print(a.name)
    b.append(a.name)
    if len(b) > 5:
        #print(b[k])
        os.remove("{id:04d}.jpg".format(id=j))
'''