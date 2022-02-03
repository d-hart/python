#13 entries
# data = [104, 101, 4, 105, 308, 103, 5,
#         107, 100, 306, 106, 102, 108]
# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160,
#         170, 183, 185, 187, 188, 191, 350, 360]

data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160,
        170, 183, 185, 187, 188, 191]

# data = [104, 105, 110, 120, 130, 130, 150, 160,
#         170, 183, 185, 187, 188, 191, 350, 360]

# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]

# data = [1041, 1051, 1101, 1201, 1301, 1301, 1501,
#          1601, 1701, 1831, 1851, 1871, 1881, 1911]
min_valid = 100
max_valid = 200

# for index in range(len(data) - 1, -1, -1):
    # if data[index] < min_valid or data[index] > max_valid:
        # print(index, data)
        # del data[index]
print(data)
top_index = len(data) - 1 # top_index = 12
for index, value in enumerate(reversed(data)):
    # When I used the reversed function with the enumerate function, 
    # the enumerate function was unaware that the value and index 
    # does not match up. Create a top index and subtract the 
    # difference to get the true index
    if value < min_valid or value > max_valid:
        print(top_index - index, value)
        del data[top_index - index]
print(data)

''' 
top-index - default enumerate index value
12-0
12-1
12-2
12-3
12-4
12-5
12-6
12-7
12-8
12-9
12-10
12-11
12-12
'''