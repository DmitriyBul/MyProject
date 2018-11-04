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
#Загрузка нейронной сети(весов и т.д.)
# load json and create model
json_file = open('model.json', 'r')
loaded_model_json = json_file.read()
json_file.close()
loaded_model = model_from_json(loaded_model_json)
# load weights into new model
loaded_model.load_weights("model.h5")
print("Loaded model from disk")

model = Sequential()
model.add(Conv2D(8,(3,3),input_shape=(100,100,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2),strides=2))
model.add(Conv2D(12,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2),strides=2))
model.add(Conv2D(16,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(units=128,activation='relu'))
model.add(Dense(units=1,activation='sigmoid'))

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

test_hand_dir = '/home/dmitriy/Documents/Dataset-3/'




#Список изображений, полученных с камеры
b = []
c = []
#Функция получения изображений
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
        Y_pred = model.predict(test_x_data_set)
        print(Y_pred)
        y_pred = np.argmax(Y_pred, axis=1)
        print(y_pred)
        #d = model.predict_classes(test_x_data_set)
        #print(d)



Images_Capture()
#s = Sign_Detection()
#print(s)