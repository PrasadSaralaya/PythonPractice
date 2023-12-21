from datetime import datetime

# Immutability

# strings are immutable in python meaning that the index value string cannot be reassigned
name = 'prasad'
print(name)
name = 'saralaya'
print(name)  # this is entire re-assignment
# name[1] = 's' # this will error out
name = name + 'a'
print(name)  # this won't error out as its addition of a string
# and entire variable name gets reassigned

# BUILT-IN FUNCTIONS AND STRING METHODS
print(len('prasad'))
# methods used specifically for string
new_name = name.replace('a', 'p')
print(name.upper())
print(name.find('a'))  # gets the 1st occurance of the string value
print(new_name)

# BOOLEAN
# can be either true or false

print(bool(0))
print(bool(-189))
print(bool(189))
print(bool(1))
print(bool('True'))
print(bool('False'))
print(bool('Prasad'))

# Exercise

birth_year = input('What year were you born ??')

currentYear = datetime.now().year
age = currentYear - int(birth_year)
print(f'Your age is {age}')

# exercise to have comments
# it can be written either with hash or with 3 single quotes as well
# 3 single quote will become a doc string


# exercise
username = input('Enter username: ')
password = input('Enter password: ')

pwd_len = len(password)
pwd_secret = '*' * pwd_len

print(f'Hi {username}, your password {pwd_secret} is {pwd_len} letters long')
