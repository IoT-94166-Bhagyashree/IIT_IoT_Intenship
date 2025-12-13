#Write a Python program to accept two numbers and display the results of addition, subtraction, 
#multiplication, and division.
num1 = float (input("enter first number:"))
num2 = float(input("enter second number:"))
print("enter your choice")
print("1.addition :")
print("2.substraction :")
print("3.multiplication :")
print("4.division :")
choice = int (input("enter your choice:"))
match choice :
    case 1 :
          print( f"the addition of num1 and num2 {num1 + num2}" )

    case 2 :
           print( f"the substraction of num1 and num2 {num1 - num2}" )

    case 3 :
             print( f"the multiplication of num1 and num2 {num1 * num2}" )

    case 4 :          
            print( f"the division of num1 and num2 {num1 / num2}" )

    case _ :
              print("invalid option")
