# filling a dictionary with user input. start with blank dictionary
responses = {}

# set a flag to indicate that polling is active
polling_active = True
while polling_active:
    # Prompt for the persons name and response
    name = input("\nWhat is your name? ")
    response = input("Which mountain would you like to climb someday? ")

    # Store the responses in the dictionary
    responses[name] = response

    # FInd out if anyone else is going to take the poll.
    repeat = input("Would you like to let another person response? (yes/no) ")
    if repeat == 'no':
        polling_active = False
    
# Poll is complete. Show the results.
print("\n--- Poll Results ---")
for name, response in responses.items():
    print(f"{name.title()} would like to climb {response.title()}")