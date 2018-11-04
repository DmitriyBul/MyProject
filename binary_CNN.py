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


#paths to find train and test data
train_Big_Finger_dir = '/home/dmitriy/Documents/Dataset-1/'
train_Goat_dir = '/home/dmitriy/Documents/Dataset-2/'
train_Victory_dir = '/home/dmitriy/Documents/Dataset-3/'
train_No_Sign_dir = '/home/dmitriy/Documents/Dataset-4/'
test_hand_dir = '/home/dmitriy/Documents/Dataset_6/'
test_non_hand_dir = '/home/dmitriy/Documents/Dataset_5/'

#get data set count
train_Big_Finger_sample = len(os.listdir(train_Big_Finger_dir))
train_Goat_sample = len(os.listdir(train_Goat_dir))
train_Victory_sample = len(os.listdir(train_Victory_dir))
train_No_Sign_sample = len(os.listdir(train_No_Sign_dir))


test_hand_sample = len(os.listdir(test_hand_dir))
test_non_hand_sample = len(os.listdir(test_non_hand_dir))



print("Train Set samples- Big Finger-"+str(train_Big_Finger_sample)+" Goat-"+str(train_Goat_sample)+" Victory-"+str(train_Victory_sample)+" No Sign-"+str(train_No_Sign_sample))



#print("Test Set samples- HAND-"+str(test_hand_sample)+" NON_HAND-"+str(test_non_hand_sample))

train_x_data_set=np.zeros([train_Big_Finger_sample+train_Goat_sample+train_Victory_sample+train_No_Sign_sample,100,100,1])
print("shape of training data set: "+ str(train_x_data_set.shape))

train_y_data_set=np.array([])

#load images containing hand in train_x_data_set matrix
for index,filename in enumerate(os.listdir(train_Big_Finger_dir)):
    img = Image.open(train_Big_Finger_dir+filename)
    img = img.resize((100,100),Image.ANTIALIAS)
    im = np.array(img)
    train_x_data_set[index, :, :, :] = im
    train_y_data_set = np.append(train_y_data_set, 0)

for index,filename in enumerate(os.listdir(train_Goat_dir)):
    img = Image.open(train_Goat_dir+filename)
    img = img.resize((100,100),Image.ANTIALIAS)
    im = np.array(img)
    train_x_data_set[index, :, :, :] = im
    train_y_data_set = np.append(train_y_data_set, 1)

for index,filename in enumerate(os.listdir(train_Victory_dir)):
    img = Image.open(train_Victory_dir+filename)
    img = img.resize((100,100),Image.ANTIALIAS)
    im = np.array(img)
    train_x_data_set[index, :, :, :] = im
    train_y_data_set = np.append(train_y_data_set, 2)

#load images that does not contain hand in train_x_data_set matrix
for index,filename in enumerate(os.listdir(train_No_Sign_dir)):
    img = Image.open(train_No_Sign_dir+filename)
    img = img.resize((100,100),Image.ANTIALIAS)
    im = np.array(img)
    train_x_data_set[index, :, :] = im
    train_y_data_set = np.append(train_y_data_set, 3)



train_x_data_set = train_x_data_set/255
print(train_x_data_set)


#train_y_data_set=np.array([])


#train_y_data_set=np.append(np.append(np.append(np.append(train_y_data_set,[1]*train_Big_Finger_sample),[0.66]*train_Goat_sample),[0.33]*train_Victory_sample),[0]*train_No_Sign_sample)
train_y_data_set = keras.utils.to_categorical(train_y_data_set, num_classes = 4)
#print(train_y_data_set.shape)
#print("shape of train label:"+str(train_y_data_set.shape))
print(train_y_data_set)


model = Sequential()
model.add(Conv2D(8,(3,3),input_shape=(100,100,2),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2),strides=2))
model.add(Conv2D(12,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2),strides=2))
model.add(Conv2D(16,(3,3),activation='relu'))
model.add(MaxPooling2D(pool_size=(2,2)))
model.add(Flatten())
model.add(Dense(units=128,activation='relu'))
model.add(Dense(units=4,activation='sigmoid'))


model.compile(optimizer='adam',loss='categorical_crossentropy',metrics=['accuracy'])

model.fit(train_x_data_set,train_y_data_set,epochs=5)
#model.summary()

#test_x_data_set=np.zeros([test_hand_sample+test_non_hand_sample,100,100,3])
test_file_list = []


for index,filename in enumerate(os.listdir(test_hand_dir)):
    img = Image.open(test_hand_dir+filename)
    test_file_list.append(filename)
    img = img.resize((100,100),Image.ANTIALIAS)
    im = np.array(img)
    test_x_data_set[index,:,:,:]=im

#test_x_data_set = test_x_data_set/255

model_json = model.to_json()
with open("model.json", "w") as json_file:
    json_file.write(model_json)

model.save_weights("model.h5")
print("Saved model to disk")

test_x_data_set = np.zeros([1, 100, 100, 3])
for index in range(1):
    test_x_data_set[index, :, :, :] = img
d = model.predict(test_x_data_set)
print (d)
