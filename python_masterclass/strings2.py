number = "9,223;372:036 854,775;807"
separators = ''

for char in number:
    if not char.isnumeric():
        separators = separators + char

print(separators)

# This is how I want to code
values = ''.join(char if char not in separators else "" for char in number).split()
print(sum([int(val) for val in values]))