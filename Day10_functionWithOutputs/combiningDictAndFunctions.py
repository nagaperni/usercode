#Calculator

#Add
def add(n1, n2):
    return n1 + n2

#Subtract
def subtract(n1, n2):
    return n1 - n2

#Multiply
def multiply(n1, n2):
    return n1 * n2

#Divide
def divide(n1, n2):
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
} 

num1 = int(input("Whats the first number?: "))
for operation in operations:
    print(operation)
operation_symbol = input("Pick an operation from the line above: ")
num2 = int(input("Whats the first number?: "))
calc_func = operations[operation_symbol]
answer = calc_func(num1, num2)

print(f"{num1} {operation_symbol} {num2} = {answer}")
