# Write a function to print given number of terms of Fibonacci series
def fibonacci(n):
    a, b = 0, 1
    print("Fibonacci Series:")
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b
n = int(input("Enter number of terms: "))

if n <= 0:
    print("Please enter a positive number")
else:
    fibonacci(n)

