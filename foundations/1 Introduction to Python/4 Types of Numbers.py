# Lesson 4: Types of Numbers in Python

print("Integers, Floats, & Complex #s")

# Integer
num1 = 10
print("Integer:", num1)
# Output: Integer: 10

# Float
num2 = 3.14
print("Float:", num2)
# Output: Float: 3.14

# Complex
num3 = 2 + 3j
print("Complex:", num3)
# Output: Complex: (2+3j)
print()

print("Type Conversion")


# Type conversion
x = 5
y = 2.5
print('x: ',x)
print('y: ',y)

# Integer to float
result1 = float(x)
print("x Integer to float:", result1)
# Output: Integer to float: 5.0

# Float to integer
result2 = int(y)
print("y Float to integer:", result2)
# Output: Float to integer: 2
print()

print("Basic Operations")
# Operations
a = 10
b = 3
print('a: ',a)
print('b: ',b)


# Addition
sum = a + b
print("Sum:", sum)
# Output: Sum: 13

# Subtraction
diff = a - b
print("Difference:", diff)
# Output: Difference: 7

# Multiplication
product = a * b
print("Product:", product)
# Output: Product: 30

# Division
quotient = a / b
print("Quotient:", quotient)
# Output: Quotient: 3.3333333333333335
# Computers represent floating-point numbers like 10/3 using binary format, (ones and zeroes 100111001111010100)
# which can only approximate some decimal values, leading to small rounding errors in the result.

# Modulo
remainder = a % b
print("Remainder:", remainder)
# Output: Remainder: 1

# Exponentiation
power = a ** b
print("Power:", power)
# Output: Power: 1000