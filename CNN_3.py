#!/usr/bin/env python
# -*- coding: utf-8 -*-
from PIL import Image
import matplotlib as plt
import numpy as np
import os
import timeit
import keras
from keras.models import Sequential
from keras.layers import Conv2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.layers import Dropout
from os.path import basename
#paths to find train and test data
train_Hand_dir = '/home/dmitriy/Documents/Dataset_5/'


train_Hand_sample = len(os.listdir(train_Hand_dir))



train_x_data_set=np.zeros([396,100,100,3])
print("shape of training data set: "+ str(train_x_data_set.shape))

train_y_data_set=np.array([])

#load images containing hand in train_x_data_set matrix


train_y_data_set = np.append(train_y_data_set, 0)
train_y_data_set = np.append(train_y_data_set, 1)
#train_y_data_set = np.append(train_y_data_set, 1)
for k in range(2, 396):
    img = Image.open("{id}.jpg".format(id=k))
    img = img.resize((100, 100), Image.ANTIALIAS)
    im = np.array(img)
    train_x_data_set[k, :, :, :] = im
    if k%2 == 0:
        train_y_data_set = np.append(train_y_data_set, 0)
    else:
        train_y_data_set = np.append(train_y_data_set, 1)



#load images that does not contain hand in train_x_data_set matrix




train_x_data_set = train_x_data_set/255
print(train_x_data_set)


#train_y_data_set=np.array([])


train_y_data_set = keras.utils.to_categorical(train_y_data_set, num_classes = 2)
#print(train_y_data_set.shape)
#print("shape of train label:"+str(train_y_data_set.shape))
print(train_y_data_set)


model = Sequential()
model.add(Conv2D(8,(3,3),input_shape=(100,100,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(12,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Conv2D(16,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Dropout(0.5))
model.add(Flatten())
model.add(Dense(units=128,activation='relu'))
model.add(Dense(units=2,activation='softmax'))
model.summary()

model.compile(optimizer='adam',loss='binary_crossentropy',metrics=['accuracy'])

model.fit(train_x_data_set,train_y_data_set,epochs=3)


model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("model.h5")