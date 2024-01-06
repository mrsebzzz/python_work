rivers = {
    'nile': 'egypt',
    'new river': 'north america',
    'ganges': 'africa',
    'colorado': 'north america',
}

for river, country in rivers.items():
    print(f"The {river.title()} runs through the country of {country.upper()}!")

for river in rivers.keys():
    print(river)
print("\n")
for country in rivers.values():
    print(country)