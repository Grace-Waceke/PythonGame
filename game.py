import random
user_action = input("Enter a choice(Rock, Paper, Scissors ): ")
possible_actions = ["Rock", "Paper", "Scissors"]
computer_action = random.choice(possible_actions)
print(f"\nYou choose{user_action}, computer choose {computer_action}. \n")
if user_action == computer_action:
    print(f"Both players selected{user_action}. It's a tie")
elif user_action == "Rock":
    if computer_action == "Scissors":
        print("Rock smashes scissors! You win!")
    else:
        print("Paper covers rock! You lose.")
elif user_action == "paper":
    if computer_action == "rock":
        print("Paper covers rock! You win!")
    else:
        print("Scissors cuts paper! You lose.")
elif user_action == "scissors":
    if computer_action == "paper":
        print("Scissors cuts paper! You win!")
    else:
        print("Rock smashes scissors! You lose.")
        play_again = input("Play again? (y/n): ")
       
