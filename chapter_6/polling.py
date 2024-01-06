# Dictionary of similiar objects
favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    'sebastian': 'html',
    'layne': 'css',
    'travis': 'java',
    }

people = ['john', 'sebastian', 'layne', 'dennis', 'reed']

for name in favorite_languages.keys():
    if name in people:
        print(f"Thank you for taking the poll, {name.title()}")
    else:
        print(f"Please take our poll, {name.title()}")



