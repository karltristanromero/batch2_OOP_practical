# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

print(f"{first_number if first_number < second_number else second_number} is smaller.")