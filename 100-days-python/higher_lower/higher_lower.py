import dataset as d
import random

data = d.dataset


def random_choice():
    return random.choice(data)


first_choice = random_choice()
second_choice = random_choice()

score = 0
game_over = False


while not game_over:

    f_data = (
        first_choice['name'],
        first_choice['description'],
        first_choice['country']
    )

    s_data = (
        second_choice['name'],
        second_choice['description'],
        second_choice['country']
    )

    count1 = first_choice['follower_count']
    count2 = second_choice['follower_count']

    print(f"\nCompare A: {f_data}")
    print(f"Against B: {s_data}")

    user = input("Who has more followers? Type 'A' or 'B': ").upper()

    if user == "A" and count1 > count2:

        score += 1
        print(f"You're right! Current score: {score}")

        second_choice = random_choice()

    elif user == "B" and count2 > count1:

        score += 1
        print(f"You're right! Current score: {score}")

        first_choice = second_choice
        second_choice = random_choice()

    else:

        game_over = True
        print(f"Wrong answer. Final score: {score}")