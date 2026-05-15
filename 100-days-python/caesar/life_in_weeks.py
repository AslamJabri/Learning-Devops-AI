max_age = 90

user_age = int(input("What is your age? "))

def life_in_weeks(user_age):
    age = max_age - user_age
    weeks = age * 52
    
    print(f"You have {weeks} weeks left.")
    
life_in_weeks(user_age)