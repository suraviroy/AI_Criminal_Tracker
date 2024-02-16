import os.path
import datetime
import pickle
import numpy as np
import tkinter as tk
import cv2
from PIL import Image, ImageTk
import face_recognition
from subprocess import call
import util
#from tkinter import *
# from test import test
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


class App:
    def __init__(self):
        self.main_window = tk.Tk()
        self.main_window.title('Add Person')
        self.main_window.geometry("1200x620+100+100")
        self.main_window.configure(bg="#2edaff")
        #bg = PhotoImage(file = "Resources/AddPerson.png")
        # label1 = Label(self.main_window.configure, image = bg)
        # label1.place(x = 0, y = 0)
        # self.login_button_main_window = util.get_button(self.main_window, 'login', 'green', self.login)
        # self.login_button_main_window.place(x=750, y=200)

        # self.logout_button_main_window = util.get_button(self.main_window, 'logout', 'red', self.logout)
        # self.logout_button_main_window.place(x=750, y=300)


        self.text_label= util.get_text_label(self.main_window, 'Add New Person')
        self.text_label.place(x=550, y=30)
        self.register_new_user_button_main_window = util.get_button(self.main_window, 'Click Picture', 'gray',
                                                                    self.register_new_user, fg='black')
        self.register_new_user_button_main_window.place(x=750, y=400)

        self.webcam_label = util.get_img_label(self.main_window)
        self.webcam_label.place(x=10, y=90, width=650, height=490)

        self.add_webcam(self.webcam_label)

        # self.db_dir = './db'
        # if not os.path.exists(self.db_dir):
        #     os.mkdir(self.db_dir)
        self.db1_dir = './Images'
        if not os.path.exists(self.db1_dir):
            os.mkdir(self.db1_dir)
        self.db2_dir = './Details'
        if not os.path.exists(self.db2_dir):
            os.mkdir(self.db2_dir)

    #     self.log_path = './log.txt'

    def add_webcam(self, label):
        
        #   cv2.VideoCapture(0)
          if 'cap' not in self.__dict__:
              self.cap = cv2.VideoCapture(0)

          self._label = label
          self.process_webcam()

    def process_webcam(self):
        ret, frame = self.cap.read()
        frame=cv2.flip(frame,1)
        self.most_recent_capture_arr = frame
       
       
        img_= cv2.cvtColor(self.most_recent_capture_arr, cv2.COLOR_BGR2RGB)
       
        self.most_recent_capture_pil = Image.fromarray(img_)
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        self._label.imgtk = imgtk
        self._label.configure(image=imgtk)

        self._label.after(20, self.process_webcam)

   
   


    def register_new_user(self):
        
        self.register_new_user_window = tk.Toplevel(self.main_window)
        self.register_new_user_window.geometry("1200x520+120+120")
        self.register_new_user_window.title('Add Details')

        self.accept_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Save', 'green', self.accept_register_new_user)
        self.accept_button_register_new_user_window.place(x=750, y=300)

        self.try_again_button_register_new_user_window = util.get_button(self.register_new_user_window, 'Close', 'red', self.try_again_register_new_user)
        self.try_again_button_register_new_user_window.place(x=750, y=400)
        
       


        self.capture_label = util.get_img_label(self.register_new_user_window)
        self.capture_label.place(x=10, y=0, width=700, height=500)

        self.add_img_to_label(self.capture_label)

        self.entry_text_register_new_user = util.get_entry_text(self.register_new_user_window)
        self.entry_text_register_new_user.place(x=750, y=70)

        self.text_label_register_new_user = util.get_text_label(self.register_new_user_window, 'Please,input username:')
        self.text_label_register_new_user.place(x=750, y=40)
        self.entry_description_register_new_user = util.get_entry_description(self.register_new_user_window)
        self.entry_description_register_new_user.place(x=750, y=150)

        self.description_label_register_new_user = util.get_description_label(self.register_new_user_window, 'Please,input description:')
        self.description_label_register_new_user.place(x=750, y=120)


    def try_again_register_new_user(self):
        self.register_new_user_window.destroy()

    def add_img_to_label(self, label):
        imgtk = ImageTk.PhotoImage(image=self.most_recent_capture_pil)
        label.imgtk = imgtk
        label.configure(image=imgtk)

        self.register_new_user_capture = self.most_recent_capture_arr.copy()

    def start(self):
        self.main_window.mainloop()
    
    

    def accept_register_new_user(self):
        
        name = self.entry_text_register_new_user.get(1.0, "end-1c")
        des = self.entry_description_register_new_user.get(1.0, "end-1c")
        faces = face_cascade.detectMultiScale(self.register_new_user_capture, 1.1, 4)
        
        for (x, y , w ,h) in faces:
            #cv2.rectangle(self.register_new_user_capture, (x,y), (x+w, y+h), (255, 0 , 0), 1)
            faces = self.register_new_user_capture[y:y + h+8, x:x + w+8]
            
            cv2.imwrite(os.path.join(self.db1_dir, '{}.png'.format(name)), faces)
            image = Image.open('./Images/{}.png'.format(name))
            new_image = image.resize((216, 216))
            new_image.save('./Images/{}.png'.format(name))
          
            
        dirpath = os.path.join(self.db2_dir,name)
        if not os.path.exists(dirpath):
            os.makedirs(dirpath)
        with open(os.path.join(dirpath,name+'.txt'), "w") as file1:
                 file1.write("Name : ")
              
                 file1.write(name)
                 
                 file1.write("\ndesciption:")
                 
                 file1.write(des)
                 file1.write('{}:{},\n'.format("\nregister date and time", datetime.datetime.now()))
        # embeddings = face_recognition.face_encodings(self.register_new_user_capture)[0]

        # file = open(os.path.join(self.db_dir, '{}.pickle'.format(name)), 'wb')
        # pickle.dump(embeddings, file)
        # call(["python","encoding.py"])
        util.msg_box('Success!', 'User is registered successfully !')
        
        
       
        self.register_new_user_window.destroy()
        self.show_user_details(name, des)
    # def show_user_details(self, name, des):
    #     self.user_details_window = tk.Toplevel(self.main_window)
    #     self.user_details_window.geometry("1200x520+120+120")
    #     self.user_details_window.title('User Details')

    #     # Display user image
    #     user_image = Image.open(os.path.join(self.db1_dir, f"{name}.png"))
    #     user_image = user_image.resize((200, 200))
    #     user_image_tk = ImageTk.PhotoImage(image=user_image)
    #     user_image_label = tk.Label(self.user_details_window, image=user_image_tk)
    #     user_image_label.image = user_image_tk
    #     # user_image_label.pack(pady=10)
    #     user_image_label.place(x=10, y=0, width=700, height=500)

    #     # Display user details
    #     user_name_label = tk.Label(self.user_details_window, text=f"Name: {name}")
    #     # user_name_label.place(x=750, y=40)
    #     user_name_label.pack()
    #     user_description_label = tk.Label(self.user_details_window, text=f"Description: {des}")
    #     # user_description_label(x=750, y=80)
    #     user_description_label.pack()

    #     # Add Case Record button
    #     add_case_record_button = tk.Button(self.user_details_window, text="Add Case Record", command=lambda: self.add_case_record(name))
    #     add_case_record_button.pack(pady=20)
    #     # add_case_record_button.place(x=750, y=200)
    def show_user_details(self, name, des):
        self.user_details_window = tk.Toplevel(self.main_window)
        self.user_details_window.geometry("1200x620+100+100")
     
        self.user_details_window.title('User Details')

    # Set background image
        bg_image = Image.open("C:\\Users\\Face Recgnition\\Resources\\detail.png")
        bg_image_resized = bg_image.resize((1280,720))
        bg_photo = ImageTk.PhotoImage(bg_image_resized)
        bg_label = tk.Label(self.user_details_window, image=bg_photo)
        bg_label.photo = bg_photo
        bg_label.place(x=0, y=0)
    

    # Display user image
        user_image = Image.open(os.path.join(self.db1_dir, f"{name}.png"))
        user_image = user_image.resize((400, 400))
        user_image_tk = ImageTk.PhotoImage(image=user_image)
        user_image_label = tk.Label(self.user_details_window, image=user_image_tk)
        user_image_label.image = user_image_tk
        user_image_label.place(x=30, y=30)

    # Display user details
        user_name_label = tk.Label(self.user_details_window, text=f"Name: {name}", font=("Helvetica", 28, "bold"))
        user_name_label.place(x=600, y=50)

        user_description_label = tk.Label(self.user_details_window, text=f"Description: {des}", font=("Helvetica", 24))
        user_description_label.place(x=600, y=150)

    # Add Case Record button
        add_case_record_button = tk.Button(self.user_details_window, text="Add Record", font=("Helvetica", 26), command=lambda: self.add_case_record(name))
        add_case_record_button.place(x=600, y=300)

# ... (your existing code) ...


    def add_case_record(self, name):
        self.case_record_window = tk.Toplevel(self.user_details_window)
        self.case_record_window.geometry("1200x620+100+100")
        self.case_record_window.title('Add Case Record')

        self.case_record_text = tk.Text(self.case_record_window, height=30, width=100)
        self.case_record_text.pack(padx=10, pady=10)

        save_button = tk.Button(self.case_record_window, text="Save", command=lambda: self.save_case_record(name))
        save_button.pack(pady=10)
    def save_case_record(self,name):
        text = self.case_record_text.get("1.0", "end-1c")
        base_path ='./Details/'+name
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
            file.write('{}:{},\n'.format("\nregister date and time", datetime.datetime.now()))
            util.msg_box('Success!', 'Case is recorded successfully !')
            call(["python","encoding.py"])
            self.case_record_window.destroy()


    # def save_case_record(self, name):
    #     case_record = self.case_record_text.get("1.0", "end-1c")
    #     if case_record.strip():
    #         dirpath = os.path.join(self.db2_dir, name)
    #         with open(os.path.join(dirpath, f"{name}_case_record.txt"), "a") as file:
    #             file.write(case_record)
    #             file.write('\n')
    #         util.msg_box('Success!', 'Case record added successfully !')
    #         self.case_record_window.destroy()
    #     else:
    #         util.msg_box('Error!', 'Please enter a case record.')
        
        

if __name__ == "__main__":
    app = App()
    app.start()



