# simple dictionary
alien_0 = {'color': 'green', 'points': 5}
print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print(f"You just scored {new_points} points!")

# adding new key-value pairs
print(alien_0)

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

# building an empty dictionary
alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)

# modifying values
alien_0 = {'color': 'green'}
print(f"The alien is {alien_0['color']}.")

alien_0 = {'color': 'yellow'}
print(f"The alien is now {alien_0['color']}.")

# removing key-value pairs
alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)