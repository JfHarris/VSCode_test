# requested_topping = 'mushrooms'
#
# if requested_topping != 'anchovies':
#     print("Hold the anchovies!")

# >>> requested_toppings = ['mushrooms', 'onions', 'pineapple']
# >>> 'mushrooms' in requested_toppings
# True
# >>> 'pepperoni' in requested_toppings
# False

requested_toppings = ['mushrooms', 'extra cheese']

if 'mushrooms' in requested_toppings:
    print("Adding mushrooms.")
if 'pepperoni' in requested_toppings:
    print("Adding pepperoni.")
if 'extra cheese' in requested_toppings:
    print("Adding extra cheese.")

print("\nFinished making your pizza!")
print("\n")

# will only run first if because it returns true and negates elifs
# requested_toppings = ['mushrooms', 'extra cheese']

# if 'mushrooms' in requested_toppings:
#     print("Adding mushrooms.")
# elif 'pepperoni' in requested_toppings:
#     print("Adding pepperoni.")
# elif 'extra cheese' in requested_toppings:
#     print("Adding extra cheese.")

# print("\nFinished making your pizza!")

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")
print("\n")

# checking for missing items

requested_toppings = ['mushrooms', 'green peppers', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping == 'green peppers':
        print("Sorry, we are all out of green peppers right now.")
    else:
        print("Adding " + requested_topping + ".")

print("\nFinished making your pizza!")
print("\n")

# checking empty list

requested_toppings = []

if requested_toppings:
    for requested_topping in requested_toppings:
        print("Adding " + requested_topping + ".")
else:
    print("Are you sure you want a plain pizza?")
print("\n")

# using multiple lists

available_toppings = ['mushrooms', 'olives', 'green peppers',
                        'pepperoni', 'pineaplle', 'extra cheese']

requested_toppings = ['mushrooms', 'french fries', 'extra cheese']

for requested_topping in requested_toppings:
    if requested_topping in available_toppings:
        print("Adding " + requested_topping + ".")
    else:
        print("Sorry, we don't have " + requested_topping + ".")

print("\nFinished making your pizza!")
