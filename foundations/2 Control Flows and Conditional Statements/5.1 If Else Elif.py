x = input("Please enter your x value: ")

# Example 1
if x == 1:
    print("a")
elif x == 2:
    print("b")
elif x == 3:
    print("c")
elif x == 4:
    print("d")
elif x == 5:
    print("e")
elif x == 6:
    print("f")
elif x == 7:
    print("g")
else:
    print("zzz")

# Example 2
y = input("Please enter your y value: ")

if y == 1:
    print("a")
elif y == 2:
    print("b")
if y > 1: # Notice that this is another "if", therefore another tree exists
    print("c")
elif y < 1:
    print("d")

