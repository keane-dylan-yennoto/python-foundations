
index_to_price = {
    1:12,
    2:34,
    3:5,
    4:3,
    5:3
}

index_to_name = {
    1:'Cheese Burger',
    2:'Steak',
    3:'Sandwich',
    4:'Coke',
    5:'Ice Tea'
}

print('=========================')
print('Welcome to my Restaurant')
print('Our menu:')


for key in index_to_price:
    print(f"{key}. {index_to_name[key]} ${index_to_price[key]}")

print(f'{len(index_to_price) + 1}. stop')

index_to_customer_order = {
    1:0,
    2:0,
    3:0,
    4:0,
    5:0
}

while True:
    order_index = int(input("What's ur order :"))

    if order_index == len(index_to_price) + 1:
        break

    index_to_customer_order[order_index] = index_to_customer_order[order_index] + 1

total_price = 0

for key in index_to_customer_order:
    total_price = total_price + index_to_customer_order[key] * index_to_price[key]

print('=========================')
print('Here is your bill: ')
for key in index_to_name:
    if index_to_customer_order[key] > 0:
        print(f'{index_to_name[key]} {index_to_customer_order[key]} x ${index_to_price[key]} = ${index_to_customer_order[key] * index_to_price[key]}')



print(f'Total Price: {total_price}')
print('=========================')
