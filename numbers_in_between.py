# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

lower_boundary = (input("Enter lower boundary of range: "))
upper_boundary = int(input("Enter upper boundary of range: "))

for num in range(lower_boundary + 1, upper_boundary):
    print(num, end= " ")