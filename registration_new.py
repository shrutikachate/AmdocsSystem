# -*- coding: utf-8 -*-
"""
Created on Wed Aug 30 11:01:50 2023

@author: user
"""

from tkinter import*
import tkinter.messagebox
from tkcalendar import Calendar
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector

window=Tk()
window.geometry("900x900")
window.title("REGISTER")

image1 = Image.open(r"C:\Users\Administrator\Desktop\Amdocs_system\img1.jpeg")
image1 = image1.resize((1600, 900))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=0)

conn= mysql.connector.connect(
        host = "localhost" ,
        user = "root" ,
        password = "pass@word1" ,
        database = "amdocs_system"
        )


mypointer=conn.cursor()

class base:
    def __init__(self,a,b,c,d,e,g,h,i):
        self.Name=a
        self.Mobile_Number=b
        self.DOB=c
        self.Email=d
        self.Adhaar_Card=e
        self.Address=g
        self.Account_Type=h
        self.Password=i
class customer(base):
    def __init__(self,a,b,c,d,e,f,g,h,i):
        self.Pan_Card=f
        base.__init__(self,a,b,c,d,e,g,h,i)  #Inheritance


thelabel_0=Label(window,text="REGISTRATION",width=18,height=1,font="ariel 30 bold",bg="powder blue")
thelabel_0.place(x=550,y=30)

def changeOnHover(button,colorOnHover,colorOnLeave):
    button.bind("<Enter>",func=lambda e:button.config(background=colorOnHover))
    button.bind("<Leave>",func=lambda e:button.config(background=colorOnLeave))

def register():
    window.destroy()
    import login   

def insert1():

    in1=metext11.get()
    in2=metext12.get()
    in3=metext13.get()
    in4=metext14.get()
    in5=metext15.get()
    in6=metext16.get()
    in7=metext17.get()
    in8=metext18.get()
    in9=metext19.get()

    c=customer(in1,in2,in3,in4,in5,in6,in7,in8,in9)
    flag=False 
    
    sql="""insert into amdocs_system.customers(Name,Mobile_Number,Email,Adhaar_Card,Address,Account_Type,Password,DOB,Pan_Card) values(%s,%s,%s,%s,%s,%s,%s,%s,%s)"""
    tt1=(c.Name,c.Mobile_Number,c.Email,c.Adhaar_Card,c.Address,c.Account_Type,c.Password,c.DOB,c.Pan_Card)
    flag=mypointer.execute(sql,tt1)
    conn.commit()
    
    butequal=Button(window,padx=32,height= -1,pady=14,bd=2,bg="powder blue",
                    command=register,text="Login",width=10,
                    font=("Courier New",18,"bold")) 
    butequal.place(x=675,y=700)   
    changeOnHover(butequal, "yellow", "skyblue1")

textin=StringVar()
textin2=StringVar()
textin3=StringVar()
textin4=StringVar()
textin5=StringVar()
textin6=StringVar()
textin7=StringVar()
textin8=StringVar()
textin9=StringVar()
textin10=StringVar()


metext11=Entry(window,font=("Courier New",13,"bold"),
               textvar=textin,width=25,bd=5,bg="powder blue")
metext11.place(x=400,y=200)
thelabel_1=Label(window,text="User Name",width=20,font="ariel 13 bold",bg="powder blue")
thelabel_1.place(x=150,y=200)


metext12=Entry(window,font=("Courier New",13,'bold'),
               textvar=textin2,width=25,bd=5,bg="powder blue")
metext12.place(x=1150,y=200)
thelabel_2=Label(window,text="Mobile Number",width=20,font="arial 13 bold",bg="powder blue")
thelabel_2.place(x=900,y=200)

def pick_date(event):
    global cal
    date_window=Toplevel()
    date_window.grab_set()
    date_window.title("Choose DOB")
    date_window.geometry("250x220+590+370")
    cal=Calendar(date_window ,selectmode="day",date_pattern="yyyy-mm-dd")
    cal.config(background = "black")
    cal.place(x=0,y=0)
    
    submit_button=Button(date_window,text="Submit",command=grab_date)
    submit_button.place(x=90,y=190)
    
def grab_date():
    metext13.delete(0,END)
    metext13.insert(0,cal.get_date())
   


metext13=Entry(window,font=("Courier New",13,"bold"),
               textvar=textin3,width=25,bd=5,bg="powder blue")
metext13.place(x=400,y=300)
metext13.insert(0,"Choose your DOB")
metext13.bind("<1>",pick_date)
thelabel_3=Label(window,text="Date of Birth",width=20,font="ariel 13 bold",bg="powder blue")
thelabel_3.place(x=150,y=300)


metext14=Entry(window,font=("Courier New",13,"bold"),
               textvar=textin4,width=25,bd=5,bg="powder blue")
metext14.place(x=1150,y=300)
thelabel_4=Label(window,text="Email-ID",width=20,font="ariel 13 bold",bg="powder blue")
thelabel_4.place(x=900,y=300)


metext15=Entry(window,font=("Courier New",13,"bold"),
               textvar=textin5,width=25,bd=5,bg="powder blue")
metext15.place(x=400,y=400)
thelabel_5=Label(window,text="Aadhar Number",width=20,font="ariel 13 bold",bg="powder blue")
thelabel_5.place(x=150,y=400)


metext16=Entry(window,font=("Courier New",13,"bold"),
               textvar=textin6,width=25,bd=5,bg="powder blue")
metext16.place(x=1150,y=400)
thelabel_6=Label(window,text="PAN Number",width=20,font="ariel 13 bold",bg="powder blue")
thelabel_6.place(x=900,y=400)


metext17=Entry(window,font=("Courier New",13,"bold"),
               textvar=textin7,width=25,bd=5,bg="powder blue")
metext17.place(x=400,y=500)
thelabel_7=Label(window,text="Address",width=20,font="ariel 13 bold",bg="powder blue")
thelabel_7.place(x=150,y=500)


textin8.set("Select account type")
drop= OptionMenu(window, textin8,"Saving Account","Current account")
drop.config(font=("Courier New",13,"bold"),bg="powder blue",width=22)
drop.pack()
drop.place(x=1150,y=500)
metext18=textin8
thelabel_8=Label(window,text="Account Type",width=20,font="ariel 13 bold",bg="powder blue")
thelabel_8.place(x=900,y=500)


metext19=Entry(window,font=("Courier New",13,"bold"),
               textvar=textin9,width=25,bd=5,bg="powder blue")
metext19.place(x=400,y=600)
thelabel_9=Label(window,text="Password",width=20,font="ariel 13 bold",bg="powder blue")
thelabel_9.place(x=150,y=600)


metext20=Entry(window,font=("Courier New",13,"bold"),
               textvar=textin10,width=25,bd=5,bg='powder blue')
metext20.place(x=1150,y=600)
thelabel_10=Label(window,text="Re-Type Password",width=20,font="ariel 13 bold",bg="powder blue")
thelabel_10.place(x=900,y=600)

def work():
    if metext19.get()==metext20.get():
        insert1()
        tkinter.messagebox.showinfo("askokcancel","Registration sucessful")
    else:
        tkinter.messagebox.showinfo("askokcancel","passwords don't match,check again")
        
butequal=Button(window,padx=32,height= -1,pady=14,bd=2,bg="powder blue",
                command=work,text="Register",width=10,
                font=("Courier New",18,"bold")) 
butequal.place(x=675,y=700)   
changeOnHover(butequal, "yellow", "skyblue1")

window.mainloop()