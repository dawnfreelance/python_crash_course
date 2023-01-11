# make an emtpy list to store the pizza toppings
pizza_toppings = []

# make a loop that asks the user to enter their toppings
# print off the topping they entered
# if they enter quit, end the program

active = True

while active:
    topping = input("Please enter a topping, type 'quit' to end the program: ")
    if topping == 'quit':
        active = False
    else:
        pizza_toppings.append(topping)
        print(f"Adding {topping}...")