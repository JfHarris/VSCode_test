from click import prompt

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
    city = input(prompt)
    if city == 'quit':
        break
    else:
        print("I'd love to go to " + city.title() + "!")

# Please enter the name of a city you have visited:
# (Enter 'quit' when you are finished.) Tel Aviv
# I'd love to go to Tel Aviv!

# Please enter the name of a city you have visited:
# (Enter 'quit' when you are finished.) quit
