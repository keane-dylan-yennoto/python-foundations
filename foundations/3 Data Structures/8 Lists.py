# Lesson 8: Lists

# Creating a list
fruits = ["apple", "banana", "orange"]

# Accessing list elements
print(fruits[0])  # Output: "apple"
print(fruits[1])  # Output: "banana"
print(fruits[2])  # Output: "orange"

# Number of Elements in a List
print(len(fruits)) # Output: 3

# Modifying list elements
fruits[1] = "grape"
print(fruits)  # Output: ["apple", "grape", "orange"]

# Adding elements to a list
fruits.append("mango")
print(fruits)  # Output: ["apple", "grape", "orange", "mango"]

# Removing elements from a list
fruits.remove("apple")
print(fruits)  # Output: ["grape", "orange", "mango"]

'''

What we learned so far such as int, float, string, etc and also lists are data types or also called classes.
.remove(), .append() are called methods for the list class

Functions that can be applied to classes are called methods.
You can google other possible methods that can be applied to lists.

Personally, when I do programming I believe that all essential building blocks are available to us. 
Thus, you can imagine what could I do to a list?
Lets say remove item with on specific index. Google how to remove item on a specific index and see how to code it.


'''