import random

print("Welcome to the PyPassword Generator")
letters= ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

choosing_password = []
letter_count = int(input("How many letters would you like in your password?\n"))
symbol_count = int(input("How many symbols would you like in your password?\n"))
number_count = int(input("How many numbers would you like in your password?\n"))



for _ in range(0,letter_count):
    choosing_password.append(random.choice(letters))
for _ in range(0,symbol_count):
    choosing_password.append(random.choice(symbols))
for _ in range(0,number_count):
    choosing_password.append(random.choice(numbers))
random.shuffle(choosing_password)
password = "".join(choosing_password)

print(f"Your password is: {password}")