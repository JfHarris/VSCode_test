alien_0 = {'color': 'green', 'points': 5}

print(alien_0['color'])
print(alien_0['points'])

new_points = alien_0['points']
print("You just earned " + str(new_points) + " points!")
print("\n")

# add new value to dictionary

alien_0 = {'color': 'green', 'points': 5}

print(alien_0)
alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)
print("\n")
# starting with an empty dictionary and adding to it

alien_0 = {}

alien_0['color'] = 'green'
alien_0['points'] = 5

print(alien_0)
print("\n")

# changing values in a dictionary

alien_0 = {'color': 'green'}
print("The alien is " + alien_0['color'] + ".")

alien_0['color'] = 'yellow'
print("The alien is now " + alien_0['color'] + ".")
print("\n")

# moving alien

alien_0 = {'x_position': 0, 'y_position': 25, 'speed': 'medium'}
print("Original x-position: " + str(alien_0['x_position']))
# Move the alien to the right
# Determine how far to move the alien based on its current speed
if alien_0['speed'] == 'slow':
    x_increment = 1
elif alien_0['speed'] == 'medium':
    x_increment = 2
else:
    x_increment = 3
# New position is old position + increment
alien_0['x_position'] = alien_0['x_position'] + x_increment
print("New position: " + str(alien_0['x_position']))

print("\n")
# removing key-value pairs

alien_0 = {'color': 'green', 'points': 5}
print(alien_0)

del alien_0['points']
print(alien_0)
