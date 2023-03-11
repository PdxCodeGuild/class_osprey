with open('1 Python/examples/data/bands.csv', 'r') as file:
    text = file.read()

lines = text.split('\n')

for line in lines:
    values = line.split(',')
    print(values)

# lines[2] = lines[2].replace(lines[2][8:], 'BTS')
lines[2] = lines[2].replace('Radiohead', 'BTS')
print(lines)

with open('1 Python/examples/data/bands2.csv', 'w') as file:
    file.write('\n'.join(lines))
