
# Lesson 3: Inputs and Outputs

''' Taking User Input '''

# To take user input in Python, you can use the `input()` function. 
# It prompts the user to enter a value and returns the input as a string. 
# If you need the input to be treated as a different data type, such as an integer or float, you can use type casting to convert it.

# Let's see an example:

# Taking user input for name
name = input("Enter your name: ")

# Taking user input for age and converting it to an integer
age = int(input("Enter your age: "))


''' Printing Output ''' 

# To print output in Python, you can use the `print()` function. 
# It takes one or more arguments and displays them as output.

# Let's see an example:


# Printing output
print(f"Hello, {name}!") # here we use a feature called f-strings or formatted string literals
print(f"You are {age} years old.")
