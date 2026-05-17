import random

print("Welcome to the Number Guessing Game!")

def choosen_number():
    number = random.randint(1,101)
    print("I'm thinking of a number between 1 and 100.")
    return number

def mode_of_game():
    while True:
        mode = input("Choose a difficulty. Type 'easy' or 'hard': ").lower()
        if mode == 'easy' or mode == 'hard':
            return mode
        else:
            print("Please select the correct operation")

def lives(difficulty):
    if difficulty == 'easy':
        attempt = 10
        return attempt 
    elif difficulty == 'hard':
        attempt = 5
        return attempt


def user_guess():
    guessed_number = int(input("Make a guess: "))
    return guessed_number



random_number = choosen_number()
difficulty = mode_of_game()
attempts = lives(difficulty)
game_over = False


while not game_over:
    user_guess_number = user_guess()

    if user_guess_number > random_number:
        attempts -= 1
        print("Too High\nGuess again.")
        print(f"You have {attempts} attempts remaining to guess the number")
        if attempts == 0:
           game_over = True
           print("You've run out of guesses,you lose") 
    elif user_guess_number < random_number:
        attempts -= 1
        print("Too Low\nGuess again.")
        print(f"You have {attempts} attempts remaining to guess the number")
        if attempts == 0:
           game_over = True
           print("You've run out of guesses,you lose") 
    else:
        game_over = True
        print("You Won")
