# This program says hello and asks for my name

print('Hello World!')
print('What is your name?') #ask for the name
myName = input() #Variable is defined from user input
print('It is nice to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') #ask for age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')