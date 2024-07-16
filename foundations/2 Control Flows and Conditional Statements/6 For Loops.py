# Lesson 6: For Loops

# Example 1: Print numbers from 1 to 5

# range(start, stop, step), stop is inclusive
print("Example 1:")
for num in range(1, 6):
    print(num)

# Example with a step
print("Example with a step:")
for num in range(1, 11, 2):
    print(num)

print()
    
# Iterate over a sequence of numbers using the range() function
# range(start, stop, step) generates a sequence of numbers from 'start' to 'stop-1' (inclusive), with a step size of 'step'
# In this case:
# - range(1, 6) generates the sequence 1, 2, 3, 4, 5
# - range(1, 11, 2) generates the sequence 1, 3, 5, 7, 9

# Example 2: Iterate over a list
print("Example 2:")
fruits = ["apple", "banana", "cherry"] 
# We will explore Python lists on the next chapter.
# For now, you can think of a list as a versatile container holding a collection of items

for fruit in fruits:
    print(fruit)
print()

# Example 3: Find the sum of all numbers from 1 to 10
print("Example 3:")
sum = 0
for num in range(1, 11):
    sum += num # this is equal to sum = sum + num
    
print(f"The sum of numbers from 1 to 10 is: {sum}")
print()

# Example 4: Print characters of a string
print("Example 4:")
message = "Hello, World!"
for char in message:
    print(char)
print()

# Example 5: For Loops in For Loops
for i in range(1, 6):
    for j in range(1, 4):
        print(f"{i} x {j} = {i*j}")
    print()