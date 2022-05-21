# This program says hello and asks for my name

print('Hello World!')#Print makes strings appear on screen
print('What is your name?') #ask for the name
myName = input() #Variable is defined from user input, input() for getting text from the keyboard.
print('It is nice to meet you, ' + myName)
print('The length of your name is:')
print(len(myName))
print('What is your age?') #ask for age
myAge = input()
print('You will be ' + str(int(myAge) + 1) + ' in a year')
#str returns values as a string, which is required for string concatination
#int returns values as integers, for math with other integers
#float returns values as floating numbers, they have the decimal point, not a whole number
#len takes a string value and reterns an integer value of the strings length
#print displays the value passed to it.
#functions are mini-programs inside the program.