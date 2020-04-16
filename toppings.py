'''requested_toppings = ['cheese', 'non-veg']

if 'cheese' in requested_toppings:
    print("adding cheese")
if 'veg' in requested_toppings:
    print("adding veg")
if 'non-veg' in requested_toppings:
    print("adding non-veg")

print("\nFinished making pizza")


requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
elif 'pepperoni' in requested_toppings:
    print("Adding veg.")
elif 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")




#requested_toppings = input('choose the toppings:\n')
requested_toppings = ['mushrooms', 'extra cheese']
#requested_toppings = str(requested_toppings)

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'veg' in requested_toppings:
    print("Adding veg.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")
else:
    print("toppings are not available")

print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:

    if requested_topping == 'green peppers':
        print("sorry, we ran out of green peppers")
    else:
        print(f"Adding {requested_topping}.")

print("\nFinished making your pizza!")



requested_toppings = []

if requested_toppings:
       for requested_topping in requested_toppings:
           print(f"Adding {requested_topping}.")
       print("\nFinished making your pizza!")
else:
       print("Are you sure you want a plain pizza?")'''

available_toppings = ['mushrooms', 'olives', 'green peppers',
                      'pepperoni', 'pineapple', 'extra cheese']
requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print(f"Adding {requested_topping.title()}")
    else:
        print(f'Sorry, we do not have {requested_topping.title()}')
print("\nFinished making your pizza!")