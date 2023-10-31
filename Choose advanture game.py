name = input("Type your name: ")
age = int(input("Type your age: "))

if age <= 18:
    print(f"Hello, {name}, you are too young to play. Get out.")
else:
    print(f"You are old enough to play, {name}. Come in.")

print(f"Welcome, {name}, age {age}, to this adventure")
print("In order to get out of this game loop adventure you need to find the right answer otherwise the game will tell you what happend"
      "and then send you back to the first question until you find the right answer. GOOD LUCk")

while True:
    answer = input(
        "You are on a dirt road, and it has come to an end. You can go RIGHT or LEFT. Which way would you like to go? ").lower()

    if answer == "left":
        while True:
            answer = input(
                "You come to a river. You can walk around it or swim across. Type SWIM or WALK to decide: ").lower()

            if answer == "swim":
                print("You swim across, but an alligator ate you. Bad luck, YOU DIED")
                break
            elif answer == "walk":
                print("You walked for many miles, and a tiger attacked for some reason, YOU DIED")
                break
            else:
                print("Not a valid option. Please type SWIM or WALK.")

    elif answer == "right":
        while True:
            answer = input(
                "You come to a bridge, it looks old. Do you want to cross it or go back? (cross/back): ").lower()

            if answer == "back":
                print(
                    "You go back and live a normal life and you died because of natural reasons. Such a boring option.")
                break

            elif answer == "cross":
                while True:
                    answer = input(
                        "You cross the bridge, and there is a stranger there. Do you want to talk to them? (Yes/No): ").lower()

                    if answer == "yes":
                        print(
                            "You talk to them, and they give you some gold to invest in bitcoin. Now you are rich! YOU WON.")
                        quit()

                    elif answer == "no":
                        print("You ignore the stranger, and they are pissed off. They beat you to death. YOU LOSE.")
                        break

                    else:
                        print("Not a valid option. Please type Yes or No.")

            else:
                print("Not a valid option. Please type cross or back.")

    else:
        print("Not a valid option. Please type LEFT or RIGHT.")

print(f"Thank you for trying, {name}, age {age} - Now get out.")