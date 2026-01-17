import random

item_list = ["Rock", "Paper", "Scissor"]

user_choice = input("Enter your move (Rock, Paper, Scissor): ").capitalize()
comp_choice = random.choice(item_list)

print(f"\nUser choice = {user_choice}")
print(f"Computer choice = {comp_choice}\n")

if user_choice == comp_choice:
    print("🤝 Match Tie")
    print("Advice: Try again. You are doing well!")

elif user_choice == "Rock":
    if comp_choice == "Paper":
        print("💻 Computer Wins")
        print("Advice: Don't worry. Learn and try a different move next time.")
    else:
        print("👤 You Win")
        print("Advice: Good choice! Keep playing with confidence.")

elif user_choice == "Paper":
    if comp_choice == "Scissor":
        print("💻 Computer Wins")
        print("Advice: Losing is part of learning. Keep practicing.")
    else:
        print("👤 You Win")
        print("Advice: Smart move! Thinking ahead helps you win.")

elif user_choice == "Scissor":
    if comp_choice == "Paper":
        print("👤 You Win")
        print("Advice: Excellent! Quick decisions bring success.")
    else:
        print("💻 Computer Wins")
        print("Advice: Stay calm and try again. You can win next round.")

else:
    print("❌ Invalid Input")
    print("Advice: Please enter only Rock, Paper, or Scissor.")
