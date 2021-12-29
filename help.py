from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter.font import Font
from PIL import Image,ImageTk
from tkinter import messagebox
import mysql.connector 
import cv2

class Help:
    def __init__(self,root):
        self.root=root
        self.root.geometry("1530x790+0+0")
        self.root.title("face Recognition system")

        title_lbl1=Label(self.root,text="HELP DESK",font=("times new roman",35,"bold"),bg="white",fg="blue")
        title_lbl1.place(x=0,y=0,width=1530,height=45)

        top_img=Image.open(r"img\1_5TRuG7tG0KrZJXKoFtHlSg.jpeg")
        top_img=top_img.resize((1530,720),Image.ANTIALIAS)
        self.proimage_top=ImageTk.PhotoImage(top_img)

        left_label=Label(self.root,image= self.proimage_top)
        left_label.place(x=0,y=55,width=1530,height=720)

        dev_label=Label(left_label,text="email:rishivyas2000@gmail.com",font=("times new roman",20,"bold"),bg="white")
        dev_label.place(x=550,y=200)

if __name__=="__main__":
    root=Tk()
    obj=Help(root)
    root.mainloop()