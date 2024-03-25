# if , elif and else

is_old = True
is_licenced = True

if is_old:
    print('you are old enough to drive')
elif is_licenced:
    print('You can drive now')
else:
    print('you are not of age')

if is_old and is_licenced:
    print('You are old enough and can drive now')
else:
    print('you are not of age')
print('OK')

# TRUTHY and FALSY

print('following is truthy')
print(bool(5))
print(bool('hello'))

print('following is falsy')
print(bool(0))
print(bool(''))
print(bool(None))

# following statment automatically checks for bool(value) in the if loop

username = input('Please enter username')
password = input('please enter password')

if username and password:
    print('You have entered username and password')
else:
    print('You have incorrect username or password')

# above combinations can be used inside of if loop as well
# As explained in the documentation, all values are considered "truthy" except for the following, which are "falsy":
# -> None
# -> False
# Numbers that are numerically equal to zero, including:
# -> 0
# -> 0.0
# -> 0j
# -> decimal.Decimal(0)
# -> fraction.Fraction(0, 1)
# Empty sequences and collections, including:
# [] - an empty list
# {} - an empty dict
# () - an empty tuple
# set() - an empty set
# '' - an empty str
# b'' - an empty bytes
# bytearray(b'') - an empty bytearray
# memoryview(b'') - an empty memoryview
# an empty range, like range(0)
# objects for which
# -> obj.__bool__() returns False
# -> obj.__len__() returns 0, given that obj.__bool__ is undefined


# TERNARY OPERATOR

# format :
# true_result if condition else false_result
is_friend = False
can_message = "can message" if is_friend else "Not allowed"
print(can_message)

# SHORT circuit - while working with OR, AND  operator
# during and OR operation the interpreter first checks only the 1st value of if condition, if its true
# it doesn't check the 2nd condition itself and directly returns true, if its false then only it checks
# the 2nd condition
# similarly during and operation the interpreter first checks 1st value of if condition, if its false
# it doesn't check 2nd condition but returns false. If it's true, then it checks the 2nd condition


