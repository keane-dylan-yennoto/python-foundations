"""

Exercise 3.1: Word Frequency Counter

Write a Python program that takes a paragraph of text as input from the user 
and counts the frequency of each word in the paragraph.

The program will display a list of unique words along with their corresponding frequencies.

Example :

=== Word Counter ===
Enter a text: Hello world. Hello Python. Python is great!

Word Frequency:
- hello: 2
- world: 1
- python: 2
- is: 1
- great: 1

"""


print("=== Word Counter ===")
paragraph = input("Enter a text: ")

char_list = []

for char in paragraph:
    if char.isalpha() or char == ' ':
        char_list.append(char)

paragraph = ''.join(char_list).lower()

words = paragraph.split()

result = {}

for word in words:
    if word in result:
        result[word] = result[word] + 1
    else:
        result[word] = 1

print()
print("Word Frequency:")
for word in result:
    print(f"- {word}: {result[word]}")