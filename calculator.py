from tkinter import *
from tkinter.messagebox import showerror

root = Tk()
root.title("Calculator")
root.geometry("500x500")
root.configure(background = "lightblue")
Label(root,text="GUI calculator",font=("comicsans",20),bg ="white").place(x=150,y=0)
Label(root,text="press 'x' twice for exponent",font=("comicsans",14),bg="lightblue").place(x=140,y=50)

entry = Entry(root,justify=RIGHT,width=25,font=13)
entry.place(x=90,y=90)

Button(root,height=2,width=5,text="7",font=9,bg="gold").place(x=50,y=200)
Button(root,height=2,width=5,text="8",font=9,bg="gold").place(x=120,y=200)
Button(root,height=2,width=5,text="9",font=9,bg="gold").place(x=190,y=200)

Button(root,height=2,width=5,text="4",font=9,bg="gold").place(x=50,y=270)
Button(root,height=2,width=5,text="5",font=9,bg="gold").place(x=120,y=270)
Button(root,height=2,width=5,text="6",font=9,bg="gold").place(x=190,y=270)

Button(root,height=2,width=5,text="1",font=9,bg="gold").place(x=50,y=340)
Button(root,height=2,width=5,text="2",font=9,bg="gold").place(x=120,y=340)
Button(root,height=2,width=5,text="3",font=9,bg="gold").place(x=190,y=340)

Button(root,height=2,width=5,text="AC",font=9,bg="red").place(x=50,y=130)
Button(root,height=2,width=5,text="(",font=9,bg="orange").place(x=120,y=130)
Button(root,height=2,width=5,text=")",font=9,bg="orange").place(x=190,y=130)
Button(root,height=2,width=5,text="C",font=9,bg="red").place(x=260,y=130)

Button(root,height=2,width=5,text="0",font=9,bg="gold").place(x=50,y=410)
Button(root,height=2,width=5,text=".",font=9,bg="orange").place(x=120,y=410)
Button(root,height=2,width=5,text="=",font=9,bg="navyblue").place(x=190,y=410)

Button(root,height=2,width=5,text="/",font=9,bg="orange").place(x=260,y=200)
Button(root,height=2,width=5,text="X",font=9,bg="orange").place(x=260,y=270)
Button(root,height=2,width=5,text="+",font=9,bg="orange").place(x=260,y=340)
Button(root,height=2,width=5,text="-",font=9,bg="orange").place(x=260,y=410)


root.mainloop()

