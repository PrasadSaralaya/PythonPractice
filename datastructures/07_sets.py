# Set is collection of unique objects
# give assignment using curly braces and add comma seperated objects

my_set = {1, 2, 100, 3, 4, 5, 6, 6}

print(my_set)  # duplicates are automatically deleted
my_set.add(2)
my_set.add(200)
print(my_set)  # 200 is added while not 2  duplicates are automatically deleted
print(list(my_set))  # typecast to list
# print(my_set[0]) # errors out as it doesnt have index

print(1 in my_set)  # returns true

list_val = [1, 9, 3, 4, 5, 6, 6, 7, 7, 8]

print(list_val)
print(set(list_val))

my_set_new = my_set.copy()
my_set.clear()

print(my_set)  # gets cleared
print(my_set_new)  # as its copied old set is absent while new one is present

# Set methods

# difference

my_set = {1, 2, 3, 4, 5}
your_set = {4, 5, 6, 7, 8, 9}

print(my_set.difference(your_set))  # gives difference but not assigned hence values remain
print(your_set.difference(my_set))  # gives difference but not assigned hence values remain order not maintained

# discard

my_set.discard(1)
print(my_set)  #discarded 1 here

my_set.add(1)
print(my_set)

# difference update
my_set.difference_update(your_set)
print(my_set) # common elements are removed and updated

my_set = {1, 2, 3, 4, 5} # updating back
your_set = {4, 5, 6, 7, 8, 9}
# intersection

print(my_set.intersection(your_set)) # common elements are shown

# disjoint

print(my_set.isdisjoint(your_set)) # checks if both sets are unique with eachother

# union

print(my_set.union(your_set)) # combines both the set but keeps only unique items and delete duplicates

# is subset
my_set = { 4, 5}
print(my_set.issubset(your_set)) # will return true as my set is subset of your set values

# is superset

print(your_set.issuperset(my_set)) # also returns true as your set is super set of my set values



