# Prog05: Create a program that ask user to input 2 numbers. Print the remainder when the first number is divided by the second number.
 
first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

try:
    remainder = first_number % second_number
    print(f"If we divide {first_number} by {second_number}, the remainder is {remainder}.")
except ZeroDivisionError:
    print("You cannot divide by zero.")