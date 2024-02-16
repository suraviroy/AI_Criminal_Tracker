import tkinter as tk
from tkinter import filedialog
import os
import util
from tkinter import*
import datetime


def addRecords(name1):
    def save_text(name):
        text = text_box.get("1.0", tk.END)
        base_path ='C:/hackathon/Machine Learning/Face Recgnition/Details/'+name
        case_number = 1
        dir1path = os.path.join(base_path,'Records')
        if not os.path.exists(dir1path):
                os.makedirs(dir1path)
        file_path = f"{dir1path}/{name}_{case_number}.txt"

        while os.path.exists(file_path):
            case_number += 1
            file_path = f"{dir1path}/{name}_{case_number}.txt"

        with open(file_path, "w") as file:
            file.write(text)
            file.write('{}:{}\n'.format("\nregister date and time", datetime.datetime.now()))
            util.msg_box('Success!', 'Case is recorded successfully !')
        root.destroy()



    root = tk.Tk()
    root.title("Add Case")
    root.geometry("850x510")


    label1 = Label(root, text = "Add Records", fg = "Red",font=("times new roman",20, "bold"))  
    label1.place(x=350,y=30) 
    text_box = tk.Text(root,width=75 ,height=14 ,font=("times new roman",14),highlightbackground="#33CCFF", highlightthickness=5)
    text_box.place(x=80,y=100)

    save_button = tk.Button(root, text="Save",font=("times new roman",18, "bold"), fg="black",bg="green",activeforeground="#000000", command=lambda: save_text(name1))
    save_button.place(x=400,y=430)

    root.mainloop()

#addRecords("Knaa")