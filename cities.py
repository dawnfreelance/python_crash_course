prompt = "\nPlease enther the name of a city you have visited:"
prompt += "\n(Enter 'quit' when your finished.)"

while True:
    city = input(prompt)

    if city == 'quit':
        break

    else:
        print(f"I'd love to go to {city.title()}!")