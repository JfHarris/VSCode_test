#age = 23
#message = "Happy " + age + "rd Birthday!"
#
#print(message)
# Would result in TypeError: Can't convert 'int' object to str implicitly
# because it doesn't know whether you mean value 23 or chars 2 and 3.
# Must specify you want to use integer as a string

age = 23
message = "Happy " + str(age) + "rd Birthday!"

print(message)