# Lesson 5: Conditional Statements (if, elif, else)

# Example: Checking if a number is positive, negative, or zero
num = 10
if num > 0:
    print(f"{num} is positive")
elif num < 0:
    print(f"{num} is negative")
else:
    print(f"{num} is zero")

# Example: Checking if a number is even or odd
num = 15
if num % 2 == 0:
    print(f"{num} is even")
else:
    print(f"{num} is odd")

# Example: Checking if a person is eligible to vote
age = 18
if age >= 18:
    print("You are eligible to vote!")
else:
    print("You are not eligible to vote.")


# Hierarchy of If, Elif, Else
'''
    The hierarchy of If, Elif, Else is:
        If -> Elif -> Else
    
    We can visualize this as a Tree

    Lets say:
    
        x is some integer value

        and the code is like this

        if x == 1:
            print("a")
        
        elif x == 2:
            print("b")

        ...
        ...
        ...

        elif x == 26:
            print("z")

        elif x == 27:
            print("aa")
        
        ...

        else:
            print("zzz")

        
        We can visualize this code as a tree, when a condition is True we go left and when it is False we go Right

        
            x == 1 (if)
            /   \
          "a"    \
                 x == 2 (elif)
                 /   \
                "b"   ...
                        \
                        ...
                          \ (else)
                          "zzz"
                    
         So when the part of ( if x == 1 ) is True, x's value is 1, we don't check for the rest and stop to that part of the code.
         Similary when ( elif x == 10 ) is True, x's value is 10, we only check from x == 1 to x == 9 and stop at that part.

         
        Howeverm when there is multiple ifs, we can see it as having multiple trees.
        Lets say 
         y is some integer number 
        and the code is:

        if y == 1:
            print("a")
        elif y == 2:
            print("b")

        if y > 1:
            print("c")
        elif y < 1:
            print("d")

        For every 'if' there is a new tree. Thus the tree will look like this.

            y == 1
             /   \
            "a"   \
                y == 2
                 /  \
               "b"   \
                     print nothing

            y > 1
            /   \
           "c"   \
                y < 1
                /   \
              "d"    \
                    print nothing

        Essentially, whenever there is a new 'if' it will create a new tree seperate from others 
         and the branches below are the codes of elifs and else.
            

        





        




'''
