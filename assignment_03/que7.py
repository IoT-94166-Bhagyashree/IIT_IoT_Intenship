# Arithmetic operation functions

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b


# calculate function that accepts another function
def calculate(operand1, operand2, operation):
    return operation(operand1, operand2)


# Testing the calculate function
print("Addition:", calculate(10, 5, add))
print("Subtraction:", calculate(10, 5, subtract))
print("Multiplication:", calculate(10, 5, multiply))
print("Division:", calculate(10, 5, divide))

# Testing with different inputs
print("\nDifferent Test Cases:")
print("Addition:", calculate(25, 15, add))
print("Multiplication:", calculate(7, 6, multiply))
print("Division:", calculate(20, 0, divide))
