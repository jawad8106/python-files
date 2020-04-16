'''message = input("Tell me something, and I will repeat it back to you: ")
print(message)

name = input("Please enter your name: ")
print(f"\nHello, {name}!")


prompt = "If you tell us who you are, we can personalize the messages you see."
prompt += "\nWhat is your first name?"

name = input(prompt)
print(f"\nHello, {name}!")




height = input("How tall are you. in inches?")
height = int(height)

if height >= 48:
    print(f'\n You are tall enough to ride')
else:
    print(f'\nYou will be able to ride when you are a little older.')

cars = input("what kind of rental car you would like: ")
print(f"\nLet me see if I can find you a {cars}")



people = input("How many people are their in dinner group? - ")
people = int(people)

if people > 8:
    print("sorry, you have to wait for a table")
else:
    print(f'\nWelcome, your table is ready!')'''


number = input("Enter a number, and I'll tell you if it's a multiple of ten or not: ")
number = int(number)

if number % 10 == 0:
    print(f"\nThe number {number} is a multiple of ten.")
else:
    print(f"\nThe number {number} is not a multiple of ten.")


