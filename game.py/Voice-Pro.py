import random
import time
import winsound   # BUILT-IN (no pip needed)

# Voice setup
try:
    import pyttsx3
    engine = pyttsx3.init()
    engine.setProperty('rate', 150)

    voices = engine.getProperty('voices')
    engine.setProperty('voice', voices[1].id)  # female voice (change to 0 for male)

    voice_on = True
except:
    voice_on = False

def speak(text):
    if voice_on:
        engine.say(text)
        engine.runAndWait()

# Game start
print("🎮 Welcome to Rock Paper Scissors 🎮")
player_name = input("Enter your name: ")

speak(f"Welcome {player_name}. Let's start the game.")

choices = ["Rock", "Paper", "Scissor"]
player_score = 0
computer_score = 0

# Best of 3 rounds
for round_no in range(1, 4):
    print(f"\n🔁 Round {round_no}")
    user_choice = input("Choose Rock, Paper, or Scissor: ").capitalize()
    computer_choice = random.choice(choices)

    print(f"{player_name}: {user_choice}")
    print(f"Computer: {computer_choice}")

    speak(f"{player_name} chose {user_choice}")
    speak(f"Computer chose {computer_choice}")

    if user_choice == computer_choice:
        print("🤝 Tie Round")
        speak("This round is a tie.")

    elif (user_choice == "Rock" and computer_choice == "Scissor") or \
         (user_choice == "Paper" and computer_choice == "Rock") or \
         (user_choice == "Scissor" and computer_choice == "Paper"):

        print("🏆 You Win This Round!")
        player_score += 1
        winsound.Beep(1000, 300)
        speak("Excellent! You win this round.")

    elif user_choice in choices:
        print("💻 Computer Wins This Round!")
        computer_score += 1
        winsound.Beep(400, 300)
        speak("Computer wins this round. Don't give up.")

    else:
        print("❌ Invalid Input")
        speak("Invalid input. Please choose correctly.")

    time.sleep(1)

# Final result
print("\n🏁 Final Result")
print(f"{player_name} Score: {player_score}")
print(f"Computer Score: {computer_score}")

if player_score > computer_score:
    print(f"🎉 Congratulations {player_name}, YOU WON THE GAME!")
    speak(f"Congratulations {player_name}. You are the final winner.")

elif computer_score > player_score:
    print("💻 Computer Won the Game")
    speak("Computer won the game. Failure is part of success. Try again.")

else:
    print("🤝 Game Tie")
    speak("The game is a tie. Well played.")

print("\n🙏 Thanks for playing!")
speak("Thank you for playing. See you next time.")
