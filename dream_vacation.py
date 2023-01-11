# make an emtpy dictionay for storing the results
responses = {}

# make a flag to start the while loop to run the poll
active = True

# start the loop and askt the user questions
while active:
    name = input("\nWhat is your name? ")
    response = input("\nIf you could visit one place in the world, where would you go? ")

    # add the responses to the dictionary
    responses[name] = response

    # ask if they would like to go again

    repeat = input("Would you like to give someone else a turn? (yes/no) ")
    if repeat == 'no':
        active = False

# print out the responses
print("\nAlright here our the responses from the poll!:")
print("!-- Poll Responses --!")
for key, value in responses.items():
    print(f"{key.title()} would like to goto: {value.title()}")


