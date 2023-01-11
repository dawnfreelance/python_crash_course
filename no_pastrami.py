# make a list called sandwich_orders and fill with names of sandwiches
sandwich_orders = ['BLT', 'Pastrami', 'Turkey club', 'Pastrami', 'Tuna', 'Ruben','Pastrami']

# make a emtpy list called fisnished_sandwiches where the orders will go
finished_sandwiches = []

# print a message letting the user know we have run out of pastrami
print("Sorry, we have run out of pastrami for thoese who have ordered it.")
print("\nMaking our orders now!")

while 'Pastrami' in sandwich_orders:
    sandwich_orders.remove('Pastrami')

while sandwich_orders:
    orders = sandwich_orders.pop()

    print(f"I just made a {orders}! order up!")
    finished_sandwiches.append(orders)

# print off the orders
print("\nHere are the sandwich Orders:")
for sandwich in finished_sandwiches:
    print(f"{sandwich}")
