num = "1, 2, 3, 4, 5, 6, 1, 1"
import random

hehe = num.count("3")

def fa():
    if hehe == 3:
        return "yes"
    elif hehe != 3:
        return "ok" + "hey"


print(fa())

def name_writter(name, age):
    return (name, age)

print(name_writter("hasan", 21))

# Asking to play with me question
playing = input("Do you want to Play? YES OR NO ")

if playing.lower() == "yes" or playing == "y":
    print("ok Lets play ")
else:
    quit()

score = 0

answer = input("What does CPU stand for? ").lower()
if answer == "central processing unit":
    print("Correct ")
    score += 1
else:
    print("Not correct")

answer = input("which funtion makes answers accept upper and lower cases ").lower()
if answer == ".lower":
    print("Correct ")
    score += 1
else:
    print("Not correct")

print("\nyour score is " + str(score) + "\n")
print("\nyour score is %" + str((score /2) * 100) + ".\n")

print("Random number mode ACTIVATED ")

r = random.randrange(0, 100)
playing2 = input("Do you want to know how beautiful you are between 1 and 100? Yes or No ").lower()
if playing2 == "yes" or playing2 == "y":
    print("\n" + str(r))
else:
    quit()








