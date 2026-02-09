import random as r
def guessing_game():
    number = r.randint(0,10)
    count =0
    while True:
        try:
            user_guess = int(input("Guess the Number out of 1-10:"))
        except ValueError:
            print("Please enter a valid number")
            continue
        count +=1
        if number == user_guess:
                return f"You have guessed The right number {number} and count is {count}"
        elif user_guess > number:
                print ("Please go down")
        else:
                print("Please Go up")

    
print(guessing_game())