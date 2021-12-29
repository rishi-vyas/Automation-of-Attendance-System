from tkinter import *
from tkinter import ttk
from tkinter.font import Font
import tkinter
from PIL import Image,ImageTk
import os
from time import strftime
from datetime import datetime
from student import Student
from train import Train
from face_recognisation import Face_Recognisation
from developer import Developer
from help import Help
from attendance import Attendance
# from login import Login_Window

class AAS:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("Automation of Attendance System")

        #image1
        img=Image.open(r"img\BestFacialRecognition.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.proimage=ImageTk.PhotoImage(img)

        flbl1=Label(self.root,image= self.proimage)
        flbl1.place(x=0,y=0,width=500,height=130)

        #image2
        img1=Image.open(r"img\facialrecognition.png")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.proimage1=ImageTk.PhotoImage(img1)

        flbl1=Label(self.root,image= self.proimage1)
        flbl1.place(x=500,y=0,width=550,height=130)

        #image3
        img2=Image.open(r"img\di.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.proimage2=ImageTk.PhotoImage(img2)

        flbl1=Label(self.root,image= self.proimage2)
        flbl1.place(x=1000,y=0,width=550,height=130)

        #bgimg       
        img3=Image.open(r"img\Coldplay-Photos.jpg")
        img3=img3.resize((1530,710),Image.ANTIALIAS)
        self.proimage3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image= self.proimage3)
        bg_img.place(x=0,y=130,width=1530,height=710)

        title_lbl1=Label(bg_img,text="Automation of Attendance System",font=("times new roman",35,"bold"),bg="white",fg="dark violet")
        title_lbl1.place(x=0,y=0,width=1530,height=45)

#********************************************time***********************************************************

        def time():
            string = strftime('%H:%M:%S %p')
            lbl.config(text = string)
            lbl.after(1000, time)
        
        lbl = Label(title_lbl1, font = ('times new roman',14,'bold'),background = 'white', foreground = 'dark violet')
        lbl.place(x=0,y=0,width=110,height=50)
        time()

#************************************************************************************************************
        
        #studentbuttonimage
        img4=Image.open(r"img\student.jpg")
        img4=img4.resize((220,220),Image.ANTIALIAS)
        self.proimage4=ImageTk.PhotoImage(img4)
        
        b1=Button(bg_img,image=self.proimage4,command=self.student_details,cursor="hand2")
        b1.place(x=200,y=100,width=220,height=220)

        b1_title=Button(bg_img,text="Student Details",command=self.student_details,cursor="hand2",font=("times new roman",15,"bold"),bg="dark violet",fg="yellow")
        b1_title.place(x=200,y=300,width=220,height=40)

        #detectfacebutton
        img5=Image.open(r"img\face_detector1.jpg")
        img5=img5.resize((220,220),Image.ANTIALIAS)
        self.proimage5=ImageTk.PhotoImage(img5)
        
        b1=Button(bg_img,image=self.proimage5,cursor="hand2", command=self.face_data)
        b1.place(x=500,y=100,width=220,height=220)

        b1_title=Button(bg_img,text="Face Detector",cursor="hand2", command=self.face_data, font=("times new roman",15,"bold"),bg="dark violet",fg="yellow")
        b1_title.place(x=500,y=300,width=220,height=40)

        #attenddancebutton
        img6=Image.open(r"img\img1.jpeg")
        img6=img6.resize((220,220),Image.ANTIALIAS)
        self.proimage6=ImageTk.PhotoImage(img6)

        b1=Button(bg_img,image=self.proimage6,cursor="hand2")
        b1.place(x=800,y=100,width=220,height=220)

        b1_title=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",15,"bold"),bg="dark violet",fg="yellow")
        b1_title.place(x=800,y=300,width=220,height=40)

        #helpbutton
        img7=Image.open(r"img\help.jpg")
        img7=img7.resize((220,220),Image.ANTIALIAS)
        self.proimage7=ImageTk.PhotoImage(img7)

        b1=Button(bg_img,image=self.proimage7,cursor="hand2",command=self.help_data)
        b1.place(x=1100,y=100,width=220,height=220)

        b1_title=Button(bg_img,text="Help Desk",cursor="hand2",command=self.help_data,font=("times new roman",15,"bold"),bg="dark violet",fg="yellow")
        b1_title.place(x=1100,y=300,width=220,height=40)

        #trainfacebutton
        img8=Image.open(r"img\di.jpg")
        img8=img8.resize((220,220),Image.ANTIALIAS)
        self.proimage8=ImageTk.PhotoImage(img8)

        b1=Button(bg_img,image=self.proimage8,cursor="hand2", command=self.train_data)
        b1.place(x=200,y=380,width=220,height=220)

        b1_title=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",15,"bold"),bg="dark violet",fg="yellow")
        b1_title.place(x=200,y=580,width=220,height=40)
        
        #photosfacebutton 
        img9=Image.open(r"img\girl.jpeg")
        img9=img9.resize((220,220),Image.ANTIALIAS)
        self.proimage9=ImageTk.PhotoImage(img9)

        b1=Button(bg_img,image=self.proimage9,cursor="hand2",command=self.open_img)
        b1.place(x=500,y=380,width=220,height=220)

        b1_title=Button(bg_img,text="Photos",cursor="hand2", command=self.open_img,font=("times new roman",15,"bold"),bg="dark violet",fg="yellow")
        b1_title.place(x=500,y=580,width=220,height=40)

        #developerbutton
        img10=Image.open(r"img\dev.jpg")
        img10=img10.resize((220,220),Image.ANTIALIAS)
        self.proimage10=ImageTk.PhotoImage(img10)

        b1=Button(bg_img,image=self.proimage10,cursor="hand2",command=self.develop_data)
        b1.place(x=800,y=380,width=220,height=220)

        b1_title=Button(bg_img,text="Developer",cursor="hand2",command=self.develop_data,font=("times new roman",15,"bold"),bg="dark violet",fg="yellow")
        b1_title.place(x=800,y=580,width=220,height=40)
        
        #exitbutton
        img11=Image.open(r"img\exit.jpg")
        img11=img11.resize((220,220),Image.ANTIALIAS)
        self.proimage11=ImageTk.PhotoImage(img11)

        b1=Button(bg_img,image=self.proimage11,cursor="hand2",command=self.iExit)
        b1.place(x=1100,y=380,width=220,height=220)

        b1_title=Button(bg_img,text="Exit",cursor="hand2",command=self.iExit, font=("times new roman",15,"bold"),bg="dark violet",fg="yellow")
        b1_title.place(x=1100,y=580,width=220,height=40)


    def open_img(self):
        os.startfile("data")

    def iExit(self):
        self.iExit=tkinter.messagebox.askyesorno("Face Recognisation", "Are you sure, wanna exit!",parent=self.root )
        if self.iExit > 0:
            self.root.destroy()

#******************************************functionbuttons*****************************************
   
    def student_details(self):
        self.new_window=Toplevel(self.root)
        self.app=Student(self.new_window)

    def train_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Train(self.new_window)

    def face_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Face_Recognisation(self.new_window)

    def develop_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Developer(self.new_window)

    def help_data(self):
        self.new_window=Toplevel(self.root)
        self.app=Help(self.new_window)

if __name__=="__main__":
        root=Tk()
        obj=AAS(root)
        root.mainloop()
