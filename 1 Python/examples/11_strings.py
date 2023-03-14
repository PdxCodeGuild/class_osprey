'''String library'''
import string

# print(string.ascii_letters)
# print(string.ascii_lowercase)
# print(string.ascii_uppercase)

# print(string.digits)
# print(string.hexdigits)
# print(string.punctuation)


'''Escape Characters'''

string_literal = 'this "is" a string'
string_literal = "this 'is' a string"
string_literal = 'this quote has "multiple" \'quote\' types'

multi_line_string = f'''

this string

        preserves whitespace

        you "can" use 'any' quote type in it
        {10 * 3}

'''

# escaped whitespace character
print('\tWelcome to Class Osprey \n\n\nIt\'s nice in here')


'''Raw string'''
raw_string = r'\n\nthis \tis a \'raw\' string\n\n'


'''Unicode characters'''

print('\u1234')
print('\u0123')
print('\u2345')
print('\u1992')
print('\u1985')
print('\u0019')


'''ASCII codes'''
print(ord('A'))
print(ord('B'))
print(ord('a'))

print(chr(67))

# for i in range(200):
#     print(f'ASCII code {i}: {chr(i)}')


'''Concatenation
use the + operator to combine strings'''

message = '\thello' + f'{" " * 1}' + 'world' + ''
print(message)


'''String methods
.upper()
.lower()
.capitalize() just the first char
.title() capitalize the first char after every whitespace
'''

# .find(substring) returns the index of
# the beginning of the first instance of substring
print(message.find('world'))  # 7
print(message.find('w'))  # 7
print(message.find('l'))  # 3

'''Split and join'''
# .split(separator) returns a list of substrings separated by given separator
sentence = 'Liam has three cats'

# separates on whitespace by default
print(sentence.split('a'))
# if you use a separator that is not present, it returns the whole string
print(sentence.split('x'))
words = sentence.split()

# string.join(iterable) returns a string with the elements from the iterable
# joined by the string that the method is called on

print('-'.join(words))

silly_string = "!  ! ! ! ! !"
exclamation_points = silly_string.split(' ')
print(exclamation_points)

# exclamation_points.join('$') #AttributeError: 'list' object has no attribute 'join'
new_string = "$".join(exclamation_points)
print(new_string)


'''Strip'''

message = '--@-----hello-world----@---'

print(message.strip('-'))
# each character in the parameter will be stripped, it's not a substring
print(message.strip('-@'))
print(message.strip('@-'))

print(message.lstrip('-@'))
print(message.rstrip('-@'))

long_message = '''

          this is a long message

'''

print(long_message.strip())


'''Replace
finds every instance of a substring and replaces it
returns a new copy
'''

print(message.replace('-', '&'))  # &&@&&&&&hello&world&&&&@&&&
print(message.replace('-', ''))  # @helloworld@
print(message.replace('-', '').replace('@', ''))


message = "@(%&@)&($(@@&here is a message)@(*&%^)@(#*$)@(#$"
print(message.strip(string.punctuation))
