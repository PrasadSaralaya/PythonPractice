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

#augmented assignment variables

value = 5
value = value + 2
print("value - " + str(value))
# above statement can be assigned using += which is an augmented assignment operator which
# will work the same as above

value = 5
value += 2
print("value in augmented variable - " + str(value))