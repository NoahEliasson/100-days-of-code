def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def divide(n1, n2):
    return n1 / n2
def multiply(n1, n2):
    return n1 * n2


operations = {
    "+": add,
    "-": subtract,
    "/": divide,
    "*": multiply
    }
def calculator():
    num1 = int(input("what is the first number: "))
    for symbol in operations:  
        print(symbol)
    operations_symbol = input("what is your symbol")
    calc_on = True
    while calc_on:
        num2 = int(input("what is the next number: "))
        calculation_function = operations[operations_symbol] # extract the value from the dict key which is a function. 
        answer = calculation_function(num1, num2)
        print(f"{num1} {operations_symbol} {num2} = {answer}")

        if input(f"Type 'y' to continue calculating with {answer} or type 'n' to quit") == "y":
            num1 = answer
        else:
            calc_on = False

calculator()