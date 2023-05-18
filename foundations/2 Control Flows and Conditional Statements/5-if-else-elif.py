# Lesson 5: Conditional Statements (if, elif, else)

# Example: Checking if a number is positive, negative, or zero
num = 10
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")

# Example: Checking if a number is even or odd
num = 15
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# Example: Checking if a person is eligible to vote
age = 18
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote.")
