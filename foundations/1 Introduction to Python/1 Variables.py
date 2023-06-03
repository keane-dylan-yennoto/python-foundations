# Lesson 1: Python Syntax and Variables

""" Variables are used to store data values """

#   They act as containers that hold a specific piece of information, 
#   such as a number, a string of text, or a more complex data structure. 
#   We'll see more types of data types moving forward


""" Variable Declaration """

x = 5
# Here we have a variable named x and assign a value of 5

""" Variable Naming Rules """

#   The name must start with a letter (a-z, A-Z) or an underscore (_).
#   The name can contain letters, numbers, and underscores.
#   Python is case-sensitive, so myVariable and myvariable are considered different variables.

first_name = "Jane"
last_name = "Doe"
_age = 21

print(f"First Name: {first_name}")
print(f"last_name: {last_name}")
print(f"Age: {_age}")


# Comment / fix the code below to be able to run

1st_kids_name = "John" 
# we can see that using a number in the front is invalid and thus the code is unable to run

1st_rank_in_hackathon = "Austin" 
# using a number as the first letter of a variable name is invalid
# The error shown should be a SyntaxError

# Another Invalid Example
-x = 1