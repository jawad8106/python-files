"""Q)Personal Message: Use a variable to represent a person’s name, and print a message to that person.
 Your message should be simple, such as, “Hello Eric, would you like to learn some Python today?”

person_name = "Eric"
question = "would you like to learn some Python today?"
message = f'Hello {person_name} {question}'
print(message)"""




'''Q)Name Cases: Use a variable to represent a person’s name, and then print that person’s name 
in lowercase, uppercase, and title case.

name = "jawad ahmed"
print(name.lower())
print(name.upper())
print(name.title())'''



'''Q) Find a quote from a famous person you admire. Print the quote and the name of its author. 
Your output should look something like the following, including the quotation marks:

Albert Einstein once said, “A person who never made a mistake never tried anything new.”
famous_person = "allama iqbal"
famous_quote = "Tu shaheen hai, parvaaz hai kaam tera"
message = f'{famous_person.title()} once said, "{famous_quote}"'
print(message)'''







'''Q) Stripping Names: Use a variable to represent a person’s name, and include some 
whitespace characters at the beginning and end of the name. Make sure you use each 
character combination, "\t" and "\n", at least once.

name = "  '\tjawad \nahmed   ' "
print(name)
name = " '     \njawad ahmed "
print(name)
name = " ' \n\tjawad\n\tjaleel\n\tahmed ' "
print(name.title())'''


'''Print the name once, so the whitespace around the name is displayed. Then print the 
name using each of the three stripping functions, lstrip(), rstrip(), and strip().



name = "  'jawad ahmed   ' "
name = name.rstrip()
print(name)
name = " '     jawad ahmed' "
print(name.lstrip())
name = " ' jawad jaleel ahmed ' "
print(name.title().rstrip())'''



