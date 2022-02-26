# List of dicts
alien_0 ={'color': 'green', 'points': 5}
alien_1 = {'color': 'yellow', 'points': 10}
alien_2 = {'color': 'red', 'points': 15}

aliens = [alien_0, alien_1, alien_2]

for alien in aliens:
    print(alien)

# {'color': 'green', 'points': 5}
# {'color': 'yellow', 'points': 10}
# {'color': 'red', 'points': 15}
print("\n")

# Empty list to store aliens
aliens = []
# Make 30 green aliens
for alien_number in range(0, 30):
    new_alien = {'color': 'green', 'points': 5, 'speed': 'slow'}
    aliens.append(new_alien)
# Show first 5 aliens
for alien in aliens[0:5]:
    print(alien)
print("...")
# Show how many aliens have been created
print("Total number of aliens: " + str(len(aliens)))
print("\n")
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# {'color': 'green', 'points': 5, 'speed': 'slow'}
# ...
# Total number of aliens: 30

# Changing aliens
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien ['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10

# Show first 5 new aliens
for alien in aliens[0:5]:
    print(alien)
print("...")
print("\n")

# Changing aliens again
for alien in aliens[0:3]:
    if alien['color'] == 'green':
        alien ['color'] = 'yellow'
        alien['speed'] = 'medium'
        alien['points'] = 10
    elif alien['color'] == 'yellow':
        alien['color'] = 'red'
        alien['speed'] = 'fast'
        alien['points'] = 15

# Show first 5 new aliens
for alien in aliens[0:5]:
    print(alien)
print("...")
print("\n")
