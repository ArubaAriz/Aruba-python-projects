from tkinter import *
from PIL import ImageTk,Image

def every_100(text):
    final_text = ""
    for i in range(0, len(text)):
        final_text +=text[i]
        if (i%100==0 and i!=0):
            final_text += "\n"
    return final_text        

root = Tk()
root.title("Aruba's Everyday Newspaper")
root.geometry("1000x800")


texts = []
photos = []
for i in range(0,3):
    try:
        with open(f"{i+1}.txt") as file:
            text = file.read()
            texts.append(every_100(text))
    except FileNotFoundError:
        texts.append(f"File {i+1}.txt not found.")
        
    try:
        image = Image.open(f"{i+1}.png")
        #TODO: resize these images
        image = image.resize((250, 250), Image.LANCZOS)
        photos.append(ImageTk.PhotoImage(image))
    except FileNotFoundError:
        photos.append(None)

f0 = Frame(root, width=800, height=70)
Label (f0,text="Aruba's Everyday Newspaper", font="Lucida 24 bold").pack()
Label (f0, text="15 th July 2025", font="Lucida 16 italic").pack()
f0.pack()

# for i in range (0,3):
#     if photos[i] is not None:
#         f = Frame(root, width=900, height=600)
#         Label(f, text=texts[i], padx=22, pady=22).pack(side="left")
#         Label(f, image=photos[i], anchor="e").pack()
#         f.pack(anchor="w")
#     else:
#         f = Frame(root, width=900, height=600)
#         Label(f, text=texts[i], padx=22, pady=22).pack()
#         f.pack(anchor="w")
        
        
f1 = Frame (root,width=900,height=600)
Label(f1, text=texts[0] , padx = 22, pady = 22).pack(side = "left")
Label(f1, image=photos[0] , anchor="e").pack()
f1.pack(anchor = "w")

f2 = Frame (root,width=900,height=600 ,padx = 22, pady = 22)
Label(f2, text=texts[1] , padx = 22, pady = 22).pack(side = "right")
Label(f2, image=photos[1] , anchor="e").pack()
f2.pack(anchor = "w")

f3 = Frame (root,width=900,height=600)
Label(f3, text=texts[2] , padx = 22, pady = 22).pack(side = "left")
Label(f3, image=photos[2] , anchor="e").pack()
f3.pack(anchor = "w")


root.mainloop()