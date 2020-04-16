'''age = 15

if age <= 4:
    print("You get a free ticket")
elif age <= 18:
    print("Your ticket price is $25")
else:
    print("Your ticket price is $40")
-------------------------------------
age = input('Enter the age \n')
age = int(age)

if age <= 4:
    price = 0
elif age <= 18:
    price = 25
else:
    price = 40
print(f'your ticket price is ${price}')
----------------------------------------'''
age = 41

if age <= 4:
    price = 0
elif age <= 18:
    price = 25
elif age >= 65:
    price = 20
else:
    price = 40
print(f'your ticket price is ${price}')







