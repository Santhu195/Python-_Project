import tkinter as tk
from tkinter import Message, Text
import cv2, os
import shutil
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font





face_cascade = cv2.CascadeClassifier('hh.xml')
video = cv2.VideoCapture(0)

m = 1
a, b, c, d = 0,0,0,0
sample = 0
while True:
    m = m + 1

    check, frame = video.read()
    gray_img = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray_img, scaleFactor=1.05, minNeighbors=5)
    img = cv2.rectangle(frame, (a, b), (a + c, b + d), (0, 255, 0), 3)

    for x, y, h, w in faces:
        img = cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
        #cv2.imwrite("TrainingImage\ " + name + "." + Id + '.' + str(sample) + ".jpg", gray[y:y + h, x:x + w])

    cv2.imshow('capturing', img)
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

# print(check)
# print(frame)

# time.sleep(3)


video.release()

cv2.destroyAllWindows()