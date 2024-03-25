# For loop
# for variable in iterable :
#   do something

# here the iterable can be anything like list, set , tuple , string etc.
# there can also be multiple levels of nesting within for loop

for item in 'Zero to mastery':
    print(item)

for item in [1, 2, 3]:
    print(item)
print('-------------')
for item in (1, 2, 4):
    print(item)
print('-------------')
for item in {1, 2, 3, 5}:
    print(item)

print('outside loop')
print(item)

print('multi level nesting')
for i in [1, 2, 3]:
    for j in ['a', 'b', 'c']:
        print(i, j)

# ITERABLES
# it can be list, set, dictionary, tuple , string or anything that can be iterated over is iterable
# iterate - action of iterating over an iterable
# main coverage of topic here is on dictionaries

user = {
    'name': 'Prasad',
    'age': 30,
    'is_married': True
}

print('Iterables')
# following print gives only key values of the dictionary
for item in user:
    print(item)

# there are few keywords to be used along with dict to get the items, keys, values etc. Eg is below
print('-----tuple------')
for item in user.items():
    print(item)  # gives the tuple of dictionary items

print('------Values-----')
for item in user.values():
    print(item)  # gives the keys of dictionary items

print('------keys-----')
for item in user.keys():
    print(item)  # gives the keys of dictionary items

# if we want to iterate through without tuple but get the keys and values we can do it as well
for item in user.items():
    key, value = item
    print(key, value)  # prints key and value with a space

# better way of programming the same is below
print('-----')
for k, v in user.items():  # k and v represents key and value
    print(k, v)

# 50 is not iterable hence this errors out
# for i in 50:
#     print(i)

# EXERCISE
# Sum of a list
my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

sum = 0
for i in my_list:
    sum = sum + i

print(sum)

# RANGE
# produces a sequence of integers from start to stop
# creates a range object on creation
# following eg creates range from 0-9 (count of range starts from 0)
for i in range(10):
    print(i)

# we can even use start stop and step over when needed
# all even numbers are printed here

for i in range(0, 10, 2):
    print(i)
# nothing is printed in below example
for i in range(0, 10, -1):
    print(i)
# if we want from bigger to smaller, then large to small number must be placed
for i in range(10, 0, -2):
    print(i)

# range of values can be converted to list
print(range(10))
print(list(range(10)))

# Enumeration
# adds index to the iterable and it can be used within the loop for any uses

for char in enumerate('prasad'):
    print(char)

# belowth code unpacks the enumeration and prints the index of it
for i, char in enumerate('prasad'):
    print(i, char)
# iterable can be list, tuple or any other iterable
print('-----------list ---------')
for i, char in enumerate([1, 2, 3]):
    print(i, char)

for i, char in enumerate(list(range(100))):
    if char == 50:
        print(f'index of char {char} is : {i}')

# WHILE LOOP

# while condition:
#   do something
#
# If conditions are given without increment or decrement then there will be infinite loop
# to avoid it we can use break
# while loop also has an else condition usually used only when there is a break

i = 0

while i < 50:
    print(i)
    i += 1
else:
    print('done printing 50 items')

# for is used usually when you need to iterate over iterable... in other cases
# when there is a condition is true we need to loop then while does a better job

while True:
    response = input('Whats your name :')
    if response.lower() == 'prasad':
        break
# these are the cases where break will be helpful

# break, continue and pass
# break can also be used in for loop
# break breaks the loop be it while or for
# continue will continue the loop when it reaches a particular line no matter what
# pass will pass to the next line
