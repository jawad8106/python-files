""" Names: Store the names of a few of your friends
in a list called names. Print each person’s name by
accessing each element in the list, one at a time.

Greetings: Start with the list you used in Exercise 3-1,
but instead of just printing each person’s name, print
a message to them. The text of each message should be
the same, but each message should be personalized with
the person’s name.
"""

friends = ['rachel', 'ross', 'monica', 'chandler', 'joey', 'phoebe']
print(friends[0:5])
print(friends[0])
print(friends[1])
print(friends[2])
print(friends[3])
print(friends[4])
print(friends[5])
message = f'You are the best "{friends[0].title()}"'
print(message)
message = f'You are the best "{friends[1].title()}"'
print(message)
message = f'You are the best "{friends[2].title()}"'
print(message)
message = f'You are the best "{friends[3].title()}"'
print(message)
message = f'You are the best "{friends[4].title()}"'
print(message)
message = f'You are the best "{friends[5].title()}"'
print(message)
