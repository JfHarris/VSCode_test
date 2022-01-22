# tuple overview
dimensions = (200, 50)
for dimension in dimensions:
    print(dimension)

print("\n")

# writing over a tuple
dimensions = (200, 50)
print("Original dimensions:")
for dimension in dimensions:
    print(dimension)

dimensions = (400, 100)
print("\nModified dimensions:")
for dimension in dimensions:
    print(dimension)

# Use tuples when you want to store values that should not
# be changed throughout the life of a program
