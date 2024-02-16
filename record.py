from collections import defaultdict
from tkinter import messagebox
from tkinter import *
from tkinter import ttk
from PIL import Image
import subprocess as sp
import numpy as np
import os
from Addcase import addRecords

def notepad1(name1):
    print("Opening File")
    programName = "notepad.exe"
    fileName = 'C:/hackathon/Machine Learning/Face Recgnition/Details/'+name1+'.txt'
    sp.Popen([programName, fileName])



def EditInfo(name2):

    def save_details():
        content = my_txt.get("1.0", "end-1c")
        with open(fileName1, 'w') as file:
            file.write(content)
        #messagebox.showinfo("Update Details","Information saved")
        root1.destroy()

    root1=Tk()
    #print("hello")
    root1.title('Gemeral Info')
    root1.geometry("950x610")
    #root1.configure(bg="#33CCFF")
    # bge = PhotoImage(file = 'C:/hackathon/Machine Learning/Face Recgnition/Resources/detail.png')
    # label2 = Label(root1, image = bge)
    # label2.place(x = 0, y = 0)
    label1 = Label(root1, text = "General Information", fg = "Red",font=("times new roman",20, "bold"))  
    label1.place(x=350,y=10) 
    label = Label(root1, text ="Edit Information of "+name2, fg = "Red",font=("times new roman",15))  
    label.place(x=53, y=90) 
    fileName1 = 'C:/hackathon/Machine Learning/Face Recgnition/Details/'+name2+'/'+name2+'.txt'
    txt_file=open(fileName1,'r')
    stuff=txt_file.read()
    my_txt=Text(root1,width=90 ,height=18 ,font=("times new roman",14),highlightbackground="#33CCFF", highlightthickness=5)
    my_txt.place(x=50,y=130)
    my_txt.insert(END,stuff)
    b=Button(root1, text="Save", font=("times new roman",18, "bold"), fg="black",bg="green",activeforeground="#000000", command=save_details)
    # b.bind("<Button>",
    #     lambda e: save_details)
    b.place(x=790, y=540)

    b1=Button(root1, text="Close", font=("times new roman",18, "bold"), fg="black",bg="red",activeforeground="#000000",command=root1.destroy)
    # b1.bind("<Button>",
    #     lambda e: EditInfo(name))
    b1.place(x=700, y=540)

    mainloop()
#EditInfo("Suravi Roy")

def openfile1(count,name4):
    root3=Tk()
    root3.title('Record Number '+str(count))
    root3.geometry("1000x610")
    fileName1 ='C:/hackathon/Machine Learning/Face Recgnition/Details/'+name4+'/Records/'+name4+"_"+str(count)+".txt"
    txt_file=open(fileName1,'r')
    stuff=txt_file.read()
    my_txt=Text(root3,width=90 ,height=20 ,font=("times new roman",14),highlightbackground="#33CCFF", highlightthickness=6)
    my_txt.place(x=90,y=65)
    my_txt.insert(END,stuff)
    my_txt.config(state=DISABLED)
    label = Label(root3, text ="Record Number "+count, fg = "Red",font=("times new roman",16,"bold"))  
    label.place(x=450, y=20)
    b1=Button(root3, text="Close", font=("times new roman",15), fg="Black",bg="red",activeforeground="#000000",command=root3.destroy)
    b1.place(x=825, y=520)
    mainloop()


# def get_button(t):
#    print(t)


def ShowRecord(name3):


    root2=Tk()
    #print("hello")

    root2.title(name3+' Case History')
    root2.geometry("1000x610")
    label = Label(root2, text ="Record History", fg = "Red",font=("times new roman",22,"bold"))  
    label.place(x=373, y=20) 
    b=Button(root2, text="Add Records", font=("times new roman",11), fg="black",bg="red",activeforeground="#000000")
    b.bind("<Button>",
        lambda e: addRecords(name3))
    b.place(x=840, y=31)
    dir_path = 'C:/hackathon/Machine Learning/Face Recgnition/Details/'+name3+'/Records'
    count = 1
    y1=140
    for path in os.listdir(dir_path):
        if os.path.isfile(os.path.join(dir_path, path)):
           
            b=Button(root2, text="Open", font=("times new roman",16, "bold"), fg="Red",activeforeground="#000000",command= lambda t= str(count): openfile1(t,name3))
            # b.bind("<Button>",
            # lambda e: openfile1(dir_path+"/"+str(count)+".txt",count))
            b.place(x=890, y=y1)
             
            path1=dir_path+"/"+name3+"_"+str(count)+".txt"
            file=open(path1,"r")
            lines=file.readlines()
            file.close()
            totalLines=len(lines)
            #print(totalLines)
            lineTxt=lines[totalLines-1]
            #print(lineTxt[23:])
            label1 = Label(root2, text ="Record number "+str(count), fg = "Red",font=("times new roman",15,"bold"))  
            label1.place(x=40, y=y1)
            label = Label(root2, text =lineTxt[23:], fg = "Red",font=("times new roman",15))  
            label.place(x=400, y=y1)
            y1+=65 
            count += 1

     
    #print('File count:', count)
    mainloop()

#ShowRecord("Suravi Roy")

def record1(name):
    
    root=Tk()
    # print("hello")
    root.title('Details')
    root.geometry("1000x600")
    bg = PhotoImage(file = 'C:/hackathon/Machine Learning/Face Recgnition/Resources/detail.png')
    #bg = PhotoImage(file='./Resources/detail.png')
    label1 = Label(root, image = bg)
    label1.place(x = 0, y = 0)
    # main_fame=Frame(root)
    # main_fame.pack(fill=BOTH , expand=1)
    # my_canvas= Canvas(main_fame)
    # my_canvas.pack(side=LEFT, fill=BOTH, expand=1)
    # my_scroll=ttk.Scrollbar(main_fame, orient=VERTICAL ,command=my_canvas.yview)
    # my_scroll.pack(side=RIGHT, fill=Y)
    # my_canvas.configure(yscrollcommand=my_scroll.set)
    # my_canvas.bind('<Configure>', lambda e: my_canvas.configure(scrollregion=my_canvas.bbox("All")))

    canvas= Canvas(root, width= 1000, height= 600)

    filee='C:/hackathon/Machine Learning/Face Recgnition/Images/'+name+'.png'
    bg3 = PhotoImage(file = filee)
    label4 = Label(root, image = bg3,highlightbackground="#33CCFF", highlightthickness=5)
    label4.place(x = 25, y = 70)
    label = Label(root, text = name, fg = "Red",font=("times new roman",20, "bold"))  
    label.place(x=50, y=330) 

    Label(root, text="General Information:", font=("times new roman", 14), fg="black").place(x=305, y=15)
    
    b=Button(root, text="Show Records", font=("times new roman",15), fg="red",activeforeground="#000000")
    b.bind("<Button>",
        lambda e: ShowRecord(name))
    b.place(x=70, y=435)

    b1=Button(root, text="Edit Info", font=("times new roman",15), fg="red",activeforeground="#000000")
    b1.bind("<Button>",
        lambda e: EditInfo(name))
    b1.place(x=25, y=490)

    b2=Button(root, text="Add Record", font=("times new roman",15), fg="red",activeforeground="#000000")
    b2.bind("<Button>",
        lambda e: addRecords(name))
    b2.place(x=130, y=490)

    fileName1 = 'C:/hackathon/Machine Learning/Face Recgnition/Details/'+name+'/'+name+'.txt'
    txt_file=open(fileName1,'r')
    stuff=txt_file.read()
    my_txt=Text(root,width=50 ,height=18 ,font=("times new roman",18),highlightbackground="#33CCFF", highlightthickness=6)
    my_txt.place(x=290,y=55)
    my_txt.insert(END,stuff)
    my_txt.config(state=DISABLED)
    mainloop()


#record1("Knaa")