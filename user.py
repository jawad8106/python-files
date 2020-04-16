'''user_0 = {
    'username': 'efermi',
    'first': 'enrico',
    'last': 'fermi',
}
for key, value in user_0.items():
    print(f"\nKey: {key}")
    print(f"Value: {value}")

user_0 = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}
for key, value in user_0.items():
    print(f"\nkey: {key}")
    print(f"value: {value}")




favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }

for name, language in favorite_languages.items():
    print(f'{name.title()}s favorite language is {language.title()}')



favorite_languages = {
       'jen': 'python',
       'sarah': 'c',
       'edward': 'ruby',
       'phil': 'python',
       }
friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}.")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")



favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")



favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

for name in sorted(favorite_languages.keys()):
    print(f'{name.title()}, thank you for taking the poll.')



favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title())


favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
    }
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
       print(language.title())



rivers = {
    'nile': 'egypt',
    'ganga': 'india',
    'missisippi': 'usa',
    }
for name in rivers.keys():
    print(name.title())
    value = rivers[name].title()
    print(f'The {name.title()} river runs through {value}.')'''



rivers = {
    'nile': 'egypt',
    'ganga': 'india',
    'missisippi': 'usa',
    }
for name in rivers.keys():
    print(name.title())
print("..............")
for country in rivers.values():
    print(country.title())







