reservation_number = input("How many people are in your party? ")
reservation_number = int(reservation_number)

if reservation_number > 8:
    print("You will have to wait for a table")
else:
    print("Your table is ready")