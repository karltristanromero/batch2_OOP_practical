# Prog06: Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.

print("Enter 10 numbers\n")

difference = 0

for i in range(10):
    num = float(input(f"Enter number ({i+1}): "))
    if i == 0:
        difference += num
    else:
        difference -= num

print(f"The difference is: {difference}")
