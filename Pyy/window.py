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

window = tk.Tk()
# helv36 = tk.Font(family='Helvetica', size=36, weight='bold')
window.title("Face_Recogniser")

dialog_title = 'QUIT'
dialog_text = 'Are you sure?'
# answer = messagebox.askquestion(dialog_title, dialog_text)

# window.geometry('1280x720')
window.configure(background='blue')

# window.attributes('-fullscreen', True)

window.grid_rowconfigure(0, weight=1)
window.grid_columnconfigure(0, weight=1)
message = tk.Label(window, text="Face-Recognition Santhosh", bg="Green", fg="white", width=50,
                   height=3, font=('times', 30, 'italic bold underline'))

message.place(x=200, y=20)

lbl = tk.Label(window, text="Enter Name", width=20, height=2, fg="red", bg="yellow", font=('times', 15, ' bold '))
lbl.place(x=400, y=200)

txt = tk.Entry(window, width=20, bg="yellow", fg="red", font=('times', 15, ' bold '))
txt.place(x=700, y=215)


lbl3 = tk.Label(window, text="Notification : ", width=20, fg="red", bg="yellow", height=2,
                font=('times', 15, ' bold underline '))
lbl3.place(x=400, y=400)

message = tk.Label(window, text="", bg="yellow", fg="red", width=30, height=2, activebackground="yellow",
                   font=('times', 15, ' bold '))
message.place(x=700, y=400)

def clear():
    txt.delete(0, 'end')
    res = ""
    message.configure(text=res)

def TakeImages():
    name = (txt.get())
    if (name.isalpha()):
        cam = cv2.VideoCapture(0)
        harcascadePath = "hh.xml"
        detector = cv2.CascadeClassifier(harcascadePath)
        sampleNum = 0
        while (True):
            ret, img = Video.read()
            gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            faces = detector.detectMultiScale(gray, 1.3, 5)
            for (x, y, w, h) in faces:
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage\ " + name + "." + Id + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                # display the frame
                cv2.imshow('frame', img)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for Name : " + name

        message.configure(text=res)
    else:
        if (name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text=res)
def TakeImages():
    name = (txt.get())
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
                cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
                # incrementing sample number
                sampleNum = sampleNum + 1
                # Saving the captured face in the dataset folder TrainingImage
                cv2.imwrite("TrainingImage\ " + name + '.' + str(sampleNum) + ".jpg", gray[y:y + h, x:x + w])
                # display the frame
            cv2.imshow('frame', img)
            # wait for 100 miliseconds
            if cv2.waitKey(100) & 0xFF == ord('q'):
                break
            # break if the sample number is morethan 100
            elif sampleNum > 60:
                break
        cam.release()
        cv2.destroyAllWindows()
        res = "Images Saved for Name : " + name

        message.configure(text=res)
    else:
        if (name.isalpha()):
            res = "Enter Numeric Id"
            message.configure(text=res)


clearButton = tk.Button(window, text="Clear", command=clear, fg="red", bg="yellow", width=20, height=2,
                        activebackground="Red", font=('times', 15, ' bold '))
clearButton.place(x=950, y=200)

takeImg = tk.Button(window, text="Take Images", command=TakeImages, fg="red", bg="yellow", width=20, height=3,
                    activebackground="Red", font=('times', 15, ' bold '))
takeImg.place(x=200, y=500)

quitWindow = tk.Button(window, text="Quit", command=window.destroy, fg="red", bg="yellow", width=20, height=3,
                       activebackground="Red", font=('times', 15, ' bold '))
quitWindow.place(x=1100, y=500)


copyWrite = tk.Text(window, background=window.cget("background"), borderwidth=0,
                    font=('times', 30, 'italic bold underline'))
copyWrite.tag_configure("superscript", offset=10)
copyWrite.insert("insert", "Developed by Santhosh")
copyWrite.configure(state="disabled", fg="red")
copyWrite.pack(side="left")
copyWrite.place(x=800, y=750)

window.mainloop()