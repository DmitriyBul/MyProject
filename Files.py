#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2
import time
import os
import numpy as np
import cv
h_min = np.array((155, 0, 138), np.uint8)
h_max = np.array((176, 84, 255), np.uint8)
hsv_min = np.array((2, 28, 65), np.uint8)
hsv_max = np.array((26, 238, 255), np.uint8)

gray_low = np.array((200), np.uint8)
gray_high = np.array((230), np.uint8)

cap = cv2.VideoCapture(0)
i = 0
for i in range (0, 400):
    ret, img = cap.read()
    img = cv2.GaussianBlur(img, (7,7), 0)
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    im2 = cv2.equalizeHist(im)
    thresh_im2 = cv2.inRange(im2, gray_low, gray_high)
    thresh = cv2.inRange(hsv, h_min, h_max)
    contours, hierarchy = cv2.findContours(thresh.copy(), cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    for contour in contours:
        area = cv2.contourArea(contour)

        if area > 4000:
            cv2.drawContours(thresh, contour, -1, (0, 255, 0), 2)
    #cv2.drawContours(img, contours, -1, (0, 255, 0), 3)
    #cv2.imshow('output', img)
    cv2.imshow('output3', thresh_im2)
    cv2.imshow('output4', thresh)

    im3 = cv2.cvtColor(thresh_im2, cv2.COLOR_GRAY2BGR)
    im4 = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
    path = "%.4d.jpg" % i
    cv2.imwrite("ima" + str(i)+ ".jpg", im4)
    i += 1
    key = cv2.waitKey(10)
    #print(cv2.countNonZero(thresh))

    

