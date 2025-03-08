# Prog07: Create a program that ask user to input 10 numbers. Print how many are even numbers.

print("Enter 10 numbers\n")

even = 0

for i in range(10):
    num = float(input(f"Enter number ({i+1}): "))
    if num % 2 == 0:
        even += 1

print(f"There are {even} even numbers.")