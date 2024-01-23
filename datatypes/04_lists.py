# LISTS - Type of DATA STRUCTURE
# group of objects of any type
# denoted by sq brackets within which there can be objects
# It can have objects of different datatype as well
# Lists are mutable

li1 = [1, 2, 3, 4]
li = [1, 2, 'a']
print(li)
print(li1)

amazon_cart = ['notebook', 'sunglasses', 'watches', 'laptop']
print(amazon_cart[0])
print(amazon_cart[1])
print(amazon_cart)

# List slicing

print(amazon_cart[0:2])  # similar to string slicing
print(amazon_cart[0::2])  # step over similar to string

# element of list can be re-asssigned as lists are mutable
amazon_cart[0] = 'textbook'
print(amazon_cart)  # notebook changes to text book
new_cart = amazon_cart  # if assignment is done this way the old list gets updated
# as the assignment is done to memory location of initial list and so its updated
new_cart[0] = 'gum'
# now amazon cart gets gum value
print(amazon_cart)
print(new_cart)
# re-assigning old value back to cart
amazon_cart[0] = 'textbook'
print('--------------------')
new_cart_1 = amazon_cart[:]  # if assignment is done this way the old list doesn't get updated
new_cart_1[0] = 'can'
# now amazon cart doesnt get can value
print(amazon_cart)
print(new_cart_1)

# MATRIX

# 2d matrix is stored as list of list and dimensions can be
# further increased by using inner lists

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(matrix[0])
print(matrix[1][2])

#  List methods

basket = [1, 2, 3, 4]
print(len(basket))

# ADDITION
# Append
# you can add an element to the list with and object using append method
# while appending u cant assign it to a new list (as its just an operation of assignment happening
# hence the assignment will yield None

new_basket = basket.append(10)  # this will yield None, however value is added to original list
print(new_basket)
print(basket)
print('---------------')
basket.append(20)
new_basket = basket[:]
print(new_basket)  # now new basket has all the values of old basked

# Insert
print(basket[3])
basket.insert(0, 30)
print(basket[3])  # added at a particular index . elements after this will get its index increased by 1
# earlier the priny value was 4 which has now changed to 3
print(basket)
# extend
basket.extend([40, 50])
# extends the list by number of elements given based on values inside the sq brackets
print(basket)
# Removal
print('------------POP------------')
basket.pop()
print(basket)  # last element is removed

basket.pop(0)  # pops the element of the index
print(basket)  # 1st element is removed here

# remove()
basket.remove(2)
# basket.remove(30) errors out as this element is not in the list
print(basket)  # here the given element gets removed
print(new_basket)
new_basket.clear()  # clears the entire list
print(new_basket)
