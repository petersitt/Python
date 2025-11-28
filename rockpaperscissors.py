import random

def play():
    user = input("Choose rock, paper, or scissors: ").lower()
    options = ["rock", "paper", "scissors"]
    
    if user not in options:
        return "Invalid choice! Please try again."
    
    computer = random.choice(options)
    print(f"Computer chose: {computer}")

    if user == computer:
        return "It's a tie!"
    
    # Winning conditions
    if (user == "rock" and computer == "scissors") or \
       (user == "paper" and computer == "rock") or \
       (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose!"

# Run the game
print(play())
