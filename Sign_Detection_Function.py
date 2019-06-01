import time
import os
import numpy as np
from PIL import Image
import timeit
from keras.models import model_from_json
from keras.models import load_model
import cv2

def Reset(r0, r1):
    if r1 == 1:
        r0 = 0
    return(r0)    
    
def Images_Capture():
    variable_0 = 0
    variable_1 = 0
    variable_2 = 0
    variable_3 = 0
    cap = cv2.VideoCapture(0)

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
            variable_0 += 1
            print("Hand")
        if d == 1:
            variable_1 += 1
            print("Ok")
        if d == 2:
            variable_2 += 1
            print("Victory")
        if d == 3:
            variable_3 = 1
            print("None")
        variable_0 = variable_1 = variable_2 = Reset(variable_0, variable_3)
        
        if variable_0 >= 7:
            cv2.destroyAllWindows()
            break
            return(d)
        elif variable_1 >= 7:
            cv2.destroyAllWindows()
            break
            return(d)
        elif variable_2 >= 7:
            cv2.destroyAllWindows()
            break
            return(d)
        variable_3 = 0
        #if a > 30:
           # cv2.destroyAllWindows()
           # break
        print(variable_0, variable_1, variable_2, variable_3)

filepath = '/home/pi/Documents/model.hf5'

loaded_model = load_model( filepath, custom_objects=None, compile=True)
if __name__ == '__main__':
    Images_Capture()
    print("aqwe")