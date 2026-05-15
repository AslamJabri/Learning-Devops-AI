alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]


again = False
def encode(message,shift):
    cipher = []

    for letter in message:
        if letter in alphabets:
            current_index = alphabets.index(letter)
            new_index = (current_index + shift) %26
            cipher.append(alphabets[new_index])
        else:
            cipher.append(letter)
    password = "".join(cipher)
    print(f"Your encoded message: {password}")

def decode(message,shift):
    cipher = []

    for letter in message:
        if letter in alphabets:
            current_index = alphabets.index(letter)
            new_index = (current_index - shift)%26
            cipher.append(alphabets[new_index])
        else:
            cipher.append(letter)
    password = "".join(cipher)
    print(f"Your decoded message: {password}")
    

while not again:
    type = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")

    message = input("Type your message:\n")
    shift = int(input("Type the shift number: \n"))


    if type == "encode":
        encode(message,shift)
    elif type == "decode":
        decode(message,shift)
    else:
        print("Please tell the proper function")
    try_again = input("Type 'yes' if you want to go again. Otherwise 'no'.")
    if try_again == "no":
        again = True
        print("GoodBye")
            

