# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

try:
    quotient = first_number / second_number
    print(f"The quotient of the numbers is {int(quotient)}.")
except ZeroDivisionError:
    print("You cannot divide by zero!")