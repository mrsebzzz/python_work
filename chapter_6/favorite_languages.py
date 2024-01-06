# Dictionary of similiar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

print(favorite_languages)

language = favorite_languages['sarah'].title()
print(f"Sarah's favorite language is {language}.")

for name, language in favorite_languages.items():
    print(f"\nName: {name}")
    print(f"Favorite language: {language}")

for name,language in favorite_languages.items():
    print(f"\n{name.title()}'s favorite language is {language.upper()}")


for name in favorite_languages.keys():
    print(name.title())

# Looping through all keys in a dictionary

friends = ['phil', 'sarah']
for name in favorite_languages.keys():
    print(f"Hi {name.title()}!")

    if name in friends:
        language = favorite_languages[name].title()
        print(f"\t{name.title()}, I see you love {language}!")

# keys() method to find out if a particular person was polled

if 'erin' not in favorite_languages.keys():
    print("Erin, please take our poll!")

# sorting through dictionary in a sorted order
for name in sorted(favorite_languages.keys()):
    print(f"{name.title()}, thank you for taking the poll!")

# looping through all values in a dictionary
print("\n\nThe following langauges have been mentioned:")
for language in favorite_languages.values():
    print(language.title())

# a set is a collection in which each item must be unique
print("\n\nThe following langauges have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())