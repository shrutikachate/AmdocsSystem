from tkinter import*
import tkinter.messagebox
from PIL import Image,ImageTk
from tkinter import ttk
from datetime import date
import mysql.connector
import bank_main
from datetime import datetime

window=Tk()
window.geometry("900x900")

image1 = Image.open(r"C:\Users\Administrator\Desktop\Amdocs_system\img1.jpeg")
image1 = image1.resize((1600, 900))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=0)

image1 = Image.open(r"C:\Users\Administrator\Desktop\Amdocs_system\img1.jpeg")
image1 = image1.resize((1200, 900))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=450, y=0)

thelabel_1=Label(window,width=90,height=30,bg="powder blue")
thelabel_1.place(x=550,y=120)

thelabel_1=Label(window,width=17,height=2,text="WELCOME BACK",font=("Courier New",18,"bold"),bg="black",fg="white")
thelabel_1.place(x=75,y=100)

thelabel_1=Label(window,width=17,height=2,text="DEPOSIT",font=("Courier New",18,"bold"),bg="powder blue")
thelabel_1.place(x=75,y=200)

thelabel_1=Label(window,width=17,height=2,text="WITHDRAW",font=("Courier New",18,"bold"),bg="powder blue")
thelabel_1.place(x=75,y=300)

thelabel_1=Label(window,width=17,height=2,text="MINI STATEMENT",font=("Courier New",18,"bold"),bg="powder blue")
thelabel_1.place(x=75,y=400)

thelabel_1=Label(window,width=17,height=2,text="CHECK BALANCE",font=("Courier New",18,"bold"),bg="powder blue")
thelabel_1.place(x=75,y=500)

conn= mysql.connector.connect(
        host = "localhost" ,
        user = "root" ,
        password = "pass@word1" ,
        database = "amdocs_system"
        )


mypointer=conn.cursor()

def changeOnHover(button,colorOnHover,colorOnLeave):
    button.bind("<Enter>",func=lambda e:button.config(background=colorOnHover))
    button.bind("<Leave>",func=lambda e:button.config(background=colorOnLeave))
    
def home():
    window.destroy()
    import home


def insert1():
    in1=metext11.get()
    today = date.today()
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    acc_num=bank_main.acc_num
    flag=False
    sql="""insert into amdocs_system.transaction(Account_Number,Type,Amount,Transaction_Date,Transaction_Time) values(%s,%s,%s,%s,%s)"""
    tt1=(acc_num,"D",in1,today,current_time)
    flag=mypointer.execute(sql,tt1)
    conn.commit()
    butequal=Button(window,padx=32,height= -1,pady=14,bd=2,bg="powder blue",
                    command=home,text="home",width=10,
                    font=("Courier New",15,"bold")) 
    butequal.place(x=780,y=400)   
    changeOnHover(butequal, "yellow", "skyblue1")
    
textin=StringVar()
metext11=Entry(window,font=("Courier New",13,"bold"),
               textvar=textin,width=25,bd=5,bg='powder blue')
metext11.place(x=735,y=300)
thelabel_1=Label(window,text="ENTER AMOUNT TO BE DEPOSITED",font="ariel 13 bold",bg="powder blue")
thelabel_1.place(x=720,y=250)

butequal=Button(window,padx=32,pady=14,bd=2,bg="skyblue1",
                command=insert1,text="SUBMIT",
                font=("Courier New",15,"bold"))  
butequal.place(x=780,y=400)   
changeOnHover(butequal, "yellow", "skyblue1")

window.mainloop()