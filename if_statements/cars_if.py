cars = ['audi', 'bmw', 'subaru', 'toyota']

for car in cars:
    if car == 'bmw':
        print(car.upper())
    else:
        print(car.title())
# >>> car = 'bmw'
# >>> car == 'bmw'
# True
# >>> car = 'audi'
# >>> car == 'bmw'
# False
# = denotes statement usually
# == denotes question usually
# case matters
# >>> car = 'Audi'
# >>> car == 'audi'
# False
# >>> car = 'Audi'
# >>> car.lower() == 'audi'
# True
# >>> car
# 'Audi'