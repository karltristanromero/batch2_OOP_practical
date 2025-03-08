# Prog04: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers without the decimal point

x = float(input("Enter dividend: "))
y = float(input("Enter divisor: "))

try:
    quotient = x / y
    print(f"The quotient of the numbers is {int(quotient)}.")
except ZeroDivisionError:
    print("You cannot divide by zero!")