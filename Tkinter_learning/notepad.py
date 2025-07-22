from tkinter import *
from tkinter import messagebox as tmsg
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os 

#defining functions for menu options
def newfile():
    global file
    file = None
    root.title("Untitled-Notepad")
    textarea.delete(1.0, END)
    
def openfile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if file == "":
        file = None
    else:
        root.title(os.path.basename(file)+" - Notepad")
        textarea.delete(1.0, END)
        f = open(file, "r")
        textarea.insert(1.0, f.read())
        f.close()
        
def savefile():
    global file
    if file == None:
        file = asksaveasfilename(initialfile="Untitled.txt", defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(textarea.get(1.0, END))
            f.close()
            root.title(os.path.basename(file)+" - Notepad")
        
def saveasfile():
    global file
    file = asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    f = open (file, "w")
    f.write(textarea.get(1.0, END))
    f.close()
    
def undo():
    textarea.event_generate("<<Undo>>")
def redo():
    textarea.event_generate("<<Redo>>")
def cut():
    textarea.event_generate("<<Cut>>")
def copy():
    textarea.event_generate("<<Copy>>")
def paste():
    textarea.event_generate("<<Paste>>")
def selectall():
    textarea.event_generate("<<SelectAll>>")
def about():
    tmsg.showinfo("Notepad", "This is a simple notepad application created using Tkinter.\nVersion 1.0\nCreated by Aruba Ariz")
def help():
    tmsg.showinfo("Help", "This is a help message.")

if __name__ == '__main__':
    root = Tk()
    root.title("Untitled-Notepad")
    root.geometry("500x500")
    try:
        icon = PhotoImage(file="C:/Users/User/Desktop/Tkinter_learning/notepad.png")
        root.iconphoto(False, icon)
    except Exception:
        pass
    root.config(bg="darkgray")  

    textframe = Frame(root)
    textframe.pack(expand = True, fill=BOTH)
    #scrollbar
    scrollbar =Scrollbar(textframe)
    scrollbar.pack(side = RIGHT, fill = Y)
    
    #Add a text area
    textarea = Text(textframe, font="lucida 15", bg="white", bd=10)
    textarea.pack(expand=True, fill=BOTH)
    scrollbar.config(command = textarea.yview)
    file = None


    #Let's create a menubar
    menubar = Menu(root)
    #filemenu begins
    filemenu = Menu(menubar, tearoff=0)
    #to open a new file
    filemenu.add_command(label="New", command=newfile)
    #to open an existing file
    filemenu.add_command(label="Open", command=openfile)    
    #to save the current file
    filemenu.add_command(label="Save", command=savefile)
    filemenu.add_command(label="Save As", command=saveasfile)
    filemenu.add_command(label="Exit", command=root.quit)
    menubar.add_cascade(label="File", menu=filemenu)
    #Edit menu begins

    #Edit menu
    editmenu = Menu(menubar, tearoff=0)
    editmenu.add_command(label="Undo", command=undo)
    editmenu.add_command(label="Redo", command=redo)
    editmenu.add_command(label="Cut", command=cut)  
    editmenu.add_command(label="Copy", command=copy)
    editmenu.add_command(label="Paste", command=paste)
    editmenu.add_command(label="Select All", command=selectall)
    menubar.add_cascade(label="Edit", menu=editmenu)

    #Help menu begins
    helpmenu = Menu(menubar, tearoff=0)
    helpmenu.add_command(label="About", command=about)
    helpmenu.add_command(label="Help", command=help)
    menubar.add_cascade(label="Help", menu=helpmenu)

    root.config(menu=menubar)
    root.mainloop()