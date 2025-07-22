from tkinter import *
window =  Tk()
window.title("Aruba's GUI")
#widhth x height 
window.geometry("700x700")
#widhth, height 
window.minsize(300, 300)
#widhth, height 
window.maxsize(1200, 1200)
#adding text to ur window
text = Label (text="Welcome to PyCharm")
text.pack()
#adding phtoto to ur gui# python doesnt directly support jpg but takes png
#so we need to convert jpg to png
photo = PhotoImage(file="1.png")
Label = Label(image=photo)
Label.pack()


# image = Image.open("1.jpg")
# photo = ImageTk.PhotoImage(image)
# photo_Label = Label(image=photo)
# photo.pack()

#Important Label options
# text = "This is a label"
# font = ("Arial", 24, "bold") or font = "Arial 24 bold" 
# fg = "red" #foreground color  
# bg/bd = "black" #background color
# padx = padding x  
# pady = padding y
# borderwidth = 5 #border width
# relief = "sunken,raised,groove, ridge" #border style
# Label = Label(text=text, font=font, fg=fg, bg=bg, )

#Important pack options
# anchor = "n, s, e, w, ne, nw, se, sw" #position of the widget
# anchor = "center" #default position
# side = "top, bottom, left, right" #side of the window #default side is top
# fill = "x, y, both" #fill the space
# expand = True/False #expand the widget to fill the space
# padx = padding x
# pady = padding y
# frames    f1 = Frame (root,bg="gray",borderwidth=6, relief=SUNKEN)
# f1.pack(side=LEFT,fill="y")
# f2= Frame(root,bg="gray",borderwidth=6, relief=SUNKEN)
# f2.pack(side=TOP,fill="x")
# buttons   b1=Button(f1,text="Click Me",font="Arial 12 bold",fg="red",bg="black",padx="15",pady="15",command=hello)
# b1.pack(side=LEFT)
# Variableclasses in Tkinter
# StringVar, IntVar, DoubleVar, BooleanVar
# These are used to store the value of a widget and can be used to get or set
# globalvaribale bnanan is not a good practice in Tkinter
# grids to make form layout
# checkbox = IntVar()  # Create an IntVar to hold the state of the checkbox
# # Create a Checkbutton widget
# checkbox = Checkbutton(text="Check me")
# checkbox.pack()
# create rectangle = Canvas(window, width=200, height=100)
# create_rectangle = create_rectangle.create_rectangle(50, 25, 150, 75, fill="blue", outline="black")
# create_rectangle.pack() 
# create line = Canvas(window, width=200, height=100)
# create_line = create_line.create_line(0, 0, 200, 100, fill="red", width=2)
# create_line.pack()
# create text = Canvas(window, width=200, height=100)
# create_text = create_text.create_text(100, 50, text="Hello, Tkinter!", font=("Arial", 16), fill="green")
# create_text.pack()  
# create oval = Canvas(window, width=200, height=100)
# create_oval = create_oval.create_oval(50, 25, 150, 75, fill="yellow", outline="black")
# create_oval.pack()
# canvas Widget = Canvas(window, width=400, height=400)
# canvas.pack()

# def Aruba(event):
#     print(f"Button clicked at {event.x}, {event.y}")
# widget = Button(root,text ="Click Me Please")
# widget.pack()
# widget.bind('<Button-1>',Aruba)
# widget.bind('<Double-1>',quit)  # Double-click to quit the application

# def myfunc():
#     print("I am a function")
    
# mymenu = Menu(root)
# mymenu.add_command(label="File", command=myfunc)
# mymenu.add_command(label="Exit", command=quit)
# root.config(menu=mymenu)



# tmsg.askretrycancel("Retry", "This is a retry message")
# tmsg.askyesno("Yes/No", "Do you want to continue?")
# tmsg.showinfo("Information", "This is an information message")
# tmsg.showwarning("Warning", "This is a warning message")
# tmsg.showerror("Error", "This is an error message")
#tmsg.showinfo("Help", "This is a help message.")

# mysldier = Scale (window,from_=0, to=100, orient=HORIZONTAL, length=200)

# Radiobutton = Radiobutton(window, text="Option 1", value=1).pack(anchor=W)

# Listbox = Listbox(window, height=5, width=20)
# Listbox.insert(1, "Item 1") 

#to connect the scrollbar to the listbox
#1. widget (yscrollcommand=scrollbar.set)
#2. scrolbar.config(comand=widget.yview)

#statusbar = Label(window, text="Status Bar", bd=1, relief=SUNKEN, anchor=W)
# statusbar.pack(side=BOTTOM, fill=X)   



window.mainloop()