# AND, OR used so far
# others are >, < , ==,!=,  >=, <=

print(4 > 5)
print(4 < 5)
print(4 == 5)
print(4 != 5)
print('hello' >= 'hello')  # does ascii comparision

print(not (1 == 1))
print(not (1 == 2))

# Exercise

is_magician = False
is_expert = True

if is_magician and is_expert:
    print('You are a master magician')
elif is_magician and not is_expert:
    print('you are getting there')
elif not is_magician:
    print('You need magic powers ')

# is and ==
print('Is and == use cases ')
print(True == 1)
print('' == 1)
print([] == 1)
print(10 == 10.0)
print([] == [])


print('is usecase')
# is checks the memory location and compares them
# though [] and [] are same but the memory location where they are stored are different
print(True is 1)
print('' is 1)
print([] is 1)
print(10 is 10.0)
print([1,2,3] is [1,2,3]) # though they are same but are different lists

# Following yield true
print(True is True)
print(10 is 10)
print('10' is '10')