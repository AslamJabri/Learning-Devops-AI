import random 

words = ["macbook","windows"]

chosen_word = random.choice(words)
lives = 6
correct_guesses = []
game_over = False
while not game_over:
    guess = input("Guess a letter: ")
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_guesses.append(letter)
            
        elif letter in correct_guesses:
            display += letter
        else:
            display += "_"
    print(display)
    if guess not in correct_guesses:
        lives -= 1
        print(f"########{lives}/6######")
        if lives ==0:
            game_over = True
            print("You lose")

    if "_" not in display:
        print("You won")
        game_over = True


