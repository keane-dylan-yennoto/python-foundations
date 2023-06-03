# Lesson 11: Introduction to Functions

# Example 1: Simple function without parameters
def greet_user():
    """Greets the user."""
    print("Hello! Welcome to our program.")

# Call the function to greet the user
greet_user()

# Example 2: Function with parameters
def greet_person(name):
    """Greets a person with a personalized message."""
    print(f"Hello, {name}! Welcome to our program.")

# Prompt the user for their name
user_name = input("Enter your name: ")

# Call the function to greet the person
greet_person(user_name)

# Example 3: Function with a return value
def add_numbers(a, b):
    """Adds two numbers and returns the result."""
    return a + b

# Prompt the user for two numbers
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Call the function to add the numbers and store the result
result = add_numbers(num1, num2)

# Display the result
print(f"The sum of {num1} and {num2} is: {result}")
