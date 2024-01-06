prompt = "\nTell me something and I will repeat it: "
prompt += "\nEnter 'quit' to end the Parrot Program. "

message = ""
while message != 'quit':
    message = input(prompt)

    if message != 'quit':
        print(message)