import timeit

data = []
max_value = 100
min_valid = 10
max_valid = 97

data_list1 = list(range(max_value)) # 100000000
data_list2 = list(range(max_value))
# data_list3 = list(range(max_value)) # 99999997

#--------------------------------------------------------------------#
def sanitise_1(data):
    # process the low values in the list
    stop = 0
    for index, value in enumerate(data):
        if value >= min_valid:
            stop = index
            break

    del data[:stop]

#--------------------------------------------------------------------#
def sanitise_2(data):
    top_index = len(data) - 1
    for index, value in enumerate(reversed(data)):
        if value < min_valid or value > max_valid:
            del data[top_index - index]

#--------------------------------------------------------------------#
def sanitise_3(data):
    for index in range(len(data) - 1, -1, -1):
        if data[index] < min_valid or data[index] > max_valid:
            del data[index]

#--------------------------------------------------------------------#
if __name__ == "__main__":
    print("Timing")
    x = timeit.timeit("sanitise_1(data_list1)",
                      setup="from __main__ import sanitise_1,"
                            "data_list1",
                        number=1)
    print("{:15.15f}".format(x))
    y = timeit.timeit("sanitise_2(data_list2)",
                      setup="from __main__ import sanitise_2,"
                            "data_list2",
                      number=1)
    print("{:15.15f}".format(y))
    # z = timeit.timeit("sanitise_2(data_list2)",
    #                   setup="from __main__ import sanitise_2,"
    #                         "data_list2",
    #                   number=1)
    # print("{:15.15f}".format(z))

    # sanitise_1(data_list1)
    # print(data_list1)
    # sanitise_2(data_list2)
    # print(data_list2)
    # sanitise_3(data_list3)
    # print(data_list3)

# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160,
#         170, 183, 185, 187, 188, 191, 350, 360]

# data = [4, 5, 104, 105, 110, 120, 130, 130, 150, 160,
#         170, 183, 185, 187, 188, 191]

# data = [104, 105, 110, 120, 130, 130, 150, 160,
#         170, 183, 185, 187, 188, 191, 350, 360]

# data = [104, 105, 110, 120, 130, 130, 150,
#         160, 170, 183, 185, 187, 188, 191]

# data = [1041, 1051, 1101, 1201, 1301, 1301, 1501,
#          1601, 1701, 1831, 1851, 1871, 1881, 1911]


# The incorrect way of removing items from an iterable
# for index, value in enumerate(data):
#     if (value < min_valid) or (value > max_valid):
#         del data[index]

# print(data)
# del data[0:2]
# print(data)
# del data[14:]
# print(data)