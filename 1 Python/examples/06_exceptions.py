'''
Programming languages are either interpreted or compiled
Python is both
'''

'''Compilation errors (thrown by the compiler)'''

# print('hello) #SyntaxError: unterminated string literal
# print('hello' #SyntaxError: '(' was never closed
# 1.upper() #SyntaxError: invalid decimal literal


# IndentationError: expected an indented block
# def hello():
# print('hello') # imagine this has the wrong number of spaces!


'''Runtime errors (thrown by the interpreter)'''
# print(hello) #NameError: name 'hello' is not defined.

colors = ['red']
blue = 'blue'
colors.append(blue)
# blue.append('green') #AttributeError: 'str' object has no attribute 'append'

# print(1 + '1') #TypeError: unsupported operand type(s) for +: 'int' and 'str'
{1, 2, 1, 1}[1]  # TypeError: 'set' object is not subscriptable
# len(123) #TypeError: object of type 'int' has no len()


def hello(name):
    print(f'hello {name}')


hello('James')
# hello() #TypeError: hello() missing 1 required positional argument: 'name'
# hello('James', 'Danny') #TypeError: hello() takes 1 positional argument but 2 were given

# colors[2]  # IndexError: list index out of range

staff = {
    'instructor': 'Danny',
    'TA': 'James'
}
# print(staff['masseuse']) #KeyError: 'masseuse'


counter = 0


def show_count():
    print(counter)
    counter += 1


# show_count() #UnboundLocalError: local variable 'counter' referenced before assignment


def break_python():
    print('whee!')
    break_python()


# break_python() #RecursionError: maximum recursion depth exceeded while calling a Python object


'''Catching errors'''

for i in range(20):
    try:
        if i is 7:
            raise TypeError('my religion says 7 is not a real number')
        if i is 13:
            raise ValueError('too spooky!')
        print(i)
    except TypeError as error:
        print(error)
    except:  # don't do this!
        print('something went wrong')
