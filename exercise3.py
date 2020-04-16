'''guest = ['amir', 'shahrukh', 'salman']
message = "come to the party"
invitation = f'{message} {guest[0]}'
print(invitation)
invitation = f'{message} {guest[1]}'
print(invitation)
invitation = f'{message} {guest[2]}'
print(invitation)
missing_guest = f' we came to know that {guest[2]} will not be able to make it to the party'
print(missing_guest)

guest = ['amir', 'shahrukh', 'salman']
print(guest)
guest[2] = 'saif'
print(guest)'''

guest = ['amir', 'shahrukh', 'saif']
message = "come to the party"
invitation = f'{message} {guest[0]}'
print(invitation)
invitation = f'{message} {guest[1]}'
print(invitation)
invitation = f'{message} {guest[2]}'
print(invitation)
guest.insert(0, 'amitabh')
print(guest)
guest.insert(2, 'kajol')
print(guest)
guest.append('aishwarya')
print(guest)
invitation = f'{message} {guest[0]}'
print(invitation)
invitation = f'{message} {guest[1]}'
print(invitation)
invitation = f'{message} {guest[2]}'
print(invitation)
invitation = f'{message} {guest[3]}'
print(invitation)
invitation = f'{message} {guest[4]}'
print(invitation)
print("Dinner table will not be arriving on time, have two spaces left only")
out_of_list = guest.pop(0)
print(f'{out_of_list.title()},I am sorry I cannot invite you to dinner.')
out_of_list = guest.pop(2)
print(f'{out_of_list.title()},I am sorry I cannot invite you to dinner.')
print(guest)
out_of_list = guest.pop(3)
print(f'{out_of_list.title()},I am sorry I cannot invite you to dinner.')
out_of_list = guest.pop(2)
print(f'{out_of_list.title()},I am sorry I cannot invite you to dinner.')
print(guest)
message = "I want to let you know that you are still invited to the dinner,"
invitation = f'{message} {guest[0]}'
print(invitation)
invitation = f'{message} {guest[1]}'
print(invitation)
del guest[1]
print(guest)
del guest[0]
print(guest)



