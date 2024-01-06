def make_shirt(size, text):
    print(f"Your shirt size is {size.upper()} and the text is {text.title()}")

make_shirt('large', 'python')
make_shirt(size='large', text='coding')

def make_shirt(text, size='large'):
    print(f"Your shirt size is {size.upper()} and the text is {text.title()}")

make_shirt('I love python')
make_shirt('I love python', size='medium')
make_shirt('Any text here', size='small')