# make a message for each ticket price

under_three = "Your ticket is free!"

three_to_twelve = "your ticket is $10"

over_twelve = "your ticket is $15"

# ask the user how old they are
# make a loop and print off one of the above variables
# dpending on how old the user is



active =True

while active:
    message = input("Please enter your age: ")
    message = int(message)
    if message < 3:
        print(under_three)
    elif message >= 3 and message <= 12:
        print(three_to_twelve)
    else:
        print(over_twelve)
        
