from tkinter import*
import qrcode

top=Tk()
top.geometry("1000x550")
top.title("TEA SHOP BILL")
top.resizable(False,False)

frame=Frame(top,height=80,width=1000,bd=20,bg="seagreen1").pack(side="top")

title=Label(frame,text="TEA TIME",bg="seagreen1",fg="black",font=('algerian',20,'bold'))
title.place(x=440,y=20)
line=Label(top,width=500,height=0,text="_______________________________________________________________________________________________________________________________________________________________________________________________",fg="black",bg="black")
line.place(x=0,y=70)

frame2=Frame(top,height=480,width=450,bg="pink").place(x=550,y=82)
bor=Label(top,text="|",height=480,bg="black",fg="black")
bor.place(x=550,y=80)

frame3=Frame(top,height=480,width=550,bg="skyblue").place(x=0,y=82)
def can():
    top.destroy()
def tot():
    tea =int(n1.get())
    coffee =int(n2.get())
    samosa =int(n3.get())
    snacks =int(n4.get())

    a=tea*10
    b=coffee*15
    c=samosa*5
    d=snacks*20
    tot=(a+b+c+d)


    
    answer.config(text=tot,font=('algerian',20,'bold'),fg="red",bg="black")
def pri():
    hii = Tk()
    hii.geometry("300x200")
    hii.title("price list")
    hii.resizable(False,False)
    l=Label(hii,text="ITEM",font="bold",bd=5,fg="red")
    l.grid(row=0,column=0)
    l=Label(hii,text="                                    ",fg="white",anchor='w')
    l.grid(row=0,column=2)
    l=Label(hii,text="PRICE",font="bold",bd=5,fg="red")
    l.grid(row=0,column=3)
    l=Label(hii,text="TEA",font="bold",bd=5)
    l.grid(row=1,column=0)
    l=Label(hii,text="10",font="bold",bd=5)
    l.grid(row=1,column=3)
    l=Label(hii,text="COFFEE",font="bold",bd=5)
    l.grid(row=2,column=0)
    l=Label(hii,text="15",font="bold",bd=5)
    l.grid(row=2,column=3)
    l=Label(hii,text="SAMOSA",font="bold",bd=5)
    l.grid(row=3,column=0)
    l=Label(hii,text="5",font="bold",bd=5)
    l.grid(row=3,column=3)
    l=Label(hii,text="SNACKS",font="bold",bd=5)
    l.grid(row=4,column=0)
    l=Label(hii,text="20",font="bold",bd=5)
    l.grid(row=4,column=3)


def qr():
    pay="github.com/santhosh29-m"
    qr=qrcode.make(pay)
    qr.save("Pay/"+"no"+".png")

    global Image
    Image=PhotoImage(file="Pay/"+"no"+".png")
    

    Image_view=Label(top)
    Image_view.place(x=620,y=150)
    Image_view.config(image=Image)
  
name=Label(top,text="NAME",fg="black",bg="skyblue",font=('algerian',20,'bold'))
name.place(x=50,y=100)
n=Entry(top,width=15,justify="center",bd=6,bg="gray40",fg="black",font=('algerian',20,'bold'))
n.place(x=180,y=100)


name1=Label(top,text="TEA",fg="black",bg="skyblue",font=('algerian',20,'bold'))
name1.place(x=50,y=160)
n1=Entry(top,width=15,justify="center",bd=6,bg="yellow",font=('algerian',20,'bold'))
n1.place(x=180,y=160)

name2=Label(top,text="COFFEE",fg="black",bg="skyblue",font=('algerian',20,'bold'))
name2.place(x=50,y=220)
n2=Entry(top,width=15,bd=6,justify="center",bg="yellow",font=('algerian',20,'bold'))
n2.place(x=180,y=220)

name3=Label(top,text="SAMOSA",fg="black",bg="skyblue",font=('algerian',20,'bold'))
name3.place(x=50,y=280)
n3=Entry(top,width=15,bd=6,justify="center",bg="yellow",font=('algerian',20,'bold'))
n3.place(x=180,y=280)

name4=Label(top,text="SNACKS",fg="black",bg="skyblue",font=('algerian',20,'bold'))
name4.place(x=50,y=340)
n4=Entry(top,width=15,bd=6,justify="center",bg="yellow",font=('algerian',20,'bold'))
n4.place(x=180,y=340)

name5=Label(top,text="TOTAL",fg="black",bg="skyblue",font=('algerian',20,'bold'))
name5.place(x=50,y=400)
n5=Entry(top,width=15,bd=6,bg="black",justify="center",font=('algerian',20,'bold'))
n5.place(x=180,y=400)

bt=Button(top,text="TOTAL",bg="black",fg="red",command=tot,font="bold",bd=5)
bt.place(x=40,y=480)

bt=Button(top,text="CANCEL",bg="black",fg="red",command=can,font="bold",bd=5)
bt.place(x=180,y=480)

bt=Button(top,text="GETQr",bg="black",fg="red",font="bold",command=qr,bd=5)                                  
bt.place(x=320,y=480)

bt=Button(top,text="PRICE",bg="black",fg="red",font="bold",command=pri,bd=5)
bt.place(x=460,y=480)

answer=Label(top,text="*",bg="black")
answer.place(x=300,y=405)

top.mainloop()


