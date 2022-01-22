# slicing a list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[0:3])
# returns first 3 elements

# returns 2, 3, 4 elements in list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[1:4])

# omitting first index in a slice automatically starts slice at beginning
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[:4])

# same principle applies when omitting second index
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[2:])

# using a negative will move index backwards from end of list
players = ['charles', 'martina', 'michael', 'florence', 'eli']
print(players[-3:])

# looping + slicing
players = ['charles', 'martina', 'michael', 'florence', 'eli']
for player in players[:3]:
    print(player.title())
