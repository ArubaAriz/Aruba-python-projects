from tkinter import *
from tkinter import filedialog
from Crypto.Cipher import AES, DES
import base64
import rsa

# ------------------ RSA Key Pair ------------------ #
public_key, private_key = rsa.newkeys(512)

# ------------------ THEME CONFIG ------------------ #
theme = {
    "light": {
        "bg": "#ffe6f0",
        "button": "#e6ccff",
        "text_bg": "white",
        "text_fg": "black"
    },
    "dark": {
        "bg": "#1e1e2f",
        "button": "#5e5eff",
        "text_bg": "#2d2d44",
        "text_fg": "white"
    }
}
current_theme = "light"

# ------------------ GUI Setup ------------------ #
root = Tk()
root.title("Text Encryptor")
root.geometry("600x650")
icon = PhotoImage(file="C:\\Users\\User\\Desktop\\Tkinter_learning\\shield.png")
root.iconphoto(False, icon)

FONT_TITLE = ("Segoe UI", 16, "bold")
FONT_LABEL = ("Comic Sans MS", 11)
FONT_TEXT = ("Arial", 10)

# ------------------ Logic Helpers ------------------ #
def pad(text):
    while len(text) % 16 != 0:
        text += ' '
    return text

def pad_des(text):
    while len(text) % 8 != 0:
        text += ' '
    return text

def unpad(text):
    return text.rstrip(' ')

def unpad_des(text):
    return text.rstrip(' ')

# ------------------ Encryption Functions ------------------ #
def aes_encrypt(plain_text):
    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_ECB)
    padded = pad(plain_text)
    return base64.b64encode(cipher.encrypt(padded.encode())).decode()

def aes_decrypt(encrypted_text):
    key = b'Sixteen byte key'
    cipher = AES.new(key, AES.MODE_ECB)
    decoded = base64.b64decode(encrypted_text)
    return unpad(cipher.decrypt(decoded).decode())

def des_encrypt(plain_text):
    key = b'8bytekey'
    cipher = DES.new(key, DES.MODE_ECB)
    padded = pad_des(plain_text)
    return base64.b64encode(cipher.encrypt(padded.encode())).decode()

def des_decrypt(encrypted_text):
    key = b'8bytekey'
    cipher = DES.new(key, DES.MODE_ECB)
    decoded = base64.b64decode(encrypted_text)
    return unpad_des(cipher.decrypt(decoded).decode())

def rsa_encrypt(plain_text):
    return base64.b64encode(rsa.encrypt(plain_text.encode(), public_key)).decode()

def rsa_decrypt(encrypted_text):
    try:
        decoded = base64.b64decode(encrypted_text.encode())
        return rsa.decrypt(decoded, private_key).decode()
    except:
        return "Decryption error."

# ------------------ Core Logic ------------------ #
def encrypt():
    text = input_box.get("1.0", END).strip()
    output_box.delete("1.0", END)
    algorithm = selected_algorithm.get()

    if algorithm == "AES":
        output_box.insert(END, aes_encrypt(text))
    elif algorithm == "DES":
        output_box.insert(END, des_encrypt(text))
    elif algorithm == "RSA":
        output_box.insert(END, rsa_encrypt(text))
    else:
        output_box.insert(END, "Please select a valid algorithm.")

def decrypt():
    encrypted = input_box.get("1.0", END).strip()
    output_box.delete("1.0", END)
    algorithm = selected_algorithm.get()

    if algorithm == "AES":
        output_box.insert(END, aes_decrypt(encrypted))
    elif algorithm == "DES":
        output_box.insert(END, des_decrypt(encrypted))
    elif algorithm == "RSA":
        output_box.insert(END, rsa_decrypt(encrypted))
    else:
        output_box.insert(END, "Please select a valid algorithm.")

def save_to_file():
    content = output_box.get("1.0", END).strip()
    if not content:
        output_box.insert(END, "\n(No output to save)")
        return
    file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file_path:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)

def toggle_theme():
    global current_theme
    current_theme = "dark" if current_theme == "light" else "light"
    th = theme[current_theme]

    # Update root and labels
    root.configure(bg=th["bg"])
    title_label.configure(bg=th["bg"])
    dropdown_label.configure(bg=th["bg"], fg=th["text_fg"])
    input_label.configure(bg=th["bg"], fg=th["text_fg"])
    output_label.configure(bg=th["bg"], fg=th["text_fg"])

    # Update text areas
    input_box.configure(bg=th["text_bg"], fg=th["text_fg"])
    output_box.configure(bg=th["text_bg"], fg=th["text_fg"])

    # Update button colors
    for btn in all_buttons:
        btn.configure(bg=th["button"], fg="black")

# ------------------ GUI Layout ------------------ #
# Title
title_label = Label(root, text="Text Encryption App", font=FONT_TITLE, fg="purple", bg=theme[current_theme]["bg"])
title_label.pack(pady=10)

# Dropdown
dropdown_frame = Frame(root, bg=theme[current_theme]["bg"])
dropdown_frame.pack(pady=5)
dropdown_label = Label(dropdown_frame, text="Select Algorithm:", bg=theme[current_theme]["bg"], font=FONT_LABEL)
dropdown_label.pack(side=LEFT, padx=5)
selected_algorithm = StringVar()
selected_algorithm.set("AES")
algo_menu = OptionMenu(dropdown_frame, selected_algorithm, "AES", "DES", "RSA")
algo_menu.pack(side=LEFT)

# Input Area
input_label = Label(root, text="Enter Text / Encrypted Text:", font=FONT_LABEL, bg=theme[current_theme]["bg"])
input_label.pack(pady=5)
input_box = Text(root, height=6, width=60, font=FONT_TEXT, bd=2, relief=SUNKEN,
                 bg=theme[current_theme]["text_bg"], fg=theme[current_theme]["text_fg"])
input_box.pack(padx=10, pady=5)

# Buttons
button_frame = Frame(root, bg=theme[current_theme]["bg"])
button_frame.pack(pady=10)
encrypt_btn = Button(button_frame, text="Encrypt", font=FONT_LABEL, command=encrypt,
                     bg=theme[current_theme]["button"], fg="black", padx=10, pady=5)
decrypt_btn = Button(button_frame, text="Decrypt", font=FONT_LABEL, command=decrypt,
                     bg=theme[current_theme]["button"], fg="black", padx=10, pady=5)
save_btn = Button(button_frame, text="Save Output", font=FONT_LABEL, command=save_to_file,
                  bg=theme[current_theme]["button"], fg="black", padx=10, pady=5)
toggle_btn = Button(button_frame, text="Dark Mode", font=FONT_LABEL, command=toggle_theme,
                    bg=theme[current_theme]["button"], fg="black", padx=10, pady=5)

encrypt_btn.pack(side=LEFT, padx=10)
decrypt_btn.pack(side=LEFT, padx=10)
save_btn.pack(side=LEFT, padx=10)
toggle_btn.pack(side=LEFT, padx=10)

all_buttons = [encrypt_btn, decrypt_btn, save_btn, toggle_btn]

# Output Box
output_label = Label(root, text="Output:", font=FONT_LABEL, bg=theme[current_theme]["bg"])
output_label.pack(pady=5)
output_box = Text(root, height=6, width=60, font=FONT_TEXT, bd=2, relief=SUNKEN,
                  bg=theme[current_theme]["text_bg"], fg=theme[current_theme]["text_fg"])
output_box.pack(padx=10, pady=5)

root.mainloop()
