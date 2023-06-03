# Lesson 10: Dictionaries

# Creating a dictionary
# Dictionaries are key-element pairs

"""
    dictionary1 = {key1: value1, 
                   key2: value2}
"""

student = {
    "name": "John",
    "age": 20,
    "major": "Computer Science"
}

# "name" is a key and its value is "John"

# Accessing dictionary elements
print(student["name"])  # Output: "John"
print(student["age"])  # Output: 20
print(student["major"])  # Output: "Computer Science"

# Modifying dictionary elements
student["age"] = 21
print(student)  # Output: {'name': 'John', 'age': 21, 'major': 'Computer Science'}

# Adding elements to a dictionary
student["university"] = "ABC University"
print(student)  # Output: {'name': 'John', 'age': 21, 'major': 'Computer Science', 'university': 'ABC University'}

# Removing elements from a dictionary
del student["major"]
print(student)  # Output: {'name': 'John', 'age': 21, 'university': 'ABC University'}
