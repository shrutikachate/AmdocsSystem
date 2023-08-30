from tkinter import*
import tkinter.messagebox
from PIL import Image,ImageTk
from tkinter import ttk

window=Tk()
window.geometry("900x900")
window.title("HOME")


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

def deposit():
    window.destroy()
    import deposit

def withdraw():
    window.destroy()
    import withdraw

def check_balance():
    window.destroy()
    import check_balance

def ministatement():
    window.destroy()
    import mini_statement
    
def changeOnHover(button,colorOnHover,colorOnLeave):
    button.bind("<Enter>",func=lambda e:button.config(background=colorOnHover))
    button.bind("<Leave>",func=lambda e:button.config(background=colorOnLeave))


thelabel_0=Label(window,text="Welcome back!!",font="ariel 18 bold",bg="black",fg="white")
thelabel_0.place(x=75,y=100)

butequal1=Button(window,padx=32,pady=14,bd=2,bg="skyblue1",
                command=deposit,width=17,text="DEPOSIT",font=("Courier New",18,"bold")) 
butequal1.place(x=75,y=200)  

butequal2=Button(window,padx=32,pady=14,bd=2,bg="skyblue1",
                command=withdraw,width=17,text="WITHDRAW",font=("Courier New",18,"bold")) 
butequal2.place(x=75,y=300)  

butequal3=Button(window,padx=32,pady=14,bd=2,bg="skyblue1",
                command=check_balance,width=17,text="CHECK BALANCE",font=("Courier New",18,"bold")) 
butequal3.place(x=75,y=400)  

butequal4=Button(window,padx=32,pady=14,bd=2,bg="skyblue1",
                command=ministatement,width=17,text="MINI STATEMENT",font=("Courier New",18,"bold")) 
butequal4.place(x=75,y=500)  



changeOnHover(butequal1, "yellow", "skyblue1")
changeOnHover(butequal2, "yellow", "skyblue1")
changeOnHover(butequal3, "yellow", "skyblue1")
changeOnHover(butequal4, "yellow", "skyblue1")
window.mainloop()