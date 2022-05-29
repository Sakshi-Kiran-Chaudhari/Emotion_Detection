from tkinter import *
from PIL import ImageTk
from tkinter import messagebox
import os

def callback():
    filename ='videotester.py'
    os.system(filename)


class Login:
    def __init__(self,root):
        self.root=root
        self.root.title("Register")
        self.root.geometry("1199x600")
        self.root.resizable(False,False);
        
        self.bg=ImageTk.PhotoImage(file="C:/Users/Rutuja/Desktop/abc/icon1.jpg")
        self.bg_image=Label(self.root,image=self.bg).place(x=0,y=0,relwidth=1,relheight=1)

        Frame_login=Frame(self.root,bg="white")
        Frame_login.place(x=550,y=150,height=400,width=500)


        title=Label(Frame_login,text="Welcome To Emotion Detector",font=("Impact",25,"bold"),fg="#d77337",bg="white").place(x=50,y=30)
        desc=Label(Frame_login,text="Register Here",font=("Goudy old style",20,"bold"),fg="#d25d17",bg="white").place(x=170,y=100)
        
        label_user=Label(Frame_login,text="Name",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=140)
        self.txt_user=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_user.place(x=90,y=170,width=350,height=35)

        label_pass=Label(Frame_login,text="Email",font=("Goudy old style",15,"bold"),fg="gray",bg="white").place(x=90,y=210)
        self.txt_pass=Entry(Frame_login,font=("times new roman",15),bg="lightgray")
        self.txt_pass.place(x=90,y=240,width=350,height=35)

        facedetect=Button(Frame_login,text=" Detect Your Emotion ",command=callback,bg="white",fg="#d77337",font=("times new roman",15)).place(x=180,y=340)
        login=Button(Frame_login,command=self.login_function,text="Register",fg="white",bg="#d77337",font=("times new roman",15)).place(x=90,y=290)

    def login_function(self):
        if self.txt_pass.get()==""or self.txt_user.get()=="":
            messagebox.showerror("Error","All fields are required",parent=self.root)
        elif self.txt_user.get()!="Sakshi" or self.txt_pass.get()!="Sakshi@gmail.com":
            messagebox.showerror("Error","Invalid Username/Email",parent=self.root)
        else:
            messagebox.showinfo("Welcome to your Panel",f"Welcome {self.txt_user.get()}\n Your Email: {self.txt_pass.get()}",parent=self.root)

root=Tk()
obj=Login(root)
root.mainloop()
