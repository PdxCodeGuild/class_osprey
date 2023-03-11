sample_dict = {
    'one': 1,
    'two': 2,
    'three': 3
}


# access using brackets
print(sample_dict['two'])
# print(sample_dict['four'])
# KeyError: 'four'


# access using dict.get()
print(sample_dict.get('two'))
print(sample_dict.get('four'))  # None


if sample_dict.get('four') is None:
    # do something
    pass


sample_dict['four'] = 4
sample_dict.update({'five': 5})
print(sample_dict)


print(sample_dict['five'] * sample_dict.get('four'))
