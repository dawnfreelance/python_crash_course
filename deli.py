# make a list called sandwich_orders and fill with names of sandwiches
sandwich_orders = ['BLT', 'Turkey club', 'Tuna', 'Ruben']

# make a emtpy list called fisnished_sandwiches where the orders will go
finished_sandwiches = []

while sandwich_orders:
    orders = sandwich_orders.pop()

    print(f"I just made a {orders}")
    finished_sandwiches.append(orders)

# print off the orders
print("\nHere are the sandwich Orders:")
for sandwich in finished_sandwiches:
    print(f"{sandwich}")
