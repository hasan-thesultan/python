import random

user_wins = 0
computer_wins = 0
draws = 0

options = ["rock", "paper", "scissors"]

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit:  ").lower()
    if user_input.lower() == "q":
        break

    if user_input not in ["rock", "paper", "scissors"]:
        continue

    random_number = random.randint(0, 2)
    # rock : 0, paper : 1, scissors : 2
    computer_pick = options[random_number]
    print("Computer picked", computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissors":
        print("You WON!")
        user_wins += 1
        continue
    elif user_input == "paper" and computer_pick == "rock":
        print("You WON!")
        user_wins += 1
        continue
    elif user_input == "scissors" and computer_pick == "paper":
        print("You WON!")
        user_wins += 1
        continue
    elif user_input == computer_pick:
        print("Same, No Points!!")
        draws += 1
        continue
    else:
        print("You LOST!")
        computer_wins += 1

print("Your wins: ", user_wins)
print("Computer wins: ", computer_wins)
print("Draw: ", draws)
print("Goodbye!")