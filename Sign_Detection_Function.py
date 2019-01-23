#! /usr/bin/env python
# -*- coding: utf-8 -*-

import time
import os
import numpy as np
from PIL import Image
import matplotlib as plt
import timeit
from keras.models import model_from_json
from keras.models import load_model
import cv2


def Images_Capture():
    a = 0
    cap = cv2.VideoCapture(0)
    Hand = 0
    Ok = 0
    Victory = 0

    while cap.isOpened():
        ret, img = cap.read()

        img = cv2.GaussianBlur(img, (7, 7), 0)

        cv2.imshow('output', img)
        img = cv2.resize(img, (100, 100))

        test_x_data_set = np.zeros([1, 100, 100, 3])
        for index in range(1):
            test_x_data_set[index, :, :, :] = img
        #print(img.shape)

        key = cv2.waitKey(10)
        d = loaded_model.predict_classes(test_x_data_set)

        if d == 0:
            print("Hand")
        if d == 1:
            print("Ok")
        if d == 2:
            print("Victory")
        if d == 3:
            a = a + 1
            print("None")
        if a > 30:
            cv2.destroyAllWindows()
            break
        '''
        if d == 0:
            Hand += 1
            print("Hand")
        if d == 1:
            Ok += 1
            print("Ok")
        if d == 2:
            Victory += 1
            print("Victory")
        if d == 3:
            print("None")
        if Hand >= 30:
            print("AAAAAAAAA")
            Hand = 0
            Ok = 0
            Victory = 0
        if Ok >= 30:
            print("BBBBBB")
            Hand = 0
            Ok = 0
            Victory = 0
        if Victory >= 30:
            print("CCCCCCCC")
            Hand = 0
            Ok = 0
            Victory = 0
        '''
filepath = '/home/dmitriy/PycharmProjects/untitled/venv/model.hf5'
#Загрузка нейронной сети(весов и т.д.)
# load json and create model
loaded_model = load_model( filepath, custom_objects=None, compile=True)
if __name__ == '__main__':
    Images_Capture()
