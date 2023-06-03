# Lesson 7: While Loops

# Example 1: Print numbers from 1 to 5
print("Example 1:")
num = 1
while num <= 5:
    print(num)
    num += 1

# Example 2: Calculate the factorial of a number
print("Example 2:")
num = 5
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(f"The factorial of 5 is: {factorial}")

# Example 3: Sum numbers until a condition is met
print("Example 3:")
num = 1
sum = 0
while sum < 10:
    sum += num
    num += 1
print(f"The sum of numbers until the sum is greater than 10 is: {sum}")
