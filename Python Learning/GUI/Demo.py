#! /usr/bin/env python

from Tkinter import *
from tkMessageBox import *
from tkFileDialog import *

root = Tk()
root.title("Simple Editor")
root.geometry("410x335")

def savebuttonCallBack():
    #print filename.get()
    file = open(filename.get(),'w')
    file.write(contents.get("1.0",'end-1c')) # from line 1 ,char 0 to end; text always add 1 more char \n
    file.close()


def loadbuttonCallBack():
    file = open(filename.get())
    contents.insert(INSERT,file.read())
    file.close()


frame=Frame(root)
frame.pack(fill=BOTH,expand=YES)
frame.grid_columnconfigure(0,weight=1)
frame.grid_rowconfigure(2,weight=1)

savebutton = Button(frame,text="Save",fg="red",width=7,command=savebuttonCallBack)
savebutton.grid(row=1,column=2,columnspan=2,padx=2,pady=2,sticky='ne')

loadbutton = Button(frame, text="open", fg="blue",width=7,command=loadbuttonCallBack)
loadbutton.grid(row=1,column=1,padx=2,pady=2,sticky='ne')

filename = Entry(frame)
filename.grid(row=1,column=0,padx=2,pady=2,sticky='nswe')

contents = Text(frame,wrap=NONE)
contents.grid(row=2,column=0,columnspan=3,padx=2,pady=2,sticky='news')


#blackbutton = Button(frame, text="Black", fg="black")
#blackbutton.pack( side = BOTTOM)

# there is a "Scrolled text" method 
# better not put srollbar on the text widget, it will cover the end of lines
scrolly_text = Scrollbar(frame,command=contents.yview);
scrolly_text.grid(row=2,column=3,pady=2,sticky='nse')
contents['yscrollcommand'] = scrolly_text.set

scrollx_text = Scrollbar(frame,command=contents.xview,orient=HORIZONTAL);
scrollx_text.grid(row=3,column=0,columnspan=3,padx=2,sticky='swe')
contents['xscrollcommand'] = scrollx_text.set
#contents.config(yscrollcommand=scrollb_text.set);

# there is an idea that,write grid lines together may help dealing with layout issus. 





root.mainloop()
