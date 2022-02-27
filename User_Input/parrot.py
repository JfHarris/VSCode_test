from click import prompt
# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#     message = input(prompt)
#     print(message)

# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. hello
# hello

# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. quit
# quit

# adding if statement keeps it from printing message

# prompt = "\nTell me something, and I will repeat it back to you: "
# prompt += "\nEnter 'quit' to end the program. "
# message = ""
# while message != 'quit':
#    message = input(prompt)
#    if message != 'quit':
#        print(message)

# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. hello
# hello

# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. quit

prompt = "\nTell me something, and I will repeat it back to you: "
prompt += "\nEnter 'quit' to end the program. "

active = True
while active:
    message = input(prompt)
    if message == 'quit':
        active = False
    else:
        print(message)

# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. hello
# hello

# Tell me something, and I will repeat it back to you: 
# Enter 'quit' to end the program. quit
