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
        img = cv2.resize(img, (100, 100))

        test_x_data_set = np.zeros([1, 100, 100, 3])
        for index in range(1):
            test_x_data_set[index, :, :, :] = img
        print(img.shape)
        cv2.imshow('output', img)
        key = cv2.waitKey(10)
        #Сохранение изображений
        #path = "%.4d.jpg" % i
        #cv.SaveImage(path, frame)
        time.sleep(1)
        #Удаление старых изображений

        d = model.predict(test_x_data_set)
        print (d)
#Функция классификации изображений
def Sign_Detection():

    test_hand_sample = len(os.listdir(test_hand_dir))
    print("Test Set samples- "+str(test_hand_sample))

    test_x_data_set = np.zeros([test_hand_sample, 100, 100, 3])
    test_file_list = []

    for index, filename in enumerate(os.listdir(test_hand_dir)):
        img = Image.open(test_hand_dir+filename)
        test_file_list.append(filename)
        img = img.resize((100, 100), Image.ANTIALIAS)
        im = np.array(img)
        test_x_data_set[index, :, :, :] = im

    test_x_data_set = test_x_data_set/255

    c = model.predict(test_x_data_set)
    return(c)
    #print(time_predictions)

Images_Capture()
#s = Sign_Detection()
#print(s)