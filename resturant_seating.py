# ask the user how many people are in the dinner party
message = input("How many people will be eating tonight?")
message = int(message)

# if the dinner party is more than eight, let the user know that
# they will have to wait, if its less, let them know a table is ready

if message >= 8:
    print("Sorry, but you will have to wait for a table.")
else:
    print("Please follow me this way to your table...")
