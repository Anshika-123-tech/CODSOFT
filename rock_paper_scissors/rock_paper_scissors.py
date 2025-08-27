import random

def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

# --- Main Game ---
print("🎮 Welcome to Rock-Paper-Scissors! 🎮")

user_score = 0
computer_score = 0

while True:
    user_choice = input("Enter rock, paper, or scissors: ").lower()
    
    if user_choice not in ["rock", "paper", "scissors"]:
        print("❌ Invalid choice. Try again.")
        continue
    
    computer_choice = get_computer_choice()
    print(f"🧑 You chose: {user_choice}")
    print(f"💻 Computer chose: {computer_choice}")
    
    winner = determine_winner(user_choice, computer_choice)
    
    if winner == "tie":
        print("🤝 It's a tie!")
    elif winner == "user":
        print("🎉 You win this round!")
        user_score += 1
    else:
        print("😢 Computer wins this round!")
        computer_score += 1
    
    print(f"📊 Score -> You: {user_score} | Computer: {computer_score}")
    
    play_again = input("Do you want to play again? (yes/no): ").lower()
    if play_again != "yes":
        print("👋 Thanks for playing! Final Score:")
        print(f"✅ You: {user_score} | 💻 Computer: {computer_score}")
        break

