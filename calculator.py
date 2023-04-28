# calculator for 2 numbers

def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
def square(a):
    return a * a
def cube(a):
    return a * a * a 
def power(a, b):
    return a ** b

a = int(input("Enter a number: "))
b = int(input("Enter another number: "))

operator = input("Enter an operator: ")

# write switch case for operator

switcher = {
    "+": add(a, b),
    "-": subtract(a, b),
    "*": multiply(a, b),
    "/": divide(a, b),
    "square": square(a),
    "cube": cube(a),
    "power": power(a, b)
}

print(switcher.get(operator, "Invalid operator!"))

if operator == "+":
    print(add(a, b))
elif operator == "-":
    print(subtract(a, b))
elif operator == "*":
    print(multiply(a, b))
elif operator == "/":
    print(divide(a, b))
elif operator == "square":
    print(square(a))
elif operator == "cube":
    print(cube(a))
elif operator == "power":
    print(power(a, b))
else:
    print("Invalid operator!")