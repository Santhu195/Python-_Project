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

name , Id = '',''
dic = {
    'Name' : name,
    'Ids' : Id
}
def store_data():
    global name,Id,dic
    name = str(input("Enter Name  "))
   
    Id  = str(input("Enter Id   "))
   
    dic = {
        'Ids' : Id,
        'Name': name
    }

    c = dic
    
    

    #print(dic)
    return  c


def TakeImages():
    dict1 = store_data()
    fieldnames = ['Name','Ids']
    with open('ss.csv','w') as f:
        writer = csv.DictWriter(f, fieldnames =fieldnames)
        writer.writeheader()
        writer.writerow(dict1)
    #print(dict1)
    #name = "Santhu"
    #Id = '1'
    if (name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "hh.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = cam.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # Saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage\ " + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                # display the frame
            cv2.imshow('Cpaturing Face ', img)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 60:
                break
            
        
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for Name : " + name + Id
        print(res)
      
        #message.configure(text=res)
    else:
        if (name.isalpha()):
            res = "Enter Numeric Id"
            #message.configure(text=res)


TakeImages()
#print(dic)
