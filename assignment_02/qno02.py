 #Write a program to accept 5 digit number and check whether it is a numeric palindrome. (if reversed
#number is same as entered number it is called as palindrome)
num = int(input("Enter a 5-digit number: "))

original = num
reverse = 0
if num > 99999:
    print("Please enter a valid 5-digit number")
else:
    while num > 0:
        digit = num % 10
        reverse = reverse * 10 + digit
        num = num /10

    if original == reverse:
        print("The number is a Palindrome")
    else:
        print("The number is not a Palindrome")
