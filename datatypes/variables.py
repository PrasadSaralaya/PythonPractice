emp_id = 90
_id = 50

print(_id)
print(emp_id)
# snake cases
# lower case starting or underscore and no numbers
# constants are usually written in capital values like PI
PI = 3.14

# dunder variables in python start with double underscores (used by
# python language only

# quick assignment of values to the variables
a, b, c = 1, 'a', 3

print(a)
print(b)
print(c)

# Expressions vs statements

iq = 100  # statement

age = iq / 5  # entire line is a statement while iq/5 is an expression

# augmented assignment variables

value = 5
value = value + 2
print('value - ' + str(value))
# above statement can be assigned using += which is an augmented assignment operator which
# will work the same as above. similarly there are *=, -=, /=

value = 5
value += 2
print('value in augmented variable - ' + str(value))

# STRINGS
# 3 single quotes is used to denote long strings coming in multiple lines
print(type("any type of string value"))

long_string = ''' 
this is 
very long
string
'''
username = 'name'
password = 'pwd'

print(long_string)

# string concatenation
f_name = 'Prasad'
l_name = 'Saralaya'
full_name = f_name + l_name
full_name_with_space = f_name + ' ' + l_name

print(full_name)
print(full_name_with_space)

# Type conversion
print('type conversion ')
a = str(100)
print(type(a))
# similar to what was done earlier in line number 31, 37

# Escape sequences
# used in single quote, apostrophe or double quotes
# whatever comes after backslash is considered as string

weather = 'it\'s \"kind of \" sunny today'
print(weather)
# similarly \t \n can be used for tab and newline character
weather = '\t it\'s \"kind of \" sunny today \n hope you have a good day'
print(weather)

# Formatted String
name = 'Prasad'
age = 10

print('Hi ' + name + '. You are ' + str(age) + ' years old.')
# the same above code can be done better with formatted strings use curly braces for variable
print('-----formatted string--------')
print(f'Hi {name}. You are {age} years old.')
# Below is an old way of formatting string we can add variables and also individual strings
print('Hi {}. You are {} years old.'.format('Prasad', '10'))
print('Hi {}. You are {} years old.'.format(name, age))

# STRING INDEXES

name = 'prasad'

print(name[0])
print(name)

# we can have a start and stop within the square bracket
# like name[start:stop]
# stop is not included
print(name[0:3])  # pra
print(name[0:6])  # prasad
print(name[0:7])  # doesnt error out
# below one prints from 3rd character till end
print(name[2:])  # asad
# below is the example where it prints from start till 2nd character
print(name[:2])  # pr
# further if there is a need to skip characters and step over then
# name[start:stop:stepover]
# that can be done by using similar thing as shown below
print(name[0:7:3])
# step over to 1t character
print(name[::1])  # default value entire string comes in
# negative index starts from end
print(name[-1])
# we can reverse the string by using -1 in the s
print(name[::-1])
# negative is used to have the data of string from last to beginning
# the above thing done is called string slicing
