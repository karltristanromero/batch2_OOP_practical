# Prog10: Create a program that ask user to input 2 numbers. Print all the numbers between the two numbers.

lb = int(input("Enter lower boundary of range: "))
ub = int(input("Enter upper boundary of range: "))

for i in range(lb + 1, ub):
    print(i, end= " ")