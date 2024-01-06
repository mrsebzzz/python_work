guest_list = ['layne', 'travis', 'grace']
print(f"Hey {guest_list[0].title()}, I would like to invite you over for dinner")
print(f"Hey {guest_list[1].title()}, I would like to invite you over for dinner")
print(f"Hey {guest_list[2].title()}, I would like to invite you over for dinner")


#changing guest list
print(guest_list)
print(F"Sorry to hear that {guest_list[2].title()} can't make it to dinner")

guest_list.pop(-1)
guest_list.append('susie')
print(guest_list)
print(f"Hey {guest_list[0].title()}, I would like to invite you over for dinner")
print(f"Hey {guest_list[1].title()}, I would like to invite you over for dinner")
print(f"Hey {guest_list[2].title()}, I would like to invite you over for dinner")

print(f"Hey, {guest_list[0].title()}, {guest_list[1].title()}, {guest_list[2].title()} I have found a bigger table")

#more guests
guest_list.insert(0, 'matt')
guest_list.insert(2, 'bill')
guest_list.append('skylar')
print(guest_list)
print(f"Hey {guest_list[0].title()}, I would like to invite you over for dinner")
print(f"Hey {guest_list[1].title()}, I would like to invite you over for dinner")
print(f"Hey {guest_list[2].title()}, I would like to invite you over for dinner")
print(f"Hey {guest_list[3].title()}, I would like to invite you over for dinner")
print(f"Hey {guest_list[4].title()}, I would like to invite you over for dinner")

#shrinking guest list
print('Sorry I can only invite two people to dinner now')
matt = guest_list.pop(0)
susie = guest_list.pop(3)
travis = guest_list.pop(2)
print(f"Sorry, {travis.title()}, {susie.title()}, and {matt.title()} there is no longer room at my table for you")

print(guest_list)
print(f"hey, {guest_list[0].title()} and {guest_list[1].title()} and {guest_list[2].title()} you are still invited.")

del guest_list[0]
del guest_list[1]
del guest_list[0]
print(guest_list)

print(len(guest_list))