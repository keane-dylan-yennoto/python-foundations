# Lesson 9: Tuples

# Creating a tuple
person = ("John", 25, "New York")

# Accessing tuple elements
print(person[0])  # Output: "John"
print(person[1])  # Output: 25
print(person[2])  # Output: "New York"

# Modifying a tuple (not possible)
# person[1] = 30  # Raises an error

# Unpacking a tuple
name, age, city = person
print(name)  # Output: "John"
print(age)  # Output: 25
print(city)  # Output: "New York"
