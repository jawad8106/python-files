'''prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
       city = input(prompt)

       if city == 'quit':
           break
       else:
           print(f"I'd love to go to {city.title()}!")

prompt = "Enter the name of pizza toppings:"

name = input(prompt)
print(f"\nwe will add {name} topping to your pizza")

prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.) "

while True:
       city = input(prompt)

       if city == 'quit':
           break
       else:
           print(f"I'd love to go to {city.title()}!")


prompt = "How old are you?"
prompt += "\nEnter 'quit' when you are finished. "

while True:
    age = input(prompt)
    if age == 'quit':
        break
    age = int(age)

    if age < 3:
        print("  You get in free!")
    elif age < 13:
        print("  Your ticket is $10.")
    else:
        print("  Your ticket is $15.")'''


prompt = "\nWhat topping would you like on your pizza?"
prompt += "\n\nEnter 'quit' when you are finished: "

while True:
    topping = input(prompt)
    if topping != 'quit':
        print("  I'll add " + topping + " to your pizza.")
    else:
        break