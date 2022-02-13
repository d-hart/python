panagram = """The quick brown
fox jumps\tover
the lazy dog"""

words = panagram.split()
print(words)

numbers = "9,223,372,036,854,775,807"
print(numbers.split(","))

# values = "".join(char if char not in separators else " " for char in numbers).split
generated_list = ['9',' ',
                  '2', '2', '3', ' ',
                  '3', '7', '2', ' ',
                  '0', '3', '6', ' ',
                  '8', '5', '4', ' ',
                  '7', '7', '5', ' ',
                  '8', '0', '7']
values = "".join(generated_list)#.split()
print(values)
values_list = values.split()
print(values_list)
#------------------------------------------------------------------------#
# Use a for loop to produce a list of ints, rather than strings.
# You can either modify the contents of the 'values_list' list in place,
# or create a new list of ints

# Rell's answer - I used the 'generated_list' instead
for index in range(len(generated_list)-1, -1, -1):
    if generated_list[index] == ' ':
        del generated_list[index]
    else:
        if type(generated_list[index]) != int:
            generated_list[index] = int(generated_list[index])
            # print(type(generated_list[index]))
        else:
            print(type(generated_list[index]))
print(generated_list)

#------------------------------------------------------------------------#
# Instructor's 1st answer
# Advantage = This answer uses less memory because there is not separate list
# Disadvantage = This answer is more difficult to read
for index in range(len(values_list)):
    values_list[index] = int(values_list[index])
print(values_list)

#------------------------------------------------------------------------#
# Instructor's 2nd answer
# Advantage = Easier to read and understand for later
# Disadvantage = This answer has to create a separate list, therefore using more memory
integer_values = []
for value in values_list:
    integer_values.append(int(value))
print(integer_values) 