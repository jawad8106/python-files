'''alien_colors = ['yellow', 'red']

if 'green' in alien_colors:
    print("You have just earned 5 points for shooting an alien")
elif 'yellow' in alien_colors:
    print("You have earned 10 points")
elif 'red' in alien_colors:
    print("You have earned 15 points")
else:
    print("player earned no points")

age = 64

if age < 2:
    print("this is a baby")
elif age < 4:
    print("this is toddler")
elif age < 13:
    print("this person is a kid")
elif age < 20:
    print("This person is an adult")
elif age < 65:
    print("this person is an elder")
else:
    print("you are an adult")

favourite_fruits = ['mango', 'apple', 'banana']

if 'mango' in favourite_fruits:
    print("you really like mango")
if 'apple' in favourite_fruits:
    print("you really like apple")
if 'banana' in favourite_fruits:
    print("you really like banana")
if 'kiwi' in favourite_fruits:
    print("you really like kiwi")
if 'orange' in favourite_fruits:
    print("you really like orange")

names = ['admin', 'jaw', 'soh', 'abd', 'adn']
for name in names:
    if 'pan' in names:
        print("Hello admin, would you like to see a status report?")
    else:
        print("Hello jade, thank you for logging in again")

current_users = ['aa', 'ba', 'ca', 'da', 'ea']
new_users = ['aa', 'ba', 'xa', 'ya', 'za']

for new in new_users:

    if new in current_users:
        print('You will need to enter a new username')
    else:
        print("username is available.")



current_users = ['aa', 'ba', 'ca', 'da', 'ea']
new_users = ['aa', 'ba', 'xa', 'ya', 'za']

#current_users_lower = [user.lower() for user in current_users]


for new_user in new_users:

    if new_user in current_users:
        print(new_user, "You will need to enter a new username")
    else:
        print(new_user, "username is available.")


numbers = list(range(1, 100))

for number in numbers:
    if number == 1:
        print("1st")
    elif number == 2:
        print("2nd")
    elif number == 3:
        print("3rd")
    else:
        print(str(number) + "th")'''











