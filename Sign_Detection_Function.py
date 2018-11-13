#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv
import time
import os
import numpy as np
from PIL import Image
import matplotlib as plt
import timeit
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import model_from_json
import cv2

h_min = np.array((41, 24, 0), np.uint8)
h_max = np.array((240, 164, 252), np.uint8)
gray_low = np.array((220), np.uint8)
gray_high = np.array((250), np.uint8)

def Images_Capture():

    cap = cv2.VideoCapture(0)

    while cap.isOpened():
        ret, img = cap.read()

        img = cv2.GaussianBlur(img, (7, 7), 0)
        hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

        im = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        im2 = cv2.equalizeHist(im)
        thresh_im2 = cv2.inRange(im2, gray_low, gray_high)
        thresh = cv2.inRange(hsv, h_min, h_max)
        im3 = cv2.cvtColor(thresh_im2, cv2.COLOR_GRAY2BGR)
        im4 = cv2.cvtColor(thresh, cv2.COLOR_GRAY2BGR)
        img = cv2.resize(im4, (100, 100))

        test_x_data_set = np.zeros([1, 100, 100, 3])
        for index in range(1):
            test_x_data_set[index, :, :, :] = img
        #print(img.shape)
        cv2.imshow('output', img)
        key = cv2.waitKey(10)
        d = loaded_model.predict_classes(test_x_data_set)
        print(d)

#Загрузка нейронной сети(весов и т.д.)
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")


test_hand_dir = '/home/dmitriy/Documents/Dataset-3/'

Images_Capture()
