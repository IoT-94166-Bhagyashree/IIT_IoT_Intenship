#Write a Python program to accept two numbers from the user and swap their values.

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

# Display values before swapping
print("Before swapping: num1 = {}, num2 = {}".format(num1, num2))

# Swapping using a temporary variable
temp = num1
num1 = num2
num2 = temp

# Display values after swapping
print("After swapping: num1 = {}, num2 = {}".format(num1, num2))
