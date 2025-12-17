def print_binary(num):
    if num < 0:
        print("Binary representation is not supported for negative numbers.")
    else:
        print(bin(num)[2:])
print_binary(10)

