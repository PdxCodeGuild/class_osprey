import re

test_string = """Mr. John Smith: 123-456-7890
Mrs. Jane Smith: 234---567-8901
Jack Smith: +1 345-678-9012
Jenny Smith: 456.789.....0123
Bob Smith: +9845 567-890-1234
Smith
Sophie Smithberg: 1 6789012345
George Greensmith: +1 (789) 012-3456
Peter Parker: 1 (890)123-4567
123-12-1234
"""

# captures every Smith with a J name
smith_family = r'J\w+ [Ss]mith\W'

# with honorifics!
smith_family = r'.* *J\w+ [Ss]mith\W'

# phone numbers without country codes
phone_numbers = r'\(?\d{3}[-\.) ]*\d{3}[-\. ]?\d{4}'

# phone numbers WITH country codes
phone_numbers = r'\+?(\d{0,3})[ -](\(?\d{3}[-\.) ]*\d{3}[-\. ]?\d{4})'


# match looks for a pattern match at the beginning of the string
# <re.Match object; span=(0, 15), match='Mr. John Smith:'>
print(re.match(smith_family, test_string))
print(re.match(phone_numbers, test_string))  # None

# search looks for a pattern match ANYWHERE in the string
print(re.search(phone_numbers, test_string))
print(re.search(r'abc', test_string))

# findall finds every match in the string, returns a list
print(re.findall(smith_family, test_string))
# if expression includes capture groups, the list wil be
# a list of tuples with one element for each group
# anything outside a capture group will be excluded from the results
print(re.findall(phone_numbers, test_string))
