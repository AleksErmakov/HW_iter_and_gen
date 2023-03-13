# TASK 2

def flat_generator(list_of_lists):
    for elem in list_of_lists:
        for el in elem:
            yield el


# list_of_lists_1 = [
#     ['a', 'b', 'c'],
#     ['d', 'e', 'f', 'h', False],
#     [1, 2, None]
# ]
#
# for item in flat_generator(list_of_lists_1):
#     print(item)