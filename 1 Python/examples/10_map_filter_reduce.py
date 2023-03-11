from functools import reduce

'''Lambdas
anonymous functions!
can take any number of arguments, but can only have one expression

syntax:
lambda arg1, arg2, arg3: expression
lambda arg: expression if condition else expression2 
'''


lambda1 = lambda x: x + 10

print(lambda1(5))
print(lambda1(832))


lambda2 = lambda x: x * 2 if x > 3 else None

print(lambda2(2))
print(lambda2(20))



'''Map, Filter Reduce
these functions can sometimes replace loops or comprehensions
they take a function as an argument
'''

'''Map
produces a new copy with 1 new value for each original value
it takes a function as the first argument
the function must take one parameter
the function must return one thing
'''

nums: list = [1, 2, 3, 4, 5]


def square(num):
    return num ** 2


squared_nums = map(square, nums)
print(squared_nums)


# the map output is a generator object
# Generators are consumed as they are looped over

for num in squared_nums:
    print(num)

squared_list = list(squared_nums)



# map with lambda
squared_nums2 = map(lambda x: x ** 2, nums)
print(list(squared_nums2))


'''Filter
produces a new copy with ONLY the elements that meet a condition
it takes a function as the first argument
the function takes one parameter
the function must return True or False
'''


def find_odd(num):
    # if num % 2 == 1:
    #     return True
    # return False
    return num % 2


odd_nums = filter(find_odd, nums)
print(list(odd_nums))

# filter with lambda
odd_nums2 = filter(lambda x: x % 2, nums)
print(list(odd_nums2))


'''Reduce
returns a single value that gets built using a helper function
not a top-level function, import using functools

takes a function as the first argument
the function takes TWO arguments
arg1 is the reduced value (the value returned by the previous iteration)
arg2 is the next element in the iterable
'''


def sum_odds(num1, num2):
    if num2 % 2 == 1:
        return num1 + num2
    return num1


sum_of_odds = reduce(sum_odds, nums)
print(sum_of_odds)

# reduce with lambda
sum_of_odds2 = reduce(lambda num1, num2: num1 + num2 if num2 % 2 else num1, nums)
print(sum_of_odds2)

def make_sentence(a, b):
    return a + ' ' + b


words = ['I', 'love', 'Python', 'especially', 'reduce']
sentence = reduce(make_sentence, words)
print(sentence)

sentence2 = reduce(lambda a, b: a + ' ' + b, words)
print(sentence2)