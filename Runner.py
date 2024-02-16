from tkinter import *
from subprocess import call
import tkinter as tk

root=Tk()

root.title('Face Recognition')
root.geometry("1200x700")
#root.configure(bg="#2edaff")
#bg = PhotoImage(file = "Resources/AddPerson.png")
bg = PhotoImage(file = 'Resources/background88.png')
label1 = Label(root, image = bg)
label1.place(x = 0, y = 0)

bg1 = PhotoImage(file = "Resources/add1.png")
label2 = Label(root, image = bg1,highlightbackground="#050A80", highlightthickness=5)
label2.place(x = 120, y = 280)

# pi = PhotoImage(file = 'Resources/more.png')

# root.wm_attributes('-transparentcolor', 'black')

def add():
    call(["python","self.py"])


def detect():
    call(["python","main.py"])
    #recg()

def data():
    call(["python","Database.py"])


b=Button(root, text="Add Person", font=("times new roman",20, "bold"),bg="#5DBDFA", fg="#050A80",bd=5, command=add,activeforeground="#000000")
b.place(x=140, y=525)

# b=Button(root, image= pi, command=add)
# b.place(x=100, y=525)
# label33 = Label(root, text="reccgg")
# label33.place(x = 100, y = 525)

bg2 = PhotoImage(file = "Resources/Detect1.png")
label3 = Label(root, image = bg2,highlightbackground="#050A80", highlightthickness=4)
label3.place(x = 500, y = 278)

b1=Button(root, text="Recognition", font=("times new roman",20, "bold"),bg="#5DBDFA", fg="#050A80",bd=5, command=detect,activeforeground="#000000")
b1.place(x=520, y=525)

bg3 = PhotoImage(file = "Resources/hhhh.PNG")
label4 = Label(root, image = bg3,highlightbackground="#050A80", highlightthickness=5)
label4.place(x = 880, y = 278)
b3=Button(root, text="Database", font=("times new roman",20, "bold"),bg="#5DBDFA", fg="#050A80",bd=5, command=data,activeforeground="#000000")
b3.place(x=920, y=525)
mainloop()