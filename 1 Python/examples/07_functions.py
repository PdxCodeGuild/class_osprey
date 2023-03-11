'''
Anatomy of a function:
1. keyword 'def'
2. name of the function
3. parentheses
4. OPTIONAL: any number of parameters AKA arguments
5: a colon
6: the function body, indented
7: the return, None by default
'''


def say_hi(name: str, title: str):
    print(f'hello, {title}. {name}')
    return None


val = say_hi('Steve', 'Mr')
print(val)


'''Keyword arguments'''


def staff_bio(first_name: str, last_name: str, role: str = 'staff member', status: str = 'active'):
    print(f'{first_name} {last_name} is a {status} {role}')


# all positional arguments first (in order) and then the keyword arguments
staff_bio('Lars', 'the masseuse', status='fictional', role='masseuse')

staff_args: tuple = 'Sheri', 'Dover'
staff_kwargs: dict = {
    'status': 'amazing',
    'role': 'director'
}

staff_bio(*staff_args, **staff_kwargs)


'''Defining a function with arbitrary args and kwargs'''


def read_contents(*args, **kwargs):
    print(args[1])
    for kwarg in kwargs:
        print(kwarg, kwargs[kwarg])


read_contents(1, 'two', (3, 4), keyword1='one', keyword5=':)')


'''Returning from a function'''

# tuple unpacking
this_tuple: tuple = ('one', 'two', 'three')
one: str
two: str
three: str
one, two, three = this_tuple
print(one)
print(two)
print(three)

# beware!
also_a_tuple: tuple = 'thing',
print(type(also_a_tuple))


def multiply_recipe(multiplier: int, ing1: int, ing2: int, ing3: int):
    '''multiplies ingredients by their multiplier'''
    return multiplier*ing1, multiplier*ing2, multiplier*ing3


ingredients = multiply_recipe(2, 1, 2, 3)
butter, sugar, eggs = multiply_recipe(2, 1, 2, 3)

print(ingredients)
print(butter)
print(eggs)
print(sugar)


def first_sorted(*string_args):
    '''
    given an arbitrary number of strings,
    sort and return the first value after sorting
    '''
    string_list = list(string_args)
    string_list.sort()
    return string_list[0]


print(first_sorted('this is a string', 'not a strong one probably', ':) :)'))


is_raining = False
is_cold = False


def is_dan_happy():
    if not is_raining and not is_cold:
        return True
    return False


if is_dan_happy():
    print('hooray!')
