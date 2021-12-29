from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.font import Font
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

class Developer:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        
        self.root.title("Face Recognition system")

        title_lbl1=Label(self.root,text="DEVELOPER",font=("times new roman",35,"bold"),bg="orange",fg="blue")
        title_lbl1.place(x=0,y=0,width=1530,height=45)

        top_img=Image.open(r"img\ryan-gosling-blade-runner-2049-zo.jpg")
        top_img=top_img.resize((1530,790),Image.ANTIALIAS)
        self.proimage_top=ImageTk.PhotoImage(top_img)

        left_label=Label(self.root,image= self.proimage_top)
        left_label.place(x=0,y=55,width=1530,height=720)

        #Frame
        main_frame=Frame(left_label,bd=2,bg="orange")
        main_frame.place(x=1000,y=0,width=500,height=600)

        top_img1=Image.open(r"img\f2cc1e2bed650d3c812ed09571ce44bb.jpg")
        top_img1=top_img1.resize((200,200),Image.ANTIALIAS)
        self.proimage_top1=ImageTk.PhotoImage(top_img1)

        left_label=Label(main_frame,image= self.proimage_top1)
        left_label.place(x=300,y=0,width=200,height=200)

        # Developer Information
        dev_label=Label(main_frame,text="Hey, How you doin?",font=("times new roman",20,"roman"),bg="orange",fg="blue")
        dev_label.place(x=0,y=5)

        dev_label=Label(main_frame,text="Ad Astra Per Aspera",font=("times new roman",25,"roman"),bg="orange",fg="blue")
        dev_label.place(x=0,y=40)

        img2=Image.open(r"img\132-1326862_big.jpg")
        img2=img2.resize((500,380),Image.ANTIALIAS)
        self.proimage2=ImageTk.PhotoImage(img2)

        flbl1=Label(main_frame,image= self.proimage2)
        flbl1.place(x=0,y=210,width=500,height=390)

if __name__=="__main__":
    root=Tk()
    obj=Developer(root)
    root.mainloop()