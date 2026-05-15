import os
print("Welcome to the secret auction progress")
bidders = {}
more_bidders = False


while not more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What's your bid?: $"))
    
    if name in bidders:
        bidders[name].append(bid)
    else:
        bidders[name] = bid

    others = input("Are there any other bidders? Type 'yes' or 'no'. ")
    
    if others == "no":
        more_bidders = True
        
        highest = 0
        winner = ""
        for c_name,bid_value in bidders.items():
            if bid_value > highest:
                highest = bid_value
                winner = c_name
        print(f"The winner is {winner} with the bid of {highest}")
        
    else:
        os.system('clear')
    

        

