# Tuples are like list but are immutable
# cant sort or reverse the tuple
# but in case of performance is better than lists


basket = (1, 2, 3, 4, 5, 5)
print(basket)
print(basket[2])
print(5 in basket)  # returns true or false like list

# basket[0] = 9 # errors out as tuples are immutable
# tuple can be used as key value in the dictionary as well
user = {
    (1, 2): [1, 2, 3, 4],
    'name': 'prasad'
}

print(user[(1, 2)])

new_basket = basket[:]

print(new_basket)
new_basket = basket[1:2]
print(new_basket)  # has (2,) as single element in tuple has comma

# individual assignment can be done similar to list

x,y,z, *others = (1,2,3,4,5,6)

print(x)
print(y)
print(others)

# tuple methods

print(basket.count(5)) # gives number of times the value occurs
print(basket.index(5)) # gives 1st index when the value occurs
print(len(basket)) # gives count of tuple

