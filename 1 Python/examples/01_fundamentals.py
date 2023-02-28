# variable assignment

variable_name = 'value'
value = variable_name

print(variable_name)
print(value)

# data types in python

a_string = "this is a string"
an_int = 1
a_float = 1.2342342345234
# complex numbers are another type
another_float = 1.0
a_bool = True
a_list = [1, 2, 3, 'four', {'five', 'six'}, a_float, a_string]
a_dict = {
    1: 2,
    3: 'four',
    'five': 6,
    7.0: 8,
    a_string: a_bool,
    True: False,
    1: 'what???',
    (1, 2): 'tuples can be dict keys!'
}
a_tuple = (1, 2, 3)  # immutable
a_set = {1, 2, 2, 2, 3, 4, 5, 5, 5, 1, 1, 1, 1.0, '1', 1.1}


def a_function():
    return "hello!"


print(a_dict)
print(a_set)

print(type(a_tuple))
print(type(a_function))


# LITERALS

# msg1 is a literal because the value is hard-coded
msg1 = 'this is a literal value'
# msg2 is not literal because the value is determined by user input
# msg2 = input('what time is it?')
# print(msg2)


# MUTABILITY
'''
Mutability means that when you change the value of a variable,
it retains the same identity
lists, dictionaries, and sets are mutable
everything else is immutable
'''

# val1 = 1
# val2 = 1
# print(id(val1))
# print(id(val2))
# val1 = 'one'
# print(id(val1))


colors = ['red', 'green', 'blue']
print(id(colors))
blue = colors.pop()
colors.append('yellow')
print(colors)
print(id(colors))

seasons = ('spring', 'summer', 'fall', 'winter')
# I can reassign different stuff to this variable, but I can't actually change this tuple
print(id(seasons))
print(id(seasons[1]))
# seasons = 1
# print(id(seasons))


# ORDERED VS UNORDERED
'''
Ordered types have an order built in, the order is an inherent part of the value.
Ordered types can be accessed by index
Lists, tuples, and strings are ordered, nothing else is
'''

print(colors[2])
# print(colors[10])
# IndexError: list index out of range
print(seasons[0])
print('hello'[3])

# print(a_set[0])
# TypeError: 'set' object is not subscriptable

# print(a_dict[5])
# KeyError: 5


# TYPE CONVERSION
'''
Type conversion is changing something from one type to another
It can be explicit, using casting
or implicit, as the result of an operation
'''

# int casting

num = '1'
num2 = int(num)
print(type(num))
print(type(num2))
# user_num = input('type a number')
# print("double that number is: ", 2*int(user_num))

this_float = 3.0
print(this_float)
print(int(this_float))

print(int(False))
print(int(True))


# float casting
print(float(1))
print(float('1'))
# print(float('one'))
# ValueError: could not convert string to float: 'one'

# float conversion
print(3 * 1.0)


# string casting
# almost anyting can be string cast!

print(str(1.0))
print(str([1, 2]))
print(str({1: 2, 3: 4}))
print(str(True).lower())
print(str(a_function).upper())


# list casting
# only types that are iterable/subscriptable can be list cast

print(list((1, 2)))
print(list('hello'))
print(list({1: 2, 3: 4, 5: 6}))
print(list({1, 2, 3, 4, 5, 6, 6, 6, 6}))
