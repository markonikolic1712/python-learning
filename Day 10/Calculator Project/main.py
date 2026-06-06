import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}




def calculator():
    print(art.logo)
    num = float(input("What is the first number?: "))
    choice = "y"
    result  = 0
    while choice == "y":
        for key, value in operations.items():
            print(f"{key}")
        operation = input("Pick an operation: ")
        next_num = float(input("What's the next number?: "))

        result = operations[operation](num, next_num)
        print(f"{num} {operation} {next_num} = {result}")
        choice = input(f"Type 'y' to continue calculating with {result}, or type 'n' to start a new calculation: ").lower()
        if choice == "y":
            num = result
        else:
            print("\n" * 25)
            calculator()

calculator()