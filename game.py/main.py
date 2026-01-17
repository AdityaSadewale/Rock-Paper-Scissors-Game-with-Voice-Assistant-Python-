import random

# List of choices
item_list = ["Rock", "Paper", "Scissor"]

# User input
user_choice = input("Enter your move (Rock, Paper, Scissor): ").capitalize()

# Computer choice
comp_choice = random.choice(item_list)

print(f"User choice = {user_choice}, Computer choice = {comp_choice}")

# Game logic
if user_choice == comp_choice:
    print("Both chose the same: Match Tie")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("Paper covers Rock = Computer Wins")
    else:
        print("Rock smashes Scissor = You Win")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("Scissor cuts Paper = Computer Wins")
    else:
        print("Paper covers Rock = You Win")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("Scissor cuts Paper = You Win")
    else:
        print("Rock smashes Scissor = Computer Wins")

else:
    print("Invalid input! Please enter Rock, Paper, or Scissor.")
