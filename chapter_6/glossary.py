programming_words = {
    'loop': 'Used to shorten code and loop through',
    'traceback': 'How python shows errors',
    'dictionary': 'Collection of data with key-value pairs',
    'key-value': 'Deals with dictionarys. How the information is stored',
    'python': 'Programming language',
    'set': 'A collection that must be unique',
    'user-input': 'Input gathered from the user',
    'elif': 'Else-If statement',
    }

print(f"Loop is defined as: \n\t {programming_words['loop']}")
print(f"Traceback is defined as: \n\t {programming_words['traceback']}")
print(f"Dictionary is defined as: \n\t {programming_words['dictionary']}")
print(f"Key-Value is defined as: \n\t {programming_words['key-value']}")
print(f"Python is defined as: \n\t {programming_words['python']}")

# glossary 2, cleaning up the code

for word, definition in programming_words.items():
    print(f"{word.title()} is defined as: {definition}.")