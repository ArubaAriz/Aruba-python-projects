from tkinter import *
root = Tk()
root.title("Aruba's GUI")
root.geometry("500x400")
# Set the icon for the window
icon = PhotoImage(file="C:\\Users\\User\\Desktop\\Tkinter_learning\\shield.png")
root.iconphoto(False, icon)

root.config(bg="lightblue")  # Set the background color of the window



root.mainloop()
exit()
# OOPS 
from tkinter import *              
#root everywhere is self and window here 
class GUI(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x400")

    def status(self):
        self.Var = StringVar()
        self.Var.set("Ready")
        self.statusbar = Label(self, textvariable=self.Var, bd=1, relief=SUNKEN, anchor=W,bg="darkgray", fg="black",)
        self.statusbar.pack(side=BOTTOM, fill=X, )
        
if __name__ == '__main__':
    window = GUI()
    window.status()
    window.mainloop()
    # window.mainloop()  # This line is not needed in the class-based approach







exit()
from tkinter import *
from tkinter import messagebox as tmsg
root=Tk()
root.title("Aruba's GUI")

def update():
    root.geometry(f"{width.get()}x{height.get()}")

Label(text="Window Resizer", font="Arial 16 bold").pack(pady=10)
width = StringVar()
height = StringVar()
Entry(root, textvariable=width).pack()
Entry(root, textvariable=height).pack()
Button(root, text="Apply",command=update).pack()

root.mainloop()


exit()
from tkinter import *
from tkinter import messagebox as tmsg
root=Tk()
root.title("Aruba's GUI")
root.geometry("500x400")
# def hello():
#     print("Hello, Tkinter!")
# # text= Label(text="Ready",anchor="s",font="Arial 12 bold",fg="red", bg="black")
# # text.pack(side=BOTTOM,expand=True,padx=10,pady=10)
# f1 = Frame (root,bg="gray",borderwidth=6, relief=SUNKEN)
# f1.pack(side=LEFT,fill="y")
# f2= Frame(root,bg="gray",borderwidth=6, relief=SUNKEN)
# f2.pack(side=TOP,fill="x")
# l1 =Label(f1,text="Project Tkinter-PyCharm")
# l1.pack(pady=162)
# l2 =Label(f2,text="Welcome to sublime text editor",font="Arial 12 bold",fg="red",pady="22")
# l2.pack()
# b1=Button(f1,text="Click Me",font="Arial 12 bold",fg="red",bg="black",padx="15",pady="15",command=hello)
# b1.pack(side=LEFT)
# def getvals():
#     print(uservalue.get())
#     print(passvalue.get()) 
# user = Label(root,text="Username")
# password = Label (root,text="Password")
# user.grid()
# password.grid(row=1)
# uservalue = StringVar()
# passvalue = StringVar()
# userentry = Entry (root,textvariable = uservalue)
# passentry = Entry (root,textvariable = passvalue, show="*")
# userentry.grid(row=0,column=1)
# passentry.grid(row=1,column=1)
# Button(text="Sumbit",command=getvals).grid()
# checkbox = IntVar()  # Create an IntVar to hold the state of the checkbox
# # Create a Checkbutton widget
# checkbox = Checkbutton(text="Check me", variable=checkbox).grid()
# def Aruba(event):
#     print(f"Button clicked at {event.x}, {event.y}")
# widget = Button(root,text ="Click Me Please")
# widget.pack()
# widget.bind('<Button-1>',Aruba)
# widget.bind('<Double-1>',quit)  # Double-click to quit the application

def myfunc():
    print("I am a function")
    
 
def help():
    print("Help menu clicked")
    tmsg.showinfo("Help", "This is a help message.")   
    

# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)

mainmenu = Menu(root)
m1=Menu (mainmenu,tearoff=0)  # tearoff=0 means the menu cannot be torn off
m1.add_command(label="New Project", command=myfunc)
m1.add_command(label="New File", command=myfunc)
m1.add_command(label="Open", command=myfunc)
m1.add_separator()  # Adds a separator line in the menu
m1.add_command(label="Save", command=myfunc)
m1.add_command(label="Save As", command=myfunc)
m1.add_separator()  
m1.add_command(label="Exit", command=quit)
root.config(menu=mainmenu)
mainmenu.add_cascade(label="File", menu=m1)
 
m2=Menu (mainmenu,tearoff=0)
m2.add_command(label="Cut", command=myfunc)
m2.add_command(label="Copy", command=myfunc)
m2.add_command(label="Paste", command=myfunc)   
mainmenu.add_cascade(label="Edit", menu=m2)

m3=Menu (mainmenu,tearoff=0)
m3.add_command(label="i am here to help you", command=help)
mainmenu.add_cascade(label="Help ", menu=m3)
root.config(menu=mainmenu)

myslider = Scale (root,from_=0, to=100, orient=HORIZONTAL, length=200 , tickinterval=50 ) #tickinterval=50 means the slider will have ticks at every 50 units
myslider.set(50)  # Set the initial value of the slider to 50
myslider.pack()

var = IntVar()  # Create an IntVar to hold the value of the radiobutton
Radiobutton(root, text="Option 1", variable=var, value=1).pack  
Radio = Radiobutton(root, text="Option 1", value=1).pack(anchor=W)

# Listbox = Listbox(root, height=5, width=20)
# Listbox.insert(1, "Item 1")
# Listbox.pack() 
# Button (root , text = "add item", command= myfunc).pack()

#to connect the scrollbar to the listbox
#1. widget (yscrollcommand=scrollbar.set)
#2. scrolbar.config(comand=widget.yview)

scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=Y)  

listbox = Listbox(root , yscrollcommand=scrollbar.set)
for i in range (344):
    listbox.insert(END, f"Item {i+1}") 
listbox.pack(fill=BOTH, padx=22)  
scrollbar.config(command=listbox.yview)  # Connect the scrollbar to the listbox






