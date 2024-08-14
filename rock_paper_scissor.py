import random
list=["Rock","Paper","Scissor"]

user_choice = input("Enter your move = Rock, Paper, Scissor = ")
comp_choice = random.choice(list)

print (f"User choice = {user_choice}, Computer choice = {comp_choice}")


if user_choice == comp_choice:
    print("Both chooses same: = Match Tie ")
    
elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer Wins")
    else:
        print("Rock smashes Scissor = You Win ")
        
                
elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts paper = Computer Wins")
    else:
        print("Paper covers Rock = You Win ")
        
elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts paper = You Win")
    else:
        print("Rock smashes Scissor = Computer Wins ")        