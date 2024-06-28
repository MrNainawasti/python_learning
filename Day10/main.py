# calculator
from replit import clear 

from art import logo


# addition
def add(n1, n2):
    return n1 + n2

# subtraction
def sub(n1, n2):
    return n1 - n2

# multlipication
def mul(n1, n2):
    return n1 * n2

# division
def div(n1, n2):
    return n1 / n2
    
operations = {
    "+": add,
    "-": sub,
    "*": mul,
    "/": div
}
def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    exit = False
    while not exit:
        for key in operations:
            print(key)
        op = input("pick an operation: ")
        num2 = float(input("What's the next number?: "))
        execute = operations[op]
        answer = execute(num1, num2)
        print(f"\n{num1} {op} {num2} = {answer}")
        print("_______________________________")
        check = input(f'''type 'y' to continue calculating with {answer},
or type 'n' to start a new calculation: ''')
        if check == "n":
            exit = True
            clear()
            calculator()
        elif check =="y":
            num1 = answer
calculator()

    
    

