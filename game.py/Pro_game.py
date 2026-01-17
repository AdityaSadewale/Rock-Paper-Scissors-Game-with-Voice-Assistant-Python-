import random

# Game rules display
print("🎮 Rock Paper Scissors Game Rules:")
print("1. Rock beats Scissors")
print("2. Scissors beats Paper")
print("3. Paper beats Rock")
print("4. Same choice means Tie\n")

# List of valid choices
choices = ["Rock", "Paper", "Scissors"]

# User input
user_choice = input("Enter your move (Rock, Paper, Scissors): ").capitalize()

# Validate input
if user_choice not in choices:
    print("❌ Invalid choice! Please choose Rock, Paper, or Scissors.")
else:
    # Computer choice
    computer_choice = random.choice(choices)

    print(f"\n👤 User choice: {user_choice}")
    print(f"💻 Computer choice: {computer_choice}\n")

    # Game logic
    if user_choice == computer_choice:
        print("🤝 It's a Tie!")

    elif user_choice == "Rock":
        if computer_choice == "Scissors":
            print("🏆 Rock smashes Scissors — You Win!")
        else:
            print("💻 Paper covers Rock — Computer Wins!")

    elif user_choice == "Paper":
        if computer_choice == "Rock":
            print("🏆 Paper covers Rock — You Win!")
        else:
            print("💻 Scissors cut Paper — Computer Wins!")

    elif user_choice == "Scissors":
        if computer_choice == "Paper":
            print("🏆 Scissors cut Paper — You Win!")
        else:
            print("💻 Rock smashes Scissors — Computer Wins!")
