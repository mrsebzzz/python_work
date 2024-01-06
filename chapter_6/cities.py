cities = {
    'richmond': {
    'country': 'USA',
    'population': 16000,
    'fact': 'Dark shitty place',
    },
    'denver': {
    'country': 'USA',
    'population': 2000000,
    'fact': 'home of the broncos'
    },
    'blacksburg': {
    'country': 'USA',
    'population': 4000,
    'fact': 'virginia tech'
    },
}

for city, city_info in cities.items():
    print(f"\nCity: {city.title()}")
    country = f"{city_info['country']}"
    population = f"{city_info['population']}"
    facts = f"{city_info['fact']}"

    print(f"\tCountry: {country}")
    print(f"\tPopulation: {population}")
    print(f"\tFact: {facts.title()}")