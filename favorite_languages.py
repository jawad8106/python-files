'''favourite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'ruby',
    'phil': 'python',
}

language = favourite_languages['sarah'].title()
print(f'sarah favourite language is {language}')


information = {
    'name': 'ziad',
    'last': 'ahmed',
    'age': '27',
    'city': 'london',
}

print(information)'

favourite_numbers = {
    'adam': '1',
    'noah': '2',
    'abraham': '3',
    'moses': '4',
    'jesus': '5',
}

favourite_number = favourite_numbers['adam'].title()
print(f'adam favourite number is {favourite_number}')'''


favorite_languages = {
       'jen': ['python', 'ruby'],
       'sarah': ['c'],
       'edward': ['ruby', 'go'],
       'phil': ['python', 'haskell'],
       }
for name, languages in favorite_languages.items():
    print(f'\n{name.title()} favourite languages are:')
    for language in languages:
        print(f'\n\t{language.title()}')








