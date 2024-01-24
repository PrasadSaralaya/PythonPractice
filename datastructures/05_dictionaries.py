# Dictionary also called dict
# called as map or hash table  in other language
# in python its datatype and data structure. It is mutable as the values can change
dictionary = {
    'a': 1,
    'b': True,
    'c': 'd'
}

print(dictionary['a'])  # returns 1 which is value of 'a' key
print(dictionary['b'])  # returns True which is value of 'a' key
print(dictionary['c'])  # returns d which is value of 'a' key
# print(dictionary['d'])# errors out as the key is not present
print(dictionary)
# here 'a','b' is called key and 1, 2 etc. its respective value
# key can be of any data type like int, string, boolean etc. and are not always
# in any order. key cant be of any data structure like list, but any datatype works as its
# suppose to be immutable. However, value can be anything like list, int, string or boolean
# Keys in dictionaries must be unique else it will be overridden by the last value

dictionary_mixed = {
    'a': [1, 2, 3, 4, 5],
    10: 2,
    True: 3
}

print(dictionary_mixed['a'])  # prints entire list
print(dictionary_mixed['a'][4])  # prints 5th element of list
print(dictionary_mixed[10])  # prints 2
print(dictionary_mixed[True])  # prints 3

# we can create a list with multiple dictionaries within
dictionary_list = [
    {
        'a': [1, 2, 3, 4, 5],
        10: 2,
        True: 3
    },
    {
        'a': [6, 7, 8, 9],
        10: 20,
        True: 30
    }
]

# print(dictionary_list['a']) # fails with error as its list of dictionary
print(dictionary_list[0]['a'])  # prints list with 1-5
print(dictionary_list[1]['a'])  # prints list with 6-9
print(dictionary_list[1]['a'][3])  # prints 9
# accessing elements differs based on the way dict is written

# dictionary dups
dictionary_dup = {
    10: 'QWERTY',
    10: 'Ten'
}

print(dictionary_dup)  # gives only 2nd element 1st one gets ignored

# Dictionary methods
# as a good practice instead of using dictionary[key] it is better
# to use dictionary.get(key)

print('--------------')
print(dictionary)
print(dictionary.get('a'))
print(dictionary.get('b'))

# instead of assigning a dictionary using json we can also use dict keyword
dictionary_eg = dict(name='prasad', subject=['english', 'maths'])
print(dictionary_eg)

# similar to in operator used in list we can use in dictionary as well

print('a' in dictionary) # true is returned as name key is present
print(1 in dictionary.values()) # true is returned as 1 value is present
print(1 in dictionary.keys()) # false is returned as 1 key is not present
print('a' in dictionary.keys()) # true is returned as a key is present
print(dictionary.items()) # Gives tuple of all the items of dictionary

# copy, update, pop and clear methods in dictionary

dictionary_cpy = dictionary.copy()
print(dictionary_cpy)

dictionary.update({'a':55})
print(dictionary) # a changes from 1 to 55

dictionary.pop('a')
print(dictionary) # key value pair a is popped out

dictionary.popitem()
print(dictionary) # pops the last element in the dictionary element c is removed here

dictionary.clear()
print(dictionary) # gives empty dictionary
print(dictionary_cpy) # gives  dictionary value as its copied
