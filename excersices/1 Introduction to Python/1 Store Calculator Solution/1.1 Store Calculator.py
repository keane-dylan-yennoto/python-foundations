""" Exercise 1.1: Store Calculator """

''' 
Write a program that acts as a simple store calculator. 

The program should take the item name, price, quantity, and discount percentage of an item from the user 

You will need to calculate the total price and the total price after applying the discount. 
Both prices should be printed to the nearest second decimal place 

See the problem output in the '1.1 Store Calculator Challenge.txt'
'''

# Code Here

print("=== Store Calculator ===")
item_name = input("Enter the item name: ")
item_price = float(input("Enter the item price: "))
item_quantity = int(input("Enter the item quantity: "))
item_discount = float(input("Enter the discount percentage: "))
print()

total_price = item_quantity * item_price
discount_total_price = (1-item_discount) * total_price

print("=== Receipt ===")
print(f"Item: {item_name}")
print(f"Price per item: ${item_price}")
print(f"Quantity: {item_quantity}")
print(f"Total price: ${total_price}")
print(f"Total price after discount: ${discount_total_price}")
