# list in dict
pizza = {
    'crust': 'thick',
    'toppings': ['mushrooms', 'extra cheese'],
}
# Summary of order
print("You ordered a " + pizza['crust'] + "-crust pizza " +
      "with the following toppings:")
for topping in pizza['toppings']:
    print("\t" + topping)
print("\n")
# You ordered a thick-crust pizza with the following toppings:
#        mushrooms
#        extra cheese
