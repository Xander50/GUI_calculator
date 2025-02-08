from tkinter import *
from tkinter.messagebox import showerror

def add_text(text,strvar:StringVar):
    strvar.set(f'{strvar.get()}{text}')

def submit(entry:Entry,strvar:StringVar):
    operation = entry.get()
    try:
        strvar.set(f'{strvar.get()}={eval(operation)}')
    except:
        showerror("Error, please enter a properly defined equation")

root = Tk()
root.title("Calculator")
root.geometry("500x500")
root.configure(background = "lightblue")

entry_strvar= StringVar(root)

Label(root,text="GUI calculator",font=("comicsans",20),bg ="white").place(x=150,y=0)
Label(root,text="press 'x' twice for exponent",font=("comicsans",14),bg="lightblue").place(x=140,y=50)

eqn_entry=Entry(root,justify=RIGHT,textvariable=entry_strvar,width=25,font=12,state="disabled")
eqn_entry.place(x=90,y=90)
# entry = Entry(root,justify=RIGHT,width=25,font=13)
# entry.place(x=90,y=90)

Button(root,height=2,width=5,text="7",font=9,bg="gold",command=lambda:add_text("7",entry_strvar)).place(x=50,y=200)
Button(root,height=2,width=5,text="8",font=9,bg="gold",command=lambda:add_text("8",entry_strvar)).place(x=120,y=200)
Button(root,height=2,width=5,text="9",font=9,bg="gold",command=lambda:add_text("9",entry_strvar)).place(x=190,y=200)

Button(root,height=2,width=5,text="4",font=9,bg="gold",command=lambda:add_text("4",entry_strvar)).place(x=50,y=270)
Button(root,height=2,width=5,text="5",font=9,bg="gold",command=lambda:add_text("5",entry_strvar)).place(x=120,y=270)
Button(root,height=2,width=5,text="6",font=9,bg="gold",command=lambda:add_text("6",entry_strvar)).place(x=190,y=270)

Button(root,height=2,width=5,text="1",font=9,bg="gold",command=lambda:add_text("1",entry_strvar)).place(x=50,y=340)
Button(root,height=2,width=5,text="2",font=9,bg="gold",command=lambda:add_text("2",entry_strvar)).place(x=120,y=340)
Button(root,height=2,width=5,text="3",font=9,bg="gold",command=lambda:add_text("3",entry_strvar)).place(x=190,y=340)

Button(root,height=2,width=5,text="AC",font=9,bg="red",command=lambda:entry_strvar.set('')).place(x=50,y=130)
Button(root,height=2,width=5,text="(",font=9,bg="orange",command=lambda:add_text("(",entry_strvar)).place(x=120,y=130)
Button(root,height=2,width=5,text=")",font=9,bg="orange",command=lambda:add_text(")",entry_strvar)).place(x=190,y=130)
Button(root,height=2,width=5,text="C",font=9,bg="red",command=lambda:entry_strvar.set(entry_strvar.get()[:-1])).place(x=260,y=130)

Button(root,height=2,width=5,text="0",font=9,bg="gold",command=lambda:add_text("0",entry_strvar)).place(x=50,y=410)
Button(root,height=2,width=5,text=".",font=9,bg="orange",command=lambda:add_text(".",entry_strvar)).place(x=120,y=410)
Button(root,height=2,width=5,text="=",font=9,bg="navyblue",command=lambda:submit(eqn_entry,entry_strvar)).place(x=190,y=410)

Button(root,height=2,width=5,text="/",font=9,bg="orange",command=lambda:add_text("/",entry_strvar)).place(x=260,y=200)
Button(root,height=2,width=5,text="X",font=9,bg="orange",command=lambda:add_text("*",entry_strvar)).place(x=260,y=270)
Button(root,height=2,width=5,text="+",font=9,bg="orange",command=lambda:add_text("+",entry_strvar)).place(x=260,y=340)
Button(root,height=2,width=5,text="-",font=9,bg="orange",command=lambda:add_text("-",entry_strvar)).place(x=260,y=410)

Button(root,height=2,width=5,text="OK",font=9,bg="white",command=lambda:root.destroy()).place(x=190,y=480)


root.mainloop()

