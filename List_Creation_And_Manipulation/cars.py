# sort prints list alphabetically
cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort()
print(cars)
print("\n")

# revrse sort

cars = ['bmw', 'audi', 'toyota', 'subaru']
cars.sort(reverse=True)
print(cars)
print("\n")
# sort changes are permanent

# using sorted()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print("Here is the original list:")
print(cars)

print("\nHere is the sorted list:")
print(sorted(cars))

print("\nHere is the original list again:")
print(cars)
print("\n")

# using reverse()
cars = ['bmw', 'audi', 'toyota', 'subaru']
print(cars)

cars.reverse()
print(cars)
# reverse() changes are permanent but can be undone by running reverse() again

# len() example
# >>> cars = ['bmw', 'audi', 'toyota', 'subaru']
# >>> len(cars)
# 4

# len() can be helpful in resolving index errors
