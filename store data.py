
def view():
    with open("password2.txt", 'r') as f:
        data = f.readlines()
    for line in data:
        print(line)


def add():
    age = int(input("enter you age it has to be a number"))
    if age <= 18:
        print("you are too small")
        quit()
    name = input("enter you name")
    with open("password2.txt", 'a') as f:
        f.write(name + "/" + str(age) + "\n")


def delete_all_passwords():
    confirmation = input("Are you sure you want to delete all passwords? (yes/no): ")
    if confirmation.lower() == "yes":
        with open("password2.txt", 'w') as f:
            f.truncate(0)
        print("All passwords have been deleted.")
    else:
        print("Operation canceled.")


while True:
    choice = input("do you want to add passwords? use functions:(q, add, view, delete_all_passwords)")
    if choice == "add":
        add()
    elif choice == "view":
        view()
    elif choice == "delete_all_passwords" or choice == "del":
        delete_all_passwords()
    elif choice == "q" or choice == "quit":
        quit()
    else:
        print("invalid word")
