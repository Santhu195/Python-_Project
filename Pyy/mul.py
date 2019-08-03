import tkinter as tk
from tkinter import Message, Text
import cv2
import csv
import os
import numpy as np
from PIL import Image, ImageTk
import pandas as pd
import datetime
import time
import tkinter.ttk as ttk
import tkinter.font as font
#import setup as ss

def add_new():
    dict1 = ss.store_data()
    

    fieldnames = ['Name','Ids']
    with open('ss.csv','a+') as f:
        writer = csv.DictWriter(f , fieldnames = fieldnames)
        #writer.writeheader()
        writer.writerow(dict1)
    
#add_new()

reader = csv.DictReader(open('ss.csv'))
for rows in reader:
    result = dict(rows)
    print(result['Ids'])
    if result['Ids'] == '1':
        name = result['Name']
    elif result['Ids'] == '2':
        name = result["Name"]
    print(name)
        
    

df = pd.read_csv('ss.csv')
df.sort_values('Ids', inplace = True)
df.drop_duplicates(subset = 'Ids', keep = 'first', inplace = True)
#df.to_csv('ss.csv', index = False)
#print(df)