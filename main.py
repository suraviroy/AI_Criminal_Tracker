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
from record import record1, notepad1






cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': "https://facedetection-499f1-default-rtdb.firebaseio.com/",
    'storageBucket': "facedetection-499f1.appspot.com"
})








bucket = storage.bucket()
cap = cv2.VideoCapture(0)
# cap.set(3, 546)
# cap.set(4, 575)
imgBackground = cv2.imread('Resources/background11.png')

folderModePath = 'Resources/Modes'
modePathList = os.listdir(folderModePath)
imgModeList = []
for path in modePathList:
    imgModeList.append(cv2.imread(os.path.join(folderModePath, path)))
#print((imgModeList))


# Load the encoding file
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


path1 = 'Images'
os.chdir(path1)

counter=0
name1=''  
nameList=[]                
while True:
    success, img = cap.read()
    img=cv2.flip(img,1)
    imgS = cv2.resize(img,(0,0),None,0.25,0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS,facesCurFrame)

    #imgBackground[189:189 + 575, 808:808 + 546] = img
    imgBackground[205:205 + 480, 45:45 + 640] = img
    #imgBackground[44:44 + 695, 815:815 + 552] = imgModeList[0]

    k=cv2.waitKey(1)
    f=0
    # cv2.putText(imgBackground,'FINDING MATCH' , (900, 390),
    #                             cv2.FONT_HERSHEY_COMPLEX, 1.4, (31, 31, 31), 3)
    

    f=0
    for encodeFace,faceLoc in zip(encodesCurFrame,facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown,encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown,encodeFace)
        #print("matches", matches)
        #print("faceDis", faceDis)

        y1, x2, y2, x1 = faceLoc
        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
        bbox = 55 + x1, 162 + y1, x2 - x1, y2 - y1
        imgBackground = cvzone.cornerRect(imgBackground, bbox, rt=0)

        matchIndex = np.argmin(faceDis)
        if matches[matchIndex]:

            id = studentIds[matchIndex]

            nameList.append(id)
            counter=counter+1

            if(counter==11):
                f=1
                break

            # imgBackground[44:44 + 695, 815:815 + 552] = imgModeList[0]

            # cv2.putText(imgBackground,"Match Found" , (920, 160),
            #                     cv2.FONT_HERSHEY_COMPLEX, 1.4, (0, 0, 0), 3)

            # # cv2.putText(imgBackground,id , (1030, 400),
            # #                     cv2.FONT_HERSHEY_COMPLEX, 1, (100, 100, 100), 2)
            # (w, h), _ = cv2.getTextSize(id, cv2.FONT_HERSHEY_COMPLEX, 1, 1)
            # offset = (530 - w) // 2
            # cv2.putText(imgBackground, str(id), (820 + offset, 530),
            #                     cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)
            
            # cv2.putText(imgBackground,'Press "Space Bar" to open his/her file' , (850, 640),
            #                     cv2.FONT_HERSHEY_COMPLEX, 0.7, (100, 100, 100), 2)
            # cv2.putText(imgBackground,'Press "ESC" to close' , (950, 680),
            #                     cv2.FONT_HERSHEY_COMPLEX, 0.7, (100, 100, 100), 2)

            print(studentIds[matchIndex])
            
            # fileName=id+'.PNG'
            # #img2=Image.open(fileName) 
            # with open(fileName, "rb") as image:
            #     f = image.read()
            #     image = np.asarray(bytearray(f))
            #     image = cv2.imdecode(image, 3)
            # imgBackground[250:250 + 216, 970:970 + 216] = image


            # blob = bucket.get_blob(f'Images/{id}.png')
            # array = np.frombuffer(blob.download_as_string(), np.uint8)
            # imgStudent = cv2.imdecode(array, cv2.COLOR_BGRA2BGR)
            # imgBackground[175:175 + 216, 909:909 + 216] = imgStudent

            # f=open('C:/hackathon/Machine Learning/Face Recgnition/Details/'+id+'.txt',"r")
            # t=f.read()

            # if(k%256==32):
            #     f=1
            #     break
        else:
            print("Not Recognize")
            nameList.append("Not Recognize")
            counter=counter+1
            if(counter==11):
                f=1
                break





    if(f==1):
        temp=defaultdict(int)
        for wrd in nameList:
            temp[wrd]+=1
            res=max(temp, key=temp.get)#max number of time the person is detected
        name1=str(res)
        print("final Name=",name1)

        imgBackground[44:44 + 695, 815:815 + 552] = imgModeList[0]
        
        if(name1 != "Not Recognize"):
            #cv2.putText(imgBackground,"Match Found" , (920, 160),
            #                        cv2.FONT_HERSHEY_COMPLEX, 1.4, (136, 8, 8), 3)

            (w, h), _ = cv2.getTextSize(name1, cv2.FONT_HERSHEY_COMPLEX, 1, 1)
            offset = (530 - w) // 2
            cv2.putText(imgBackground, str(name1), (820 + offset, 530),
                                cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,0), 2)
                
            cv2.putText(imgBackground,'Press "Space Bar" to open his/her file' , (850, 640),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.7, (100, 100, 100), 2)
            cv2.putText(imgBackground,'Press "ESC" to close' , (950, 680),
                                    cv2.FONT_HERSHEY_COMPLEX, 0.7, (100, 100, 100), 2)

            

            fileName=name1+'.PNG'
                #img2=Image.open(fileName) 
            with open(fileName, "rb") as image:
                f = image.read()
                image = np.asarray(bytearray(f))
                image = cv2.imdecode(image, 3)
            imgBackground[230:230 + 216, 970:970 + 216] = image
            

        

        else:

            n='C:/hackathon/Machine Learning/Face Recgnition/Resources/not.png'
            with open(n, "rb") as image:
                f = image.read()
                image = np.asarray(bytearray(f))
                image = cv2.imdecode(image, 3)
            imgBackground[44:44 + 695, 815:815 + 552] = image

        counter=0
        f=0
        nameList=[]
        




    if(k%256==32 and name1!='' and name1!="Not Recognize"):
        # print("Opening File")
        # programName = "notepad.exe"
        # fileName = 'C:/hackathon/Machine Learning/Face Recgnition/Details/'+name1+'.txt'
        # sp.Popen([programName, fileName])
        record1(name1)

            

    


            
    cv2.imshow("Face Recognition", imgBackground)

    if  k%256 == 27:
        break
cap.release()
cv2.destroyAllWindows()



