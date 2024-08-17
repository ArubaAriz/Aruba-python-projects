import tkinter as tk
from tkinter import messagebox, simpledialog
import random

def check_winner():
    global winner
    for combo in [[0, 1, 2], [3, 4, 5], [6, 7, 8], [0, 3, 6], [1, 4, 7], [2, 5, 8], [0, 4, 8], [2, 4, 6]]:
        if buttons[combo[0]]["text"] == buttons[combo[1]]["text"] == buttons[combo[2]]["text"] != "":
            buttons[combo[0]].config(bg="green")
            buttons[combo[1]].config(bg="green")
            buttons[combo[2]].config(bg="green")
            winner = True
            messagebox.showinfo("Tic-Tac-Toe", f"Player {buttons[combo[0]]['text']} wins!")
            restart_game()
            return

    if all(button["text"] != "" for button in buttons):
        messagebox.showinfo("Tic-Tac-Toe", "It's a tie!")
        restart_game()

def Button_click(index):
    global winner

    if buttons[index]["text"] == "" and not winner:
        buttons[index]["text"] = current_player
        check_winner()

        if not winner:
            toggle_player()
            if game_mode == '1' and current_player == "O":  # Computer's turn
                computer_move()

def computer_move():
    empty_spots = [i for i, button in enumerate(buttons) if button["text"] == ""]
    if empty_spots:
        index = random.choice(empty_spots)
        buttons[index]["text"] = current_player
        check_winner()
        if not winner:
            toggle_player()

def toggle_player():
    global current_player
    current_player = "X" if current_player == "O" else "O"
    label.config(text=f"Player {current_player}'s turn")

def restart_game():
    global current_player, winner
    answer = messagebox.askyesno("Game Over", "Do you want to play again?")
    if answer:
        for button in buttons:
            button.config(text="", bg="SystemButtonFace")  # Reset all buttons
        current_player = "X"
        winner = False
        label.config(text=f"Player {current_player}'s turn")
    else:
        root.quit()

root = tk.Tk()
root.withdraw()  # Hide the main window while the dialog is open

game_mode = simpledialog.askstring("Choose Mode", "Enter '2' for Two Player mode or '1' to play against Computer:")

root.deiconify()  # Show the main window again

if game_mode not in ['1', '2']:
    messagebox.showerror("Invalid Option", "Please restart and choose a valid mode.")
    root.quit()

root.title("Tic-Tac-Toe")

buttons = [tk.Button(root, text="", font=("normal", 25), width=6, height=2, command=lambda i=i: Button_click(i)) for i in range(9)]

for i, button in enumerate(buttons):
    button.grid(row=i//3, column=i % 3)

current_player = "X"
winner = False
label = tk.Label(root, text=f"Player {current_player}'s turn", font=("normal", 16))
label.grid(row=3, column=0, columnspan=3)

root.mainloop()
