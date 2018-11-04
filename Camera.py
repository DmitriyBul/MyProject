import cv
import time
import os
import numpy as np
import cv2

b = []

capture = cv.CaptureFromCAM(-1)
cv.NamedWindow("capture", cv.CV_WINDOW_AUTOSIZE)
i = 0
while True:
    frame = cv.QueryFrame(capture)
    cv.ShowImage("capture", frame)
    cv.WaitKey(10)

    path = "%.4d.jpg" % i
    cv.SaveImage(path, frame)
    i += 1
    time.sleep(1)
    #os.remove("capture0000.jpg")

#Reading images in folder
    #for k in range(1,1001):
       # img = cv2.imread("{id:04d}.jpg".format(id=k))
       # a.append(img)
        #print(a)
    if i > 8:
        if i < 5:
            j = i
        else:
            j = i - 4
        a = open("{id:04d}.jpg".format(id=i), "r")
        #c = os.path.splitext(a.name)[0]
        #c = int(c)
        #print(a.name)
        b.append(a.name)
        if len(b) > 5:
            #print(b[k])
            os.remove("{id:04d}.jpg".format(id=j))