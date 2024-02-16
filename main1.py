import cv2
import numpy as np
from tkinter import *
from PIL import Image, ImageTk
import datetime
import os
import pickle
import face_recognition
import cvzone
import webbrowser
from collections import defaultdict
import subprocess as sp




root = Tk()
root.geometry("1000x2000")
root.configure(bg="black")
Label(root, text="Fruad Detection System", font=("times new roman", 30,"bold"),bg="black", fg="red").pack()
f1 = LabelFrame(root, bg="red")
f1.pack(padx=12, pady=3, side=LEFT)
L1 = Label(f1, bg="black",padx=40)
L1.pack(padx=2, pady=3, side=LEFT)

def photo(id):
    programName = "notepad.exe"
    fileName = 'C:/hackathon/Machine Learning/Face Recgnition/Details/'+id+'.txt'
    sp.Popen([programName, fileName])




print("Loading Encode File ...")
file = open('EncodeFile.p', 'rb')
encodeListKnownWithIds = pickle.load(file)
file.close()
encodeListKnown, studentIds = encodeListKnownWithIds
print(studentIds)
print("Encode File Loaded")

path = 'Images'
images = []
classNames = []
myList = os.listdir(path)
#print(myList)
for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

cap = cv2.VideoCapture(0)

path1 = 'Images'
os.chdir(path1)
name_list=[]
x=0
while True:
    success, img = cap.read()
    img1 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = ImageTk.PhotoImage(Image.fromarray(img1))
    L1['image'] = img
    root.update()
    img2=Image.fromarray(img1)

    imgS = cv2.resize(img1,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)
    f=0
    name1=''
    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        #print("matches", matches)
        #print("faceDis", faceDis)
        
        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:

            id = studentIds[matchIndex]
            print(studentIds[matchIndex])

            name_list.append(id)
            x=x+1

            y1, x2, y2, x1 = faceLoc
            y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
            bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
            img1 = cvzone.cornerRect(img1, bbox, rt=0)
            
            if(x==6):
                f=1
                break
            
            # fileName=id+'.PNG'
            # frame = Frame(root, width=600, height=400)
            # frame.pack(padx=12, pady=3, side=LEFT)
            # img = ImageTk.PhotoImage(Image.open(fileName))
            # label = Label(frame, image = img)
            # label.pack(padx=2, pady=3, side=LEFT)
        else:
            print("Not Recognize")
            name_list.append("Not Recognize")
            x=x+1
            if(x==6):
                f=1
                break
    if(f==1):
        temp=defaultdict(int)
        for wrd in name_list:
            temp[wrd]+=1
        res=max(temp, key=temp.get)#max number of time the person is detected
        name1=str(res)
        print("final Name=",name1) 
        fileName=name1+'.PNG'
        frame = Frame(root, width=216, height=216)
        frame.pack(padx=300, pady=20, side=TOP)
        img6 = ImageTk.PhotoImage(Image.open(fileName))
        label1 = Label(frame, image = img6)
        label1.pack(padx=2, pady=3, side=TOP)
        Label(root, text=name1,font=("times new roman", 30,"bold"),bg="black", fg="white").place(x=100,y=100)
        # Label(root, text=name1 ,font=("times new roman", 30,"bold"),bg="black", fg="red").pack()
        # f=open('C:/hackathon/Machine Learning/Face Recgnition/Details/'+name1+'.txt',"r")
        # t=f.read()
        # Button(root, text="View File", font=("times new roman",20, "bold"),bg="black", fg="red", command=photo(name1)).pack(padx=10, pady=3)
        #Label(root, text=t ,width = 50, height = 50,font=("times new roman", 30,"bold"),bg="black", fg="white").pack(side=RIGHT)
        # text=Text(root, width = 50, height = 50, 
        #   wrap = WORD, padx = 10, pady = 10)
        x=0
        f=0
        name_list=[]

    k=cv2.waitKey(1)
    if  k%256 == 27:
        break



cap. release()
cv2.destroyAllWindows()
