#! /usr/bin/env python

from Tkinter import *
import tkMessageBox

# Application: parent container class of all widget.
# in gui every button label textbox are  widget
class Application(Frame):
    def __init__(self,master=None):
        Frame.__init__(self,master)
        self.pack()
        self.createWidgets()
        
        
    def createWidgets(self):
        #self.helloLabel = Label(self,text = 'Hello ,World !')
        #self.helloLabel.pack()
        self.nameInput = Entry(self)
        self.nameInput.pack()
        self.alertButton = Button(self,text='Hello',command = self.hello)
        self.alertButton.pack()
        self.quitButton = Button(self,text='quit',command = self.quit)
        self.quitButton.pack()

    def hello(self):
        name = self.nameInput.get() or 'world'
        tkMessageBox.showinfo('Message','Hello,%s'%name)

app = Application()
app.master.title('Hello World!')
app.mainloop()
