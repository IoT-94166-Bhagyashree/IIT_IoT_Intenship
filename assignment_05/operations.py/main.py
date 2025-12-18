from operations import arithmetic, string_ops

# Arithmetic operations
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

print("Addition:", arithmetic.add(a, b))
print("Multiplication:", arithmetic.multiply(a, b))

# String operations
text = input("Enter a string: ")

print("Reversed String:", string_ops.reverse_string(text))
print("Number of Vowels:", string_ops.count_vowels(text))
