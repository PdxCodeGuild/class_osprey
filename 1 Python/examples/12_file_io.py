import string
from random import random, choice
'''Reading a file'''

absolute_path = '/home/dan/code-guild/class_osprey/1 Python/examples/data/frankenstein.txt'
relative_path = '1 Python/examples/data/fire-and-ice.txt'

with open(relative_path, 'r', encoding='utf-8') as file:
    contents: str = file.read()


'''Working with file contents'''

lines: list = contents.split('\n')

phrases = ['no cap', 'mood', 'fr fr']

new_contents = []
for line in lines:
    new_line = line.lower().strip(string.punctuation)
    new_line = new_line.replace('fire', 'fire🔥')
    new_line = new_line.replace(' ice', ' ice🧊')
    new_line = new_line.replace('’', '')

    if random() < 0.33:
        phrase = choice(phrases)
        new_line = new_line + ' ' + phrase

    new_contents.append(new_line)

# for l in new_contents:
#     print(l)


'''Writing to a file'''

out_path = '1 Python/examples/data/fire-and-ice-fr-fr.txt'

out_content: str = '\n'.join(new_contents)
print(out_content)

with open(out_path, 'w') as f:
    f.write(out_content)
