"""
Excercise 2.1: Simple Calculator

Write a Python program that takes two numbers, a and b, and a simple mathematical symbol as input from the user.
However an additional twist is that this must be done forever till the user ask to stop. 

The program should perform the corresponding mathematical operations: 

    '+' for addition, 
    '-' for subtraction, 
    '*' for multiplication, 
    '/' for division

on the numbers a and b, and display the result.

See the problem output in the '2.1 Simple Calculator Challenge.txt'
"""

while True:
    print("=== Simple Calculator ===")
    a = input("Enter the first number: ")

    if a == 'stop':
        break
    a = float(a)

    b = float(input("Enter the second number: "))
    sym = (input("Enter the mathematical symbol (+, -, *, /): "))

    result = 0

    if sym == '+':
        result = a + b
    elif sym == '-':
        result = a - b
    elif sym == '*':
        result = a * b
    else:
        result = a / b
    
    print()
    print(f"Result: {result}")

print()
print("End Of Program")


    