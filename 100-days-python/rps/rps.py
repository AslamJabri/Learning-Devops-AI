import random

rps = ["Rock","Paper","Scissors"]

user_input = int(input("What do you choose? Type 0 for Rock, 1 For Paper or 2 for Scissors. "))
    

computer_choice = random.randint(0,2)


if user_input > 2  or user_input < 0:
    print("Wrong number entered")
else:
    print(f"User choose {rps[user_input]}")
    print(f"Computer choose {rps[computer_choice]}")
    if user_input == 0 and computer_choice == 2:
        print("User wins")
    elif user_input == 1 and computer_choice == 0:
        print("User wins")
    elif user_input == 2 and computer_choice == 1:
        print("User Wins")
    elif user_input == computer_choice:
        print("Tie")
    else:
        print("Computer Wins")