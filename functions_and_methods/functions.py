# def - keyword for function
# same naming convention like variables used with brackets and colon
# function must be called to be used
# function is used for DRY Principle (do not repeat yourself)


def say_hello():
    print('hellooooo')


print('----------function hello print-------------')
say_hello()


def add(a, b):
    return a + b


res_number = add(1, 2)  # adds integers
res_string = add('a', 'b')  #concatenates strings
res_list = add([2], [1])  # adds 2 lists
print(res_number)
print(res_string)
print(res_list)

# ARGUMENTS AND PARAMETERS
# we can make functions dynamic by giving them parameters
# same function can be called with different arguments resulting diff values returned
# def name(parameters)
# call name(arguments)

print('---------------------------')


def say_hello_1(name, emoji):
    print(f'hello {name} {emoji}')


say_hello_1('Prasad', '!! ')
say_hello_1('Ram', '!! ')

# DEFAULT PARAMETERS AND KEYWORD ARGUMENTS
# POSITIONAL ARGUMENTS -
say_hello_1('!!!', 'Prasad')  # gives output but may not be as expected

# KEYWORD ARGUMENTS
say_hello_1(emoji='!!!', name='Prasad')  # this gives by mapping arguments to parameters
# the above one isn't very good practice for coding

print('---------------------------------')


# DEFAULT PARAMETERS
# if we forget to give the parameters then the default parameters are taken up
# even if we give one among the 2 parameters it will take up the one defined rest from
# default parameters

def say_hello_1(name='Ram', emoji='!!!'):
    print(f'hello {name} {emoji}')


say_hello_1('Prasad', '!!')
say_hello_1('Prasad')
say_hello_1()

print('--------- Return --------------')


# RETURN - return keyword
# indicates the last part of the function anything post this won't be taken by interpreter
# if functions don't return anything in code it returns None
# Functions usually does only one thing (as good coding practice)

def multiply(num1, num2):
    def another_mul(num1, num2):
        return num1 * num2


print(multiply(5, 2))  # retunrs none as 1st function has nothing to return


def multiply(num1, num2):
    def another_mul(num1, num2):
        return num1 * num2

    return another_mul


print(multiply(5, 2)(10, 2))  # gives 20 as the 2nd num1, num 2 gets


# executed from the return part of the function. A simpler way of representing the same is

def multiply(num1, num2):
    def another_mul(num3, num4):
        return num3 * num4

    return another_mul(num1, num2)


print(multiply(5, 2))  # this would then call the initial argument values only
