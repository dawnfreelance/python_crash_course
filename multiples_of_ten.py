# ask the user for a number to see if it is a multiple of 10
message = input("Please enter a number and i will tell you if it is a multiple of 10: ")
message = int(message)
# check to see if the number is a multiple of 10
# by getting the remainder of dividing the number by 10
# if it is a multiple, the remainder will be 0 
# and if it is not, the remainder will not be 0
# print a message for each senario

if message % 10 == 0:
    print(f"Your number {message} is a multiple of 10")
else:
    print(f"Your number {message} is not a multiple of 10")