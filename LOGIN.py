from tkinter import ttk
from tkinter import *
import tkinter.messagebox
from PIL import Image,ImageTk
from tkinter import ttk
import mysql.connector

window=Tk() 
window.geometry("550x600")
window.title("Login") 


image1 = Image.open(r"C:\Users\Administrator\Desktop\Amdocs_system\img1.jpeg")
image1 = image1.resize((1600, 900))
test = ImageTk.PhotoImage(image1)
label1 = tkinter.Label(image=test)
label1.image = test
label1.place(x=0, y=0)
 
melabel=Label(window,text="AMDOCS BANK",bg="powder blue",width=15,font=("Algerian",50,"bold"))
melabel.place(x=450,y=90)

try:
    mydbconn=mysql.connector.connect(
        host="localhost",
        user="root",
        password="pass@word1",
        database="amdocs_system")
    
    
except mysql.connector.Error as error:
    print("Failed to get record from MySQL table: {}".format(error))
    
    
def changeOnHover(button,colorOnHover,colorOnLeave):
    button.bind("<Enter>",func=lambda e:button.config(background=colorOnHover))
    button.bind("<Leave>",func=lambda e:button.config(background=colorOnLeave))

def Login():
    mypointer=mydbconn.cursor()
    uname=metext11.get()
    pwd=metext13.get()
    q1="select * from customers where  Name = %s and Password = %s"
    mypointer.execute(q1,[(uname),(pwd)])
    results = mypointer.fetchall()
    if len(results)==0:
        tkinter.messagebox.askokcancel("askokcancel","Login Failed")
    else:
        window.destroy()
        global account_number
        account_number=results[0][0]
        import home
        
def Register():
    #tkinter.messagebox.askokcancel("askokcancel","Registration Successful")
    window.destroy()
    import registration_new

textin=StringVar()
textin2=StringVar()

metext11=Entry(window,font=("Courier New",12,"bold"),textvar=textin,width=25,bd=5,bg="powder blue")
metext11.place(x=750,y=330)
thelabel=Label(window,text="Username",bg="powder blue", width=15,font="arial 15 bold")
thelabel.place(x=500,y=330)

metext13=Entry(window,font=("Courier New",12,"bold"),textvar=textin2,width=25,bd=5,bg="powder blue")
metext13.place(x=750,y=430)
thelabel1=Label(window,text="Password",bg="powder blue",width=15,font="arial 15 bold")
thelabel1.place(x=500,y=430)


butequal=Button(window,padx=15,pady=10,bd=3,bg="skyblue1",command=Login,text="Login",font=("Algerian",16,"bold"))
butequal.place(x=600,y=530)

butequal1=Button(window,padx=15,pady=10,bd=3,bg="skyblue1",command=Register,text="Register",font=("Algerian",16,"bold"))
butequal1.place(x=750,y=530)

changeOnHover(butequal, "yellow", "skyblue1")
changeOnHover(butequal1, "yellow", "skyblue1")



window.mainloop()   
