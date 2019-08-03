import tkinter as tk
from tkinter import Message, Text
import cv2
import os
import csv
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
#import setup as ss


def DetectFace():
    reader = csv.DictReader(open('ss.csv'))
    for rows in reader:
        result = dict(rows)
        print(result)
        if result['Ids'] == '1':
            name1 = result['Name']
        elif result['Ids'] == '2':
            name2 = result["Name"]
    recognizer = cv2.face.LBPHFaceRecognizer_create()  #cv2.createLBPHFaceRecognizer()
    recognizer.read("TrainData\Trainner.yml")
    harcascadePath = "hh.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath);
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    # Camera ON Everytime
    while True:
        ret, frame = cam.read()
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.3, 5)
        for (x, y, w, h) in faces:
            cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 3)
            Id, confidence = recognizer.predict(gray[y:y + h, x:x + w])
            if (confidence < 85):
                if (Id == 1):
                    name = name1
                elif (Id == 2):
                    name = name2
                Predicted_name = str(name)
            else:
                Predicted_name = 'Unknown'
                noOfFile = len(os.listdir("UnknownFaces")) + 1
                if int(noOfFile) < 5:
                    cv2.imwrite("UnknownFaces\Image" + str(noOfFile) + ".jpg", frame[y:y + h, x:x + w])
                
                else:
                    pass


            cv2.putText(frame, str(Predicted_name), (x, y + h), font, 1, (255, 255, 255), 2)
        cv2.imshow('Picture', frame)
        if (cv2.waitKey(1) == ord('q')):
            break
DetectFace()

def add_new():
    
    dict2 = ss.store_data()
    fieldnames = ['Name','Ids']
    with open('ss.csv','a+') as f:
        writer = csv.DictWriter(f , fieldnames = fieldnames)
        #writer.writeheader()
        writer.writerow(dict2)
    
#add_new()