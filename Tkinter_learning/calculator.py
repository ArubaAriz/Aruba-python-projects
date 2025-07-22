from tkinter import *
root = Tk()
root.title("Aruba's Calculator")
root.geometry("370x650")
icon = PhotoImage(file="C:\\Users\\User\\Desktop\\Tkinter_learning\\calc.png")
root.iconphoto(False, icon)
root.config(bg="darkgray")  


def click(event):
    global scval
    text = event.widget.cget("text")
    print(text)
    if text == "=":
        if scval.get().isdigit():
            value = int(scval.get())
        else:
            try:
                value = eval(screen.get())
            except Exception as e:
                print("Error:", e)
                value = "Error"
        
        scval.set(value)
        screen.update()
    elif text == "C":
        scval.set("")
        screen.update()
    else:
        scval.set(scval.get() + text)
        screen.update()

scval = StringVar()
scval.set("")
screen = Entry(root, textvariable=scval, font="lucida 20 bold", bg="lightgray", bd=10)
screen.pack(fill=X, padx=10, pady=10)  

f = Frame(root, bg="lightgray")
f.pack(padx=10, pady=10)  # pack the Frame in root and the buttons inside frame with grid

for i in range(9):
    row = i // 3
    col = i % 3
    b = Button(f, text=str(i+1), font="lucida 15 bold", bg="lightgray", bd=10, width=4, height=2)
    b.bind("<Button-1>", click)
    b.grid(row=row, column=col, padx=5, pady=5)  
 
#operation buttons
b = Button(f, text="0", font="lucida 15 bold", bg="lightgray", bd=10, width=4, height=2)
b.bind("<Button-1>", click)
b.grid(row=3, column=0, padx=5, pady=5)
b = Button(f, text="%", font="lucida 15 bold", bg="lightgray", bd=10, width=4, height=2)
b.bind("<Button-1>", click) 
b.grid(row=3, column=1, padx=5, pady=5)
b = Button(f, text="*", font="lucida 15 bold", bg="lightgray", bd=10, width=4, height=2)
b.bind("<Button-1>", click)     
b.grid(row=3, column=2, padx=5, pady=5)
b = Button(f, text="-", font="lucida 15 bold", bg="lightgray", bd=10, width=4, height=2)
b.bind("<Button-1>", click)
b.grid(row=4, column=0, padx=5, pady=5)
b = Button(f, text="+", font="lucida 15 bold", bg="lightgray", bd=10, width=4, height=2)
b.bind("<Button-1>", click)
b.grid(row=4, column=1, padx=5, pady=5)
b = Button(f, text="/", font="lucida 15 bold", bg="lightgray", bd=10, width=4, height=2)
b.bind("<Button-1>", click) 
b.grid(row=4, column=2, padx=5, pady=5)
b = Button(f, text="=", font="lucida 15 bold", bg="lightgray", bd=10, width=4, height=2)
b.bind("<Button-1>", click)
b.grid(row=5, column=0, columnspan=3, padx=5, pady=5) 
b = Button(f, text="C", font="lucida 15 bold", bg="lightgray", bd=10, width=4, height=2)
b.bind("<Button-1>", click)
b.grid(row=5, column=0, padx=5, pady=5) 


root.mainloop()