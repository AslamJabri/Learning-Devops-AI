first_number = float(input("What's the first number?: "))
print("+","-","*","/")
calculation = input("Pick an operation: ")
second_number = float(input("What's the next number?: "))

def addition(num1,num2):
    return num1+num2
def subtraction(num1,num2):
    return num1-num2
def multiplication(num1,num2):
    return num1*num2
def division(num1,num2):
    return num1/num2

def operation(operator):
    if operator == "+":
        return addition(first_number,second_number)
    elif operator == "-":
        return subtraction(first_number,second_number)
    elif operator == "*":
        return multiplication(first_number,second_number)
    elif operator == "/":
        return division(first_number,second_number)
    else:
        return ("Select the correct operation")

result = operation(calculation)
    
print(f"{first_number} {calculation} {second_number} = {result}")


calculate_more = False

while not calculate_more:
    user_decision = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation or 'exit' to finish: ")
    
    if user_decision == "y":
        first_number = result
        print("+","-","*","/")
        calculation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        result = operation(calculation)
    elif user_decision == "n":
        first_number = float(input("What's the first number?: "))
        print("+","-","*","/")
        calculation = input("Pick an operation: ")
        second_number = float(input("What's the next number?: "))
        result = operation(calculation)
    elif user_decision == "exit":
        calculate_more = True
        print("Thank You!")
    else:
        print("Please use a proper instructions")