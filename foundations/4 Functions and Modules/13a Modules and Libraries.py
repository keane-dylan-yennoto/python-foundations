# Lesson 13a: Modules and Libraries

# Example 1: Using a built-in module math
import math

# Calculate the square root of a number
number = float(input("Enter a number: "))
result = math.sqrt(number)
print(f"The square root of {number} is: {result}")



# Example 2: Using the datetime module
import datetime

# Get the current date and time
current_datetime = datetime.datetime.now()

# Format and display the current date and time
formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
print(f"Current date and time: {formatted_datetime}")



# Example 3: Using the random module
import random

# Generate a random number between 1 and 10
random_number = random.randint(1, 10)
print(f"Random number: {random_number}")


