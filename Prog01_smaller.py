# Prog01: Create a program that ask user to input 2 numbers. Print the smaller number.

x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

print(f"{x if x < y else y} is smaller.")