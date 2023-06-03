# Lesson 12: File Handling

# Example 1: Writing to a file
filename = "data.txt"

# Open the file in write mode
file = open(filename, "w")

# Write multiple lines to the file
file.write("Line 1\n")
file.write("Line 2\n")
file.write("Line 3\n")

# Close the file
file.close()

print(f"Data written to '{filename}' successfully.")

# Example 2: Appending to a file
file = open(filename, "a")

# Append additional lines to the file
file.write("Line 4\n")
file.write("Line 5\n")

# Close the file
file.close()

print(f"Additional data appended to '{filename}'.")

# Example 3: Reading from a file
file = open(filename, "r")

# Read and print the contents of the file
contents = file.read()
print("File Contents:")
print(contents)

# Close the file
file.close()
