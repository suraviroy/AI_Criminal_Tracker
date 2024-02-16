import tkinter
import cv2
import os
import pickle
import cv2
import face_recognition
import cvzone
from tkinter import *
from tkinter import ttk
from PIL import Image
import webbrowser
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage
import numpy as np
from datetime import datetime
import subprocess as sp
from collections import defaultdict
from tkinter import messagebox

# def record1(name):
#     root=tkinter.Toplevel()
#     # print("hello")
#     root.title('Details')
#     root.geometry("1000x600")
#     bg = PhotoImage(file = './Resources/detail.png')
#     label1 = Label(root, image = bg)
#     label1.place(x = 0, y = 0)
#     # main_fame=Frame(root)
#     # main_fame.pack(fill=BOTH , expand=1)
#     # my_canvas= Canvas(main_fame)
#     # my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
#     # my_scroll=ttk.Scrollbar(main_fame, orient=VERTICAL ,command=my_canvas.yview)
#     # my_scroll.pack(side=RIGHT, fill=Y)
#     # my_canvas.configure(yscrollcommand=my_scroll.set)
#     # my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("All")))

#     canvas= Canvas(root, width= 1000, height= 600)

#     filee='./Images/'+name+'.png'
#     bg3 = PhotoImage(file = filee)
#     label4 = Label(root, image = bg3,highlightbackground="black", highlightthickness=5)
#     label4.place(x = 25, y = 80)
#     label = Label(root, text = name, fg = "RED",font=("times new roman",20, "bold"))  
#     label.place(x=15, y=370) 

#     fileName1 = './Details/'+name+'.txt'
#     txt_file=open(fileName1,'r')
#     stuff=txt_file.read()
#     my_txt=Text(root,width=50 ,height=20 ,font=("times new roman",18),highlightbackground="black", highlightthickness=3)
#     my_txt.place(x=290,y=30)
#     my_txt.insert(END,stuff)
#     txt_file.close()
#     mainloop()
def record1(name):
    def save_details():
        content = my_txt.get("1.0", "end-1c")
        with open(fileName1, 'w') as file:
            file.write(content)
        messagebox.showinfo("Update Details","Information saved")

    root = tkinter.Toplevel()
    root.title('Details')
    root.geometry("1000x600")
    bg = PhotoImage(file='./Resources/detail.png')
    label1 = Label(root, image=bg)
    label1.place(x=0, y=0)

    canvas = Canvas(root, width=1000, height=600)

    filee = './Images/' + name + '.png'
    bg3 = PhotoImage(file=filee)
    label4 = Label(root, image=bg3, highlightbackground="black", highlightthickness=5)
    label4.place(x=25, y=80)
    label = Label(root, text=name, fg="RED", font=("times new roman", 18, "bold"))
    label.place(x=25, y=370)

    fileName1 = './Details/' +name+'/'+ name + '.txt'
    txt_file = open(fileName1, 'r')
    stuff = txt_file.read()
    txt_file.close()

    my_txt = Text(root, width=50, height=20, font=("times new roman", 18), highlightbackground="black",
                  highlightthickness=3)
    my_txt.place(x=290, y=30)
    my_txt.insert(END, stuff)

    save_button = Button(root, text="Save",font= ("Castellar",15, "bold"),bg="white", fg="blue", command=save_details)
    save_button.grid(padx=0, pady=0)
    save_button.place(x=50, y=500)

    mainloop()

