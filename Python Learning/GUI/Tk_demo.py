#! /usr/bin/env python

from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *

def ui_process():
    root =Tk()
    root.geometry("500x400+800+500")

#tag   
    L_titile = Label(root,text='Title',)
    L_titile.config(font='Helvetica -15 bold',fg='blue')
    L_titile.place(x=150,y=20,anchor="center")
    L_author = Label(root, text='author:b4l8')
    L_author.config(font='Helvetica -10 bold')
    L_author.place(x=250,y=380)

#button
    B_0 = Button(root, text="text", command=lambda:CreatDialog(root))
    B_0.place(x=90,y=200)

    B_OK = Button(root,text="create",command=lambda:button_process(root))
    B_OK.place(x=200,y=200)
    B_NO = Button(root, text="cancel")
    B_NO.place(x=250,y=200)

#check
    v = IntVar()
    R_ONE=Radiobutton(root, text="One", variable=v, value=1,command=lambda:Print_b(1)).place(x=60,y=150)
    R_TWO=Radiobutton(root, text="Two", variable=v, value=2,command=lambda:Print_b(2)).place(x=10,y=150)

#slider
    W = Scale(root, from_=0, to=100,orient=HORIZONTAL)#orient=HORIZONTAL 
    W.place(x=50,y=300)
    print(W.get())  

#menubar
    menubar = Menu(root)
    root.config(menu=menubar)
    filemenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="File", menu=filemenu)
    filemenu.add_command(label="New", command=NewFile)
    filemenu.add_command(label="Open", command=OpenFile)
    filemenu.add_command(label="Save", command=SaveFile)
    filemenu.add_separator()
    filemenu.add_command(label="Exit", command=root.quit)
    
    
    helpmenu = Menu(menubar, tearoff=0)
    menubar.add_cascade(label="Help", menu=helpmenu)
    helpmenu.add_command(label="About..",command=About)
    mainloop()

#function port to button_process
def button_process(root):
    #messagebox
    askokcancel('Python Tkinter', 'confirm creation of window?')
    askquestion('Python Tkinter', "confirm creation of window?")
    askyesno('Python Tkinter', 'Create a window?')
    showerror('Python Tkinter', 'unknown error')
    showinfo('Python Tkinter', 'hello world')
    showwarning('Python Tkinter', 'warning!!!!')
    root1 = Toplevel(root)

def PrintHello():
    print("hello")

def Print_b(a):
    print(a)

#CreatDialog
def CreatDialog(root):
    root2 = Toplevel(root)
    Label(root2,text ="First Name").grid(row=0)
    Label(root2,text = "Last Name").grid(row=1)
    e1 = Entry(root2)
    e2 = Entry(root2)
    e1.grid(row = 0,column=1)
    e2.grid(row = 1,column=1)
    #world = simpledialog.askstring('Python Tkinter', 'Input String', initialvalue = 'Python Tkinter')
    #print(world)
    #simpledialog.askinteger()
    #simpledialog.askfloat()

#file operating dialog
def NewFile():
    print "New File!!"
def About():
    print "This is a simple example of a menu"
def OpenFile():
    f = askopenfilename(title='open file', filetypes=[('Python', '*.py *.pyw'), ('All Files', '*')])
    print(f)

def SaveFile():
    f = asksaveasfilename(title='save file', initialdir='~/Learn/Python', initialfile='hello.py')
    print(f)
   
if __name__ == "__main__":
    print("start")
    ui_process()

