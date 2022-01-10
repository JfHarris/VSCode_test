#list exercises
bicycles = ['trek', 'cannondale', 'redline', 'specialized']
print(bicycles)

#accessing elements in a list
print(bicycles[0])
#will print trek

print(bicycles[0].title())
#will print Trek

#remember that lists start at 0 not 1
print(bicycles[1])
print(bicycles[3])
#will print cannondale and specialized

print(bicycles[-1])
#will print last item in list...specialized in this case
# - can be used with other numbers too to work backward from end of list

message = "My first bicycle was a " + bicycles[0].title() + "."
print(message)