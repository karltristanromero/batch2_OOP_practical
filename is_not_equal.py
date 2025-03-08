# Prog02: Create a program that ask user to input 2 numbers. Print 'Not Equal' when the numbers are not the same.

first_number = float(input("Enter the first number: "))
second_number = float(input("Enter the second number: "))

if first_number != second_number:
    print(f"Numbers {first_number} and {second_number} are not equal.")